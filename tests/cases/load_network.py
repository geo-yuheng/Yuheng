# 每个对象访问一边完整的内容或者指定内容看是否出错

import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

import yuheng


class TestLoadNetwork(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_load_network_single_element(self):
        FILENAME = "element_ogf_haresora_kinen.osm"
        data_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "..",
            "assets",
            "osm",
            FILENAME,
        )
        world_local = yuheng.Carto()
        world_local.read(mode="file", file_path=data_path)
        world_network = yuheng.Carto()
        # world_network.read(mode="n")
        world_network.read_network(
            target="element",
            source="api",
            endpoint="ogf",
            type="way",
            allow_cache=False,
            element_id="w28814809v1",
            version="2",
        )

        world_network.meow()
        assert len(world_local.way_dict) == 1
        assert len(world_network.way_dict) == 1
        for id in world_network.way_dict:
            assert world_network.way_dict[id].id == 28814809
        assert (
            world_local.way_dict[28814809].tags
            == world_network.way_dict[28814809].tags
        )
        assert (
            world_local.way_dict[28814809].changeset
            == world_network.way_dict[28814809].changeset
        )
        assert (
            world_local.way_dict[28814809].timestamp
            == world_network.way_dict[28814809].timestamp
        )

    def test_load_network_area(self):
        world_network = yuheng.Carto()
        world_network.read_network(
            target="area",
            source="api",
            endpoint="ogf",
            allow_cache=False,
            S=39.9671,
            W=116.4110,
            N=39.9726,
            E=116.4191,
        )


if __name__ == "__main__":
    unittest.main()
