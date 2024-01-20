import os
import argparse
import sys
from typing import Dict, List, Tuple, Union


current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Waifu


def extractor(poly_file_path: str) -> str:
    poly_file = open(poly_file_path, "r", encoding="utf-8")
    poly_content = poly_file.read()
    poly_file.close()
    return poly_content


def transformer(
    line_str: str, **kwargs
) -> Union[Dict[str, float], List[float], Tuple[float, float]]:
    if kwargs.get("schema") == None:
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
    return carto_object


def main(
    poly_file_path: str,
    schema=None,
    order=None,
    output_format="raw",
    **kwargs: dict
) -> List[Dict[str, float]]:
    # 暂时只处理单一环路的poly文件

    # 文件处理
    poly_content: List[str] = (
        extractor(poly_file_path).split("END")[0].split("\n")[2:]
    )
    poly_object: List[Dict[str, float]] = [
        transformer(i[3:], schema=schema, order=order)
        for i in list(filter(bool, poly_content))
    ]
    if output_format.lower() == "raw":
        return poly_object
    if output_format.lower() == "yuheng":
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
        "--output-format", type=str, default="raw", dest="output-format"
    )

    main(**argument_parser.parse_args().__dict__)
