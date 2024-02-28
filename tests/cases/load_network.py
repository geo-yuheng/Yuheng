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
        self.map = yuheng.Waifu()
        FILENAME = "element_ogf_haresora_kinen.osm"
        data_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "..",
            "assets",
            "osm",
            FILENAME,
        )
        self.map.read(mode="file", file_path=data_path)

    def test_load_network_single_element(self):
        m_local = self.map
        m_network = yuheng.Waifu()
        # m_network.read(mode="n")
        m_network.read_network(
            target="element",
            source="api",
            endpoint="ogf",
            type="way",
            allow_cache=False,
            element_id="w28814809v1",
            version="2",
        )

        m_network.meow()
        assert len(m_local.way_dict) == 1
        assert len(m_network.way_dict) == 1
        for id in m_network.way_dict:
            assert m_network.way_dict[id].id == 28814809
        assert (
            m_local.way_dict[28814809].tags
            == m_network.way_dict[28814809].tags
        )
        assert (
            m_local.way_dict[28814809].changeset
            == m_network.way_dict[28814809].changeset
        )
        assert (
            m_local.way_dict[28814809].timestamp
            == m_network.way_dict[28814809].timestamp
        )


if __name__ == "__main__":
    unittest.main()
