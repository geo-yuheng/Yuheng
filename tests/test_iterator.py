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

    def test_iterator_node(self):
        m = self.map
        test_node_dict = m.node_dict
        for id in test_node_dict:
            print(id, test_node_dict[id])
            for key in test_node_dict[id].tags:
                print(key, "=", test_node_dict[id].tags[key])

    def test_iterator_way(self):
        pass

    def test_iterator_relation(self):
        pass

    # 下面的四个未来也可能算作select部分的测试用例，也可能依然归类为迭代用例

    def test_iterator_node_by_way(self):
        # 当点为路径的成员时，通过路径访问成员点
        pass

    def test_iterator_node_by_relation(self):
        # 当点为关系的成员时，通过关系访问成员点
        pass

    def test_iterator_way_by_relation(self):
        # 当路径为关系的成员时，通过关系访问成员路径
        pass

    def test_iterator_relation_by_relation(self):
        # 当关系为关系的成员时，通过关系访问成员关系
        # 多边形问题暂不讨论几何是否正确
        pass

if __name__ == "__main__":
    unittest.main()
