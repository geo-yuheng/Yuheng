# 每个对象访问一边完整的内容或者指定内容看是否出错

import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

import yuheng


class TestIterator(unittest.TestCase):
    def setUp(self) -> None:
        self.world = yuheng.Waifu()
        FILENAME = "extract_josm_bbox_qingzhou.osm"
        data_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "..",
            "assets",
            "osm",
            FILENAME,
        )
        self.world.read(mode="file", file_path=data_path)

    def test_iterator_node(self):
        m = self.world
        test_node_dict = m.node_dict
        for id in test_node_dict:
            print(id)  # , test_node_dict[id])
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
