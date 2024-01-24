import os
import sys

import geojson

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Waifu


def read(
    json_file_path: str, output_target=None
) -> Union[dict, str, geojson.feature.FeatureCollection, Waifu]:
    """
    ourput_target:
    * yuheng: 输出Waifu对象
    * dict: 输出Python原生的dict对象
    * geojson: 输出geojson.feature.FeatureCollection对象
    * serialize: 输出特定格式的序列化字符串对象
    """
    json_file = open(json_file_path, "r", encoding="utf-8")
    json_content = json_file.read()
    json_file.close()
    geojson_obj = geojson.loads(json_content)

    from pprint import pprint

    pprint(geojson_obj)
    return geojson_obj


def write(
    yuheng_obj: Waifu, output_target=None, **kwargs
) -> Union[dict, str, geojson.feature.FeatureCollection]:
    """
    ourput_target:
    * dict: 输出Python原生的dict对象
    * str: 输出将geojson序列化后的字符串对象
    * geojson: 输出geojson.feature.FeatureCollection对象
    flag:
    读到的node使用若干个Point还是MultiPoint
    """
    from geojson import Point

    for id in Waifu.way_dict:
        single_node = Waifu.way_dict[id]
        geojson_point_ojb = Point(single_node.lon, single_node.lat)
    pass


if __name__ == "__main__":
    read(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "..",
            "..",
            "tests",
            "assets",
            "geojson",
            "geojsonio-ring2.geojson",
        )
    )
