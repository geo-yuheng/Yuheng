# 每个对象访问一边完整的内容或者指定内容看是否出错

import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

from yuheng.basic import logger
from yuheng.plugin.overpass import gen_metadata


class TestPluginOverpass(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_plugin_overpass(self):
        logger.info(
            gen_metadata(metadata_entry_data={"out": "xml", "maxsize": 65535})
        )
        logger.info(
            gen_metadata(
                metadata_entry_data={"out": "popup", "maxsize": 65535}
            )
        )
        logger.info(
            gen_metadata(
                metadata_entry_data={
                    "out": "json",
                    "timeout": 255,
                    "bbox": "whatever",
                },
                bbox_info={"E": 20, "W": 10, "S": 30, "N": 40.5},
            )
        )
        logger.info(
            gen_metadata(
                metadata_entry_data={
                    "out": "csv",
                    "timeout": 255,
                },
                csv_info={
                    "query_key_list": ["amenity", "addr:city", "admin_level"],
                    "explicit_declare_header": True,
                    "delimiter": "|",
                },
            )
        )


if __name__ == "__main__":
    unittest.main()
