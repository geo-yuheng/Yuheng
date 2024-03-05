import argparse
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Carto
from yuheng.component import Node, Way, Relation


def main(obj):
    # if run in standalone cli, only support input a xml file and then parse it to Carto
    # if run by import, both parse xml or pass Carto object is acceptable.
    if isinstance(obj, type(str)):
        # parse mode
        pass
    else:
        world = obj


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--file", type=str, default=True, dest="file")
    main(**argument_parser.parse_args().__dict__)
