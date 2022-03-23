import unittest
from os.path import join, realpath, dirname

from kqs_class import Waifu

# A simple example for testing
class TestClass(unittest.TestCase):
    data_path = join(
        dirname(realpath(__file__)), "export", "OSMWebsite_export.osm"
    )

    def setUp(self) -> None:
        self.map = Waifu()
        self.map.from_file(self.data_path)

    def test_entity_count(self):
        m = self.map
        assert len(m.bounds_list) == 1
        assert len(m.node_dict) == 11818
        assert len(m.way_dict) == 2376
        assert len(m.relation_dict) == 14


if __name__ == "__main__":
    unittest.main()
