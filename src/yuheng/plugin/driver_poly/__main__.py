import os
from typing import Dict, List, Tuple, Union


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
    elif isinstance(kwargs.get("schema", None), type([])):
        if kwargs.get("order", None) == "lon-lat":
            return [float(f) for f in line_str.split("   ")]
        else:  # lat-lon
            return list(reversed([float(f) for f in line_str.split("   ")]))
    elif isinstance(kwargs.get("schema", None), type(())):
        if kwargs.get("order", None) == "lon-lat":
            return tuple([float(f) for f in line_str.split("   ")])
        else:  # lat-lon
            return tuple(reversed([float(f) for f in line_str.split("   ")]))
    pass


def main(
    poly_file_path: str, schema=None, order=None, output_format="raw"
) -> List[Dict[str, float]]:
    # 暂时只处理单一环路的poly文件

    # 文件处理
    poly_content = extractor(poly_file_path).split("END")[0].split("\n")[2:]

    poly_object = [
        transformer(i[3:], schema=schema, order=order)
        for i in list(filter(bool, poly_content))
    ]
    if output_format == "raw":
        print(poly_object)
        return poly_object
    else:
        return poly_object


if __name__ == "__main__":
    # main("polyfile.poly")
    # # For Debug
    main(
        os.path.join(
            os.getcwd(),
            "..",
            "..",
            "..",
            "..",
            "tests",
            "poly",
            "Izaland-polyfile-20231213-laoshubabytest.poly",
        )
    )
