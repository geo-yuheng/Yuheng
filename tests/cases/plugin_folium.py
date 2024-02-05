import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)


class TestPluginDriverPoly(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_plugin_driver_poly_import(self):
        from yuheng.plugin.folium.__main__ import display

        test_way = Way()
        test_node = Node()
        test_relation = Relation()
        test_map = Waifu()

        display()

    def test_plugin_driver_poly_cli(self):
        pass


if __name__ == "__main__":
    unittest.main()
