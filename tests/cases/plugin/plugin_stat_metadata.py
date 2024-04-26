import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

from yuheng import Carto
from yuheng.basic import logger
from yuheng.component import Node, Relation, Way
from yuheng.plugin.stat_metadata_clustering.__main__ import main


class TestPluginStatMetadata(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_plugin_stat_metadata_argument(self):
        command = " ".join(
            [
                "python",
                (
                    '"'
                    + os.path.join(
                        os.path.dirname(__file__),
                        "..",
                        "..",
                        "src",
                        "yuheng",
                        "yuheng_plugin",
                        "yuheng_stat_metadata_clustering",
                        "__main__.py",
                    )
                    + '"'
                ),
                "--file",
                (
                    '"'
                    + os.path.join(
                        os.path.dirname(__file__),
                        "..",
                        "assets",
                        "osm",
                        "extract_osmwebsite_bbox_buctcampus.osm",
                    )
                    + '"'
                ),
            ]
        )
        logger.info(command)
        os.system(command)

    def test_plugin_stat_metadata_import(self):
        world = Carto()
        result = main(world=world)

    def test_plugin_stat_metadata_import_invalid(self):
        world = {"type": "carto", "content": "map"}
        result = main(world=world)


if __name__ == "__main__":
    unittest.main()
