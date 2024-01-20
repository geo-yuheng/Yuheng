import os
import argparse
import sys
from typing import Dict, List, Tuple, Union


current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Waifu
from yuheng.type import Node, Way


def extractor(poly_file_path: str) -> str:
    poly_file = open(poly_file_path, "r", encoding="utf-8")
    poly_content = poly_file.read()
    poly_file.close()
    return poly_content


def transformer(
    line_str: str, **kwargs
) -> Union[Dict[str, float], List[float], Tuple[float, float]]:
    if (
        kwargs.get("schema") == None
        or kwargs.get("schema", "").lower() == "dict"
    ):
        return dict(
            zip(
                ["longitude", "latitude"],  # ["经度", "纬度"]
                [float(f) for f in line_str.split("   ")],
            )
        )
    elif kwargs.get("schema", "").lower() == "list":
        if kwargs.get("order", None) == "lon-lat":
            return [float(f) for f in line_str.split("   ")]
        else:  # lat-lon
            return list(reversed([float(f) for f in line_str.split("   ")]))
    elif kwargs.get("schema", "").lower() == "tuple":
        if kwargs.get("order", None) == "lon-lat":
            return tuple([float(f) for f in line_str.split("   ")])
        else:  # lat-lon
            return tuple(reversed([float(f) for f in line_str.split("   ")]))
    pass


def load(
    poly_object: List[Dict[str, float]], output_format="yuheng"
) -> Union[None, Waifu]:
    carto_object = Waifu()
    node_obj_list = []
    for i in range(len(poly_object)):
        node_obj_list.append(
            Node(
                attrib={
                    "id": str(i),
                    "visible": "true",
                    "version": "1",
                    "changeset": "-1",
                    "timestamp": "1970-01-01T00:00:00Z",
                    "user": "plugin_driver_poly",
                    "uid": "1",
                    "lat": poly_object[i].get("latitude"),
                    "lon": poly_object[i].get("longitude"),
                },
                tag_dict={},
            )
        )
    node_id_list = [i.id for i in node_obj_list]
    poly_way = Way(
        attrib={
            "id": "1",
            "visible": "true",
            "version": "1",
            "changeset": "1",
            "timestamp": "1970-01-01T00:00:00Z",
            "user": "plugin_driver_poly",
            "uid": "1",
        },
        tag_dict={},
        nd_list=node_id_list,
    )

    # 这个函数是从test_type_constructor抄来的，后续建议转正
    def insert_to_dict(spec_dict, element_list):
        for i in element_list:
            spec_dict[int(i.id)] = i

    insert_to_dict(carto_object.node_dict, node_obj_list)
    insert_to_dict(carto_object.way_dict, [poly_way])

    return carto_object


def main(
    poly_file_path: str, schema=None, order=None, output_format="raw", **kwargs
) -> List[Dict[str, float]]:
    # 暂时只处理单一环路的poly文件

    poly_content: List[str] = (
        extractor(poly_file_path).split("END")[0].split("\n")[2:]
    )
    poly_object: List[Dict[str, float]] = [
        transformer(i[3:], schema=schema, order=order)
        for i in list(filter(bool, poly_content))
    ]

    if output_format.lower() == "raw":
        return poly_object
    elif output_format.lower() == "yuheng":
        return load(poly_object)
    else:
        return poly_object


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--poly_file_path", type=str, dest="poly_file_path"
    )
    argument_parser.add_argument("--schema", default=None, dest="schema")
    argument_parser.add_argument("--order", default=None, dest="order")
    argument_parser.add_argument(
        "--output-format", type=str, default="raw", dest="output_format"
    )

    main(**argument_parser.parse_args().__dict__)
