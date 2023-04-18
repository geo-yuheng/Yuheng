import unittest
from os.path import dirname, join, realpath

from src import keqing


class TestLoadAbbreviation(unittest.TestCase):
    def setUp(self) -> None:
        self.map = keqing.Waifu()

    def test_load_abbreviation(self):
        FILENAME = "OSMWebsite_export.osm"
        data_path = join(dirname(realpath(__file__)), "extract", FILENAME)
        self.map.read(mode="f", fpath=data_path)
        m = self.map
        assert len(m.bounds_list) == 1
        assert len(m.node_dict) == 11818
        assert len(m.way_dict) == 2376
        assert len(m.relation_dict) == 14


if __name__ == "__main__":
    unittest.main()
