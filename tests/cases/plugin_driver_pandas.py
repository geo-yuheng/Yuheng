import unittest
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

from yuheng.plugin.driver_pandas.__main__ import transform
from yuheng import Carto
from yuheng.component import Node, Way, Relation
import pandas


class TestTransformFunction(unittest.TestCase):
    def setUp(self):
        test_filename = "extract_osmwebsite_bbox_buctcampus.osm"
        # test_filename = "element_ogf_haresora_kinen.osm"
        self.carto = Carto()
        self.carto.read(
            mode="file",
            file_path=os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "..",
                "assets",
                "osm",
                test_filename,
            ),
        )

    def test_transform(self):
        # 执行转换函数
        result_df = transform(self.carto)
        result_df.to_csv(
            "filenamekkkkkkqqqqqq.csv", encoding="utf-8-sig", index=False
        )
        # 验证结果是一个DataFrame
        self.assertTrue(isinstance(result_df, pandas.DataFrame))

        self.assertEqual(
            len(result_df),
            (
                len(self.carto.node_dict)
                + len(self.carto.way_dict)
                + len(self.carto.relation_dict)
            ),
        )


if __name__ == "__main__":
    unittest.main()
