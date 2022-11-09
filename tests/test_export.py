# 尝试直接另存，完全新建对象另存，在已有基础增删改后另存

import unittest
from os.path import dirname, join, realpath
import xml

from kqs.waifu import Waifu


class TestExport(unittest.TestCase):
    def setUp(self) -> None:
        self.map = Waifu()
        FILENAME = "standard_load.osm"
        data_path = join(dirname(realpath(__file__)), "export", FILENAME)
        self.map.read(mode="file", file_path=data_path)

    def test_self_save(self):
        m = self.map
        m.write(mode="file",file_path="self_save_dist.osm")

        # src=xml.parsers
        # dst=xml.parsers

    def test_iterator_way(self):
        pass

if __name__ == "__main__":
    unittest.main()
