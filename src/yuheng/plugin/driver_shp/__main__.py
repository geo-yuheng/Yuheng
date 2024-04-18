import argparse
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from src.yuheng import logger


def write():
    logger.error("暂不支持输出为shp文件")
    pass

def read(shp_file_path: str = "", schema=None, order=None, **kwargs):
    # 文件读取
    shp_file = open(shp_file_path, "r", encoding="utf-8")
    shp_content = shp_file.read()
    shp_file.close()

    logger.debug(shp_content)


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--shp_file_path", type=str, dest="shp_file_path"
    )
    read(**argument_parser.parse_args().__dict__)