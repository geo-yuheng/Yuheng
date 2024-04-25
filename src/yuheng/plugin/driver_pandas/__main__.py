import pandas as pd

# not geopandas

import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Carto
from yuheng.basic import logger
from yuheng.component import Member, Node, Relation, Way

import time


@logger.catch()
def transform(world: Carto) -> pd.DataFrame:
    all_elements = []

    def collect_to_list(element_dict: dict, type: str):
        for element_id, element_obj in element_dict.items():
            element_data = {
                "id": type[0] + str(element_id),
                **element_obj.tags,
            }
            all_elements.append(element_data)

    for e in [
        (world.node_dict, "node"),
        (world.way_dict, "way"),
        (world.relation_dict, "relation"),
    ]:
        collect_to_list(e[0], e[1])
    return pd.DataFrame(all_elements)


def read() -> Carto:
    pass


def write() -> pd.DataFrame:
    pass


def main() -> None:
    logger.error("This plugin can't be run as module.")


if __name__ == "__main__":
    main()
