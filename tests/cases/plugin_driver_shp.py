import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

from yuheng.basic import logger


class TestPluginDriverShp(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_plugin_driver_shp(self):
        from yuheng.plugin.driver_shp.__main__ import main

        pass

if __name__ == "__main__":
    unittest.main()
