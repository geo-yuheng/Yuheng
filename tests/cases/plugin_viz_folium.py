import os
import sys
import unittest


current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

from yuheng import Carto
from yuheng.type import Member, Node, Relation, Way
from yuheng.plugin.viz_folium.__main__ import VizFolium


class TestPluginVisualizationFolium(unittest.TestCase):
    def setUp(self) -> None:
        self.test_node_1 = Node(
            {"id": "1", "lat": 1.14, "lon": 5.14},
            {"name": "folium cafe", "amenity": "cafe"},
        )
        self.test_node_2 = Node(
            {"id": "2", "lat": 19.19, "lon": 8.10},
            {"name": "yuheng restaurant", "amenity": "restaurant"},
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
        self.test_map = Carto()
        # 需要插入到Carto对象里面。
        # self.test_map.insert(
        #     self.test_node_1,
        #     self.test_node_2,
        #     self.test_way,
        #     self.test_relation,
        # )

    def test_plugin_viz_folium_display_kwargs(self):
        carto_viz = VizFolium()
        carto_viz.display(
            test_node_1=self.test_node_1,
            test_node_2=self.test_node_2,
            test_way=self.test_way,
            test_relation=self.test_relation,
        )

    def test_plugin_viz_folium_display_added(self):
        carto_viz = VizFolium()
        carto_viz.add(self.test_node_1)
        carto_viz.add(self.test_node_2)
        carto_viz.add(self.test_way)
        carto_viz.add(self.test_relation)
        carto_viz.display()

    def test_plugin_viz_folium_display_object(self):
        carto_viz = VizFolium()
        carto_viz.display(world=self.test_map)


if __name__ == "__main__":
    unittest.main()
