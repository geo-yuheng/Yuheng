import os
import sys
from typing import Union

import geojson

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Waifu


def read(
    input_file_path: str, output_target="geojson"
) -> Union[dict, str, geojson.feature.FeatureCollection, Waifu]:
    """
    ourput_target:
    * yuheng: 输出Waifu对象
    * dict: 输出Python原生的dict对象
    * geojson: 输出geojson.feature.FeatureCollection对象
    * serialize: 输出特定格式的序列化字符串对象
    """
    geojson_file = open(input_file_path, "r", encoding="utf-8")
    geojson_content = geojson_file.read()
    geojson_file.close()
    geojson_obj = geojson.loads(geojson_content)

    if output_target == "geojson":
        return geojson_obj
    elif output_target == "dict":
        return dict(geojson_obj)
    elif output_target == "str":
        return ""  # 因为返回模式还没设计
    elif output_target == "yuheng":
        # 真正的人上人——中间格式！
        print(dict(geojson_obj))
        for key in geojson_obj:
            if key == "type" and geojson_obj[key] == "FeatureCollection":
                # geojson.io生成的都是这种
                features = list(geojson_obj["features"])
                # print(type(features))
                # print(features)
        pass
    else:
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
    from pprint import pprint

    ans = read(
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
            # "geojsonio-commute-bus.geojson",
        ),
        output_target="yuheng",
    )
    pprint(ans)
