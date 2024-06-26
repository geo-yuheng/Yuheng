import os
import sys
import unittest

from folium import TileLayer

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

from yuheng import Carto
from yuheng.component import Member, Node, Relation, Way
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
        self.test_map.insert_to_dict(
            self.test_map.node_dict,
            [
                self.test_node_1,
                self.test_node_2,
            ],
        )
        self.test_map.insert_to_dict(
            self.test_map.way_dict,
            [self.test_way],
        )
        self.test_map.insert_to_dict(
            self.test_map.relation_dict,
            [self.test_relation],
        )

    def test_plugin_viz_folium_display_invalid_argument(self):
        """
        Test exit directly because occupy preserved arguments.
        """
        # rebellious developer
        carto_viz = VizFolium()
        carto_viz.display(
            default_zoom=self.test_map,  # should be int
            default_center_lat="beijing",  # should be float
            default_center_lon=int(6),  # should be float
        )

    def test_plugin_viz_folium_display_added(self):
        """
        Test load NWR object via add method.
        """
        carto_viz = VizFolium()
        carto_viz.add(self.test_node_1)
        carto_viz.add(self.test_node_2)
        carto_viz.add(self.test_way)
        carto_viz.add(self.test_relation)
        carto_viz.display()

    def test_plugin_viz_folium_display_kwargs(self):
        """
        Test load NWR object via argument enumerate.
        """
        carto_viz = VizFolium()
        carto_viz.display(
            test_node_1=self.test_node_1,
            test_node_2=self.test_node_2,
            test_way=self.test_way,
            test_relation=self.test_relation,
        )

    def test_plugin_viz_folium_display_object(self):
        """
        Test load Carto object via argument.
        """
        carto_viz = VizFolium()
        carto_viz.display(world=self.test_map)

    def test_plugin_viz_folium_complex(self):
        # can add default_tiles and default_attribution in future
        world = Carto()
        world.read(
            mode="file",
            file_path=os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "..",
                "assets",
                "osm",
                "extract_osmwebsite_bbox_buctcampus.osm",
            ),
        )
        world.meow()
        world.read_network(
            target="element",
            source="api",
            endpoint="ogf",
            type="way",
            allow_cache=False,
            element_id="w28814809v1",
            version="2",
        )
        world.meow()
        world.read_network(
            target="element",
            source="api",
            endpoint="ogf",
            type="node",
            allow_cache=False,
            element_id=["n299872168v1", "n299872169v1", "n299872170v1"],
            version="1",
        )
        world.meow()
        viz = VizFolium()
        viz.add(world)
        viz.display(
            default_center_lat=39.8571,
            default_center_lon=116.3974,
            default_zoom=9,
            colour_original=True,
            # OpenStreetMap
            # default_tiles=TileLayer(
            #     tiles="OpenStreetMap",
            #     attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
            # ),
            # # cartodb
            # default_tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
            # default_attribution=" ".join(
            #     [
            #         f'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
            #         f'&copy; <a href="https://carto.com/attributions">CARTO</a>',
            #     ]
            # ),
            # # ogf
            # default_tiles=TileLayer(
            #     tiles="https://tiles04.rent-a-planet.com/ogf-carto/{z}/{x}/{y}.png",
            #     attr='&copy; <a href="https://opengeofiction.net">OpenGeofiction</a> creators',
            #     opacity=0.5,
            # ),
            default_style_line_width=3,
            default_style_line_width_uncoloured=2,
            default_style_line_width_coloured=5,
        )
        viz.meow()


if __name__ == "__main__":
    unittest.main()
