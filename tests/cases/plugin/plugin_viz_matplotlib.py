import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..", "src")
sys.path.append(src_dir)

from yuheng import Carto
from yuheng.component import Member, Node, Relation, Way
from yuheng_plugin.yuheng_viz_matplotlib.__main__ import init


class TestPluginVisualizationMatplotlib(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_plugin_viz_folium_display_object(self):
        init(1600, 900, 12.5, -3, -2.7, 6.66)


if __name__ == "__main__":
    unittest.main()
