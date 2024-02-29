import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

import yuheng


class TestLoadFile(unittest.TestCase):
    def setUp(self) -> None:
        self.world = yuheng.Carto()

    def test_load_file_OSMWebsite(self):
        FILENAME = "extract_osmwebsite_bbox_weihaichengshantou.osm"
        data_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "..",
            "assets",
            "osm",
            FILENAME,
        )
        self.world.read(mode="file", file_path=data_path)
        m = self.world
        assert len(m.bounds_list) == 1
        assert len(m.node_dict) == 11818
        assert len(m.way_dict) == 2376
        assert len(m.relation_dict) == 14

    def test_load_file_JOSM(self):
        FILENAME = "extract_josm_bbox_qingzhou.osm"
        data_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "..",
            "assets",
            "osm",
            FILENAME,
        )
        self.world.read(mode="file", file_path=data_path)
        m = self.world
        assert len(m.bounds_list) == 1
        assert len(m.node_dict) == 539
        assert len(m.way_dict) == 67
        assert len(m.relation_dict) == 5

    def test_load_file_level0(self):
        FILENAME = "extract_level0_newdata.osm"
        data_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "..",
            "assets",
            "osm",
            FILENAME,
        )
        self.world.read(mode="file", file_path=data_path)
        m = self.world
        # level0 test failed because current program can't handle element without lat, e.g.: <node id='3328159064' version='2' action='delete' timestamp='2021-11-28T05:14:24+00:00'>
        assert len(m.bounds_list) == 0
        assert len(m.node_dict) == 478
        assert len(m.way_dict) == 22
        assert len(m.relation_dict) == 0


if __name__ == "__main__":
    unittest.main()
