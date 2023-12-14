# import os
from typing import Dict, List


def main(poly_file_path: str) -> List[Dict[str, float]]:
    # 暂时只处理单一环路的poly文件

    # 文件读取
    poly_file = open(poly_file_path, "r", encoding="utf-8")
    poly_content = poly_file.read()
    poly_file.close()

    # 文件处理
    poly_content = poly_content.split("END")[0].split("\n")[2:]
    poly_object = [
        dict(zip(["latitude", "longitude"], i[3:].split("   ")))
        for i in list(filter(bool, poly_content))
    ]
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
