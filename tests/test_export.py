# 尝试直接另存，完全新建对象另存，在已有基础增删改后另存

import unittest
import xml.sax
from os.path import dirname, join, realpath
from xml import sax
from xml.sax.handler import ContentHandler

from kqs.waifu import Waifu


class TestExport(unittest.TestCase):
    def setUp(self) -> None:
        self.map = Waifu()
        self.FILENAME_TARGET = "standard_load.osm"
        self.FILENAME_OUTPUT = "self_save_dist.osm"
        self.path_target = join(
            dirname(realpath(__file__)), "export", self.FILENAME_TARGET
        )
        self.path_output = join(
            dirname(realpath(__file__)), "export", self.FILENAME_OUTPUT
        )
        self.map.read(mode="file", file_path=self.path_target)

    def test_self_save(self):
        m = self.map
        m.write(mode="file", file_path=self.path_output)

        class MapElementHandler(xml.sax.ContentHandler):
            def __init__(self, file_name: str):
                pass

        sax.parse(
            source=self.path_output,
            handler=MapElementHandler(file_name=self.path_target),
        )
        # output=xml.parsers

    def test_insert_node_save(self):
        # 在标准读取的基础上插入点后保存
        pass

    def test_create_node_save(self):
        # 在空文件创建单点后保存
        pass

    def test_delete_way_save(self):
        # 在标准读取中删除路径后保存
        pass


if __name__ == "__main__":
    unittest.main()
