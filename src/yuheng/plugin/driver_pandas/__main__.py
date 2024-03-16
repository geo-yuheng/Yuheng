import pandas

# not geopandas

import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Carto
from yuheng.basic import logger
from yuheng.component import Member, Node, Relation, Way


def transform(world: Carto) -> pandas.DataFrame:
    """
    读取world中所有element的tag，转换为一个DataFrame
    """
    df = pandas.DataFrame()
    for node_id, element in world.node_dict.items():
        temp_tags = element.tags
        df = df.append(temp_tags, ignore_index=True)
    for way_id, element in world.way_dict.items():
        temp_tags = element.tags
        df = df.append(temp_tags, ignore_index=True)
    for relation_id, element in world.relation_dict.items():
        temp_tags = element.tags
        df = df.append(temp_tags, ignore_index=True)
    print(
        len(df),
        len(world.node_dict),
        len(world.way_dict),
        len(world.relation_dict),
    )


def main() -> None:
    logger.error("This plugin can't be run as module.")


if __name__ == "__main__":
    main()
