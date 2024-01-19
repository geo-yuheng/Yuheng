import os


def main(json_file_path: str, schema=None, order=None):
    # 文件读取
    json_file = open(json_file_path, "r", encoding="utf-8")
    json_content = json_file.read()
    json_file.close()

    print(json_content)


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
            "map.geojson",
        )
    )
