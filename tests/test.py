import unittest
from os.path import dirname, join, realpath

from kqs.waifu import Waifu


# A simple example for testing
class TestClass(unittest.TestCase):
    data_path = join(
        dirname(realpath(__file__)), "export", "OSMWebsite_export.osm"
    )

    def setUp(self) -> None:
        self.map = Waifu()
        self.map.read_file(self.data_path)

    def test_entity_count(self):
        m = self.map
        assert len(m.bounds_list) == 1
        assert len(m.node_dict) == 11818
        assert len(m.way_dict) == 2376
        assert len(m.relation_dict) == 14

    def test_entity_count_JOSM(self):
        m = self.map
        assert len(m.bounds_list) == 1
        assert len(m.node_dict) == 539
        assert len(m.way_dict) == 67
        assert len(m.relation_dict) == 5

    def test_entity_count_level0(self):
        m = self.map
        # level0 test failed because current program can't handle element without lat, e.g.: <node id='3328159064' version='2' action='delete' timestamp='2021-11-28T05:14:24+00:00'>
        assert len(m.bounds_list) == 0
        assert len(m.node_dict) == 0
        assert len(m.way_dict) == 0
        assert len(m.relation_dict) == 0


if __name__ == "__main__":
    unittest.main()
