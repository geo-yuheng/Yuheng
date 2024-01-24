import os
import geojson

def read(json_file_path: str, output_target=None)->geojson.feature.FeatureCollection:
    """
    ourput_target: 输出其他某种文本格式？直出库读出来的geojson对象？dict？某种特定的字符串序列化？Waifu？
    """
    # 文件读取
    json_file = open(json_file_path, "r", encoding="utf-8")
    json_content = json_file.read()
    json_file.close()
    geojson_obj=geojson.loads(json_content)

    from pprint import pprint
    pprint(geojson_obj)
    return geojson_obj

def write():
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
