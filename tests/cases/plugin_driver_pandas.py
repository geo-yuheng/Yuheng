import unittest
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

from yuheng.plugin.driver_pandas.__main__ import transform
from yuheng import Carto
from yuheng.component import Node, Way, Relation


class TestTransformFunction(unittest.TestCase):
    def setUp(self):
        # 创建一个Carto对象和一些元素用于测试
        self.carto = Carto()
        self.carto.read(
            mode="file",
            file_path=os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "..",
                "assets",
                "osm",
                "extract_osmwebsite_bbox_buctcampus.osm",
            ),
        )

    def test_transform(self):
        # 执行转换函数
        result_df = transform(self.carto)

        # 验证结果是一个DataFrame
        self.assertTrue(isinstance(result_df, pandas.DataFrame))

        # 验证DataFrame的行数是否正确（3个元素 * 2个tags（node）+ 1个元素（way）+ 1个元素（relation）= 8行）
        self.assertEqual(len(result_df), 8)

        # 验证DataFrame包含正确的标签数据
        expected_tags = {
            "node1": {"type": "node", "name": "Node1"},
            "node2": {"type": "node", "name": "Node2"},
            "way1": {"type": "way", "name": "Way1"},
            "relation1": {"type": "relation", "name": "Relation1"},
        }
        for element_id, expected_tags_row in expected_tags.items():
            self.assertTrue((result_df["id"] == element_id).any())
            for tag, value in expected_tags_row.items():
                self.assertTrue((result_df["tag"] == tag).any())
                self.assertTrue((result_df["value"] == value).any())


if __name__ == "__main__":
    unittest.main()
