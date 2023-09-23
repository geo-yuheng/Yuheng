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
        map = self.map
        node_1 = Node(
            attrib={
                "id": "1",
                "visible": "true",
                "version": "1",
                "changeset": "1",
                "timestamp": "2012-12-21T11:33:55Z",
                "user": "810",
                "uid": "1919",
                "lat": "1.0",
                "lon": "5.0",
            },
            tag_dict={},
        )
        node_2 = Node(
            attrib={
                "id": "2",
                "visible": "true",
                "version": "1",
                "changeset": "1",
                "timestamp": "2012-12-21T11:33:55Z",
                "user": "810",
                "uid": "1919",
                "lat": "6.0",
                "lon": "5.0",
            },
            tag_dict={},
        )
        node_3 = Node(
            attrib={
                "id": "3",
                "visible": "true",
                "version": "1",
                "changeset": "2",
                "timestamp": "2012-12-22T11:33:55Z",
                "user": "810",
                "uid": "1919",
                "lat": "3.5",
                "lon": "1.0",
            },
            tag_dict={},
        )
        node_4 = Node(
            attrib={
                "id": "4",
                "visible": "false",
                "version": "1",
                "changeset": "2",
                "timestamp": "2012-12-22T11:33:55Z",
                "user": "810",
                "uid": "1919",
                "lat": "6.0",
                "lon": "5.0",
            },
            tag_dict={},
        )
        node_5 = Node(
            attrib={
                "id": "5",
                "visible": "true",
                "version": "1",
                "changeset": "2",
                "timestamp": "2012-12-22T11:33:55Z",
                "user": "810",
                "uid": "1919",
                "lat": "6.0",
                "lon": "5.0",
            },
            tag_dict={},
        )
        node_6 = Node(
            attrib={
                "id": "6",
                "visible": "true",
                "version": "1",
                "changeset": "2",
                "timestamp": "2012-12-22T11:33:55Z",
                "user": "810",
                "uid": "1919",
                "lat": "6.0",
                "lon": "5.0",
            },
            tag_dict={},
        )
        node_7 = Node(
            attrib={
                "id": "7",
                "visible": "true",
                "version": "1",
                "changeset": "3",
                "timestamp": "2012-12-23T11:33:55Z",
                "user": "810",
                "uid": "1919",
                "lat": "6.0",
                "lon": "5.0",
            },
            tag_dict={},
        )
        way_1 = Way(
            attrib={
                "id": "114",
                "visible": "true",
                "version": "1",
                "changeset": "3",
                "timestamp": "2012-12-23T11:33:55Z",
                "user": "810",
                "uid": "1919",
            },
            tag_dict={},
            nd_list=["1", "2", "3"],
        )
        way_2 = Way(
            attrib={
                "id": "514",
                "visible": "true",
                "version": "1",
                "changeset": "3",
                "timestamp": "2012-12-23T11:33:55Z",
                "user": "810",
                "uid": "1919",
            },
            tag_dict={},
            nd_list=["5", "6", "7"],
        )
        relation_1 = Relation(
            attrib={
                "id": "114514",
                "visible": "true",
                "version": "1",
                "changeset": "1",
                "timestamp": "2012-12-21T11:33:55Z",
                "user": "810",
                "uid": "1919",
            },
            tag_dict={
                "building": "yes",
                "colour": "red",
                "building:prefabricated": "cai-gang-ban",
            },
        )
        assert len(map.node_dict) == 7
        assert len(map.way_dict) == 2
        assert len(map.relation_dict) == 1


if __name__ == "__main__":
    unittest.main()
