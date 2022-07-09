# 每个对象访问一边完整的内容或者指定内容看是否出错

import unittest
from os.path import dirname, join, realpath

from kqs.waifu import Waifu


class TestLoad(unittest.TestCase):
    def setUp(self) -> None:
        self.map = Waifu()
        FILENAME = "JOSM_export.osm"
        data_path = join(dirname(realpath(__file__)), "export", FILENAME)
        self.map.read_file(data_path)

    def test_iterator(self):
        m = self.map
        test_node_dict = m.node_dict
        for id in test_node_dict:
            print(id, test_node_dict[id])
            for key in test_node_dict[id].tags:
                print(key, "=", test_node_dict[id].tags[key])


if __name__ == "__main__":
    unittest.main()
