# 构造1个relation，2个way，几个node，看看way_dict/node_dict序列化后是否和预期一致（先做序列化）
# （以及允许人工new对象）

import unittest
# from os.path import dirname, join, realpath # 可能后期会导出存为.osm文件

from src import keqing
from src.keqing.type.element import Node, Way, Relation


class TestTypeConstructor(unittest.TestCase):
    def setUp(self) -> None:
        self.map = keqing.Waifu()

    def test_construct_elements(self):
        map=self.map
        node_1=Node(attrib={"id":"114514","version":"1","changeset":"1"}, tag_dict={"building":"yes","colour":"red"})

        assert len(map.way_dict) == 1


if __name__ == "__main__":
    unittest.main()
