import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

from yuheng import Carto
from yuheng.component import Node, Relation, Way
from yuheng.plugin.stat_metadata_clustering.__main__ import main


class TestPluginVisualizationFolium(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_plugin_viz_folium_display_invalid_argument(self):
        pass


if __name__ == "__main__":
    unittest.main()
