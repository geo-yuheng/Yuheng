import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

import yuheng


class TestLoadAbbreviation(unittest.TestCase):
    def setUp(self) -> None:
        self.world = yuheng.Waifu()

    def test_load_abbreviation(self):
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


if __name__ == "__main__":
    unittest.main()
