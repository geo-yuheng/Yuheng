# import os
from typing import Dict, List, Tuple, Union


def main(
    poly_file_path: str, schema=None, order=None
) -> List[Dict[str, float]]:
    # 暂时只处理单一环路的poly文件

    # 文件读取
    poly_file = open(poly_file_path, "r", encoding="utf-8")
    poly_content = poly_file.read()
    poly_file.close()

    # 文件处理
    poly_content = poly_content.split("END")[0].split("\n")[2:]

    def line2node(
        line_str: str,
    ) -> Union[Dict[str, float], List[float], Tuple[float, float]]:
        if schema == None:
            return dict(
                zip(
                    ["longitude", "latitude"],  # ["经度", "纬度"]
                    [float(f) for f in line_str.split("   ")],
                )
            )
        elif isinstance(schema, type([])):
            if order == "lon-lat":
                return [float(f) for f in line_str.split("   ")]
            else:  # lat-lon
                return list(
                    reversed([float(f) for f in line_str.split("   ")])
                )
        elif isinstance(schema, type(())):
            if order == "lon-lat":
                return tuple([float(f) for f in line_str.split("   ")])
            else:  # lat-lon
                return tuple(
                    reversed([float(f) for f in line_str.split("   ")])
                )
        pass

    poly_object = [line2node(i[3:]) for i in list(filter(bool, poly_content))]
    print(poly_object)
    return poly_object


if __name__ == "__main__":
    main("polyfile.poly")
    # # For Debug
    # main(
    #     os.path.join(
    #         os.getcwd(),
    #         "..",
    #         "..",
    #         "..",
    #         "..",
    #         "tests",
    #         "poly",
    #         "Izaland-polyfile-20231213-laoshubabytest.poly",
    #     )
    # )
