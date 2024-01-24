import os


def main(shp_file_path: str, schema=None, order=None):
    # 文件读取
    shp_file = open(shp_file_path, "r", encoding="utf-8")
    shp_content = shp_file.read()
    shp_file.close()

    print(shp_content)


if __name__ == "__main__":
    main(
        os.path.join(
            os.getcwd(),
            "..",
            "..",
            "..",
            "..",
            "tests",
            "testcase-round2",
            "map.topojson",
        )
    )
