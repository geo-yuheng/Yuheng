import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

from yuheng.basic import logger


class TestPluginDriverTopojson(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_plugin_driver_topojson(self):
        from yuheng.plugin.driver_topojson.__main__ import read

        read(
            os.path.join(
                os.getcwd(),
                "..",
                "assets",
                "topojson",
                "geojsonio-ring2.topojson",
            )
        )


if __name__ == "__main__":
    unittest.main()
