import argparse
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from src.yuheng import logger


def main(json_file_path: str = "", schema=None, order=None, **kwargs):
    # 文件读取
    json_file = open(json_file_path, "r", encoding="utf-8")
    json_content = json_file.read()
    json_file.close()

    logger.debug(json_content)


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--json_file_path", type=str, dest="json_file_path"
    )
    main(**argument_parser.parse_args().__dict__)
