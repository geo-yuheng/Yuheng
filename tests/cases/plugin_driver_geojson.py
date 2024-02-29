# 每个对象访问一边完整的内容或者指定内容看是否出错

import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)


class TestPluginDriverPoly(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_plugin_driver_geojson_import(self):
        from yuheng.plugin.driver_geojson.__main__ import read
        from pprint import pprint

        ans = read(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "assets",
                "geojson",
                "geojsonio-ring2.geojson",
                # "geojsonio-commute-bus.geojson",
            ),
            output_target="yuheng",
        )
        pprint(ans)


if __name__ == "__main__":
    unittest.main()
