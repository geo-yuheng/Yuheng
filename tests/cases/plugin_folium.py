import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

from yuheng import Way, Node, Relation, Waifu, Member
from yuheng.plugin.folium.__main__ import display


class TestPluginFolium(unittest.TestCase):
    def setUp(self) -> None:
        from yuheng.plugin.folium.__main__ import display

        self.test_node_1 = Node(
            {"id": "1"}, {"name": "folium cafe", "amenity": "cafe"}
        )
        self.test_node_2 = Node(
            {"id": "2"}, {"name": "yuheng restaurant", "amenity": "restaurant"}
        )
        self.test_way = Way(
            {"id": "10"}, {"cuisine": "chinese;chicken;bubble_tea"}, [1, 2]
        )
        self.test_relation = Relation(
            {"id": "100"},
            {"highway": "food"},
            [
                Member(element_type="node", role="dessert", ref=1),
                Member(element_type="node", role="dessert", ref=2),
                Member(element_type="way", role="meal", ref=10),
            ],
        )
        self.test_map = Waifu()

    def test_plugin_driver_poly_import(self):
        display(self.test_relation)


if __name__ == "__main__":
    unittest.main()
