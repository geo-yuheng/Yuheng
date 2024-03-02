import argparse
import os
import sys
from pprint import pprint
from typing import Union

import geojson

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)


from yuheng import Carto


def read(
    input_file_path: str, output_target="geojson"
) -> Union[dict, str, geojson.feature.FeatureCollection, Carto]:
    """
    ourput_target:
    * yuheng: 输出Carto对象
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
        pprint(dict(geojson_obj))

        def is_valid_geojson_element(element_dict):
            key_list = [key for key in element_dict]
            if "type" not in key_list:
                return False
            else:
                # There still can contain more validation
                return True

        def parse_geojson_element(element_dict):
            pass

        for key in geojson_obj:
            if key == "type" and geojson_obj[key] == "FeatureCollection":
                features = list(geojson_obj["features"])
                # print(type(features))
                # print(features)
        pass
    else:
        return geojson_obj


def write(
    yuheng_obj: Carto, output_target=None, **kwargs
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

    for id in Carto.way_dict:
        single_node = Carto.way_dict[id]
        geojson_point_ojb = Point(single_node.lon, single_node.lat)
    pass


if __name__ == "__main__":
    main()
