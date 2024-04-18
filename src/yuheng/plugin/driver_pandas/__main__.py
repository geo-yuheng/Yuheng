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


def transform(world: Carto) -> pd.DataFrame:
    """
    读取world中所有element的tag，转换为一个DataFrame
    """
    # 初始化一个空 DataFrame，列名包括所有元素（node, way, relation）'tags' 字典的所有键
    all_tags_keys = set.union(
        *[set(e.tags.keys()) for e in world.node_dict.values()],
        *[set(e.tags.keys()) for e in world.way_dict.values()],
        *[set(e.tags.keys()) for e in world.relation_dict.values()]
    )
    # 将 all_tags_keys 转换为列表
    all_tags_keys = list(all_tags_keys)
    df = pd.DataFrame(columns=all_tags_keys)

    # 遍历并处理 node, way 和 relation 的 tags
    for node_id, element in world.node_dict.items():
        temp_series = pd.Series(element.tags, index=df.columns)
        df = df.append(temp_series, ignore_index=True)

    for way_id, element in world.way_dict.items():
        temp_series = pd.Series(element.tags, index=df.columns)
        df = df.append(temp_series, ignore_index=True)

    for relation_id, element in world.relation_dict.items():
        temp_series = pd.Series(element.tags, index=df.columns)
        df = df.append(temp_series, ignore_index=True)
    print(
        len(df),
        len(world.node_dict),
        len(world.way_dict),
        len(world.relation_dict),
    )
    return df

def read() -> Carto:
    pass

def write() -> pd.DataFrame:
    pass

def main() -> None:
    logger.error("This plugin can't be run as module.")


if __name__ == "__main__":
    main()
