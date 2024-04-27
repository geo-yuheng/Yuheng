# 每个对象访问一边完整的内容或者指定内容看是否出错

import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..", "src")
sys.path.append(src_dir)

from yuheng.basic import logger


class TestPluginDriverPoly(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_plugin_driver_geojson_import(self):
        # from pprint import pprint

        from yuheng_plugin.yuheng_driver_geojson.__main__ import read

        ans = read(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "assets",
                "geojson",
                "geojsonio-ring2.geojson",
                # "geojsonio-commute-bus.geojson",
            ),
            output_target="yuheng",
        )
        # pprint(ans)
        logger.info(dict(ans))


if __name__ == "__main__":
    unittest.main()
