# 每个对象访问一边完整的内容或者指定内容看是否出错

import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

from yuheng.basic import logger
from yuheng.plugin.overpass import get_query_parts, parse, remove_comment


class TestPluginOverpass(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_plugin_overpass_parse(self):
        with open(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "..",
                "assets",
                "overpassql",
                "wizard_generated_beijing_building.overpassql",
            ),
            "r",
            encoding="utf-8",
        ) as f:
            query_content = f.read()
        logger.debug(f"\n{query_content}")
        logger.info(f"\n{remove_comment(query_content)}")
        query_parts = get_query_parts(query_content)
        logger.info(f"\n{query_parts}")
        parsed_query_parts = parse(query_parts)
        logger.info(f"\n{parsed_query_parts}")


if __name__ == "__main__":
    unittest.main()
