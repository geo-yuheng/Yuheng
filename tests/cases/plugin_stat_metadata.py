import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

from yuheng import Carto
from yuheng.component import Node, Relation, Way
from yuheng.plugin.stat_metadata_clustering.__main__ import main


class TestPluginStatMetadata(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_plugin_stat_metadata_argument(self):
        os.system(
            " ".join(
                [
                    "python",
                    os.path.join(
                        os.path.realpath(__file__),
                        "..",
                        "..",
                        "src",
                        "yuheng",
                        "plugin",
                        "stat_metadata_clustering",
                        "__main__.py",
                    ),
                    os.path.join(
                        os.path.realpath(__file__),
                        "..",
                        "assets",
                        "osm",
                        "xtract_osmwebsite_bbox_buctcampus.osm",
                    ),
                ]
            )
        )

    def test_plugin_stat_metadata_import(self):
        world = Carto()
        result = main(world)


if __name__ == "__main__":
    unittest.main()
