import argparse
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Carto
from yuheng.basic import logger
from yuheng.component import Node, Way, Relation


def main(**kwargs):
    # if run in standalone cli, only support input a xml file and then parse it to Carto
    # if run by import, both parse xml or pass Carto object is acceptable.
    for k, v in kwargs.items():
        logger.debug(v)

        if isinstance(v, str):
            # parse mode
            if v[0:5] != "<?xml":
                # this is a file path
                logger.debug("this is a file path")
                logger.info(v)
                world = Carto()
                world.read(mode="file", file_path=v)
            else:
                logger.debug("this is a text")
                world = Carto()
                world.read(mode="memory", text=v)
        elif isinstance(v, type(Carto())):
            world = v
            world.meow()
        else:
            logger.info(f'Unrecognizable value from key "{k}"')
            pass

        # reverse
        metadata_frame = []
        for id, element in world.node_dict.items():
            metadata_frame.append(("n" + str(element.id), element.timestamp))
        for id, element in world.way_dict.items():
            metadata_frame.append(("w" + str(element.id), element.timestamp))
        for id, element in world.relation_dict.items():
            metadata_frame.append(("r" + str(element.id), element.timestamp))
        logger.debug(metadata_frame[0])
        logger.debug(len(metadata_frame))


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--file", type=str, default=True, dest="file")
    main(**argument_parser.parse_args().__dict__)
