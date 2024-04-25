import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

import pandas
from yuheng import Carto
from yuheng.component import Node, Relation, Way
from yuheng.plugin.driver_pandas.__main__ import transform


class TestTransformFunction(unittest.TestCase):
    def setUp(self):
        self.test_filename = "extract_osmwebsite_bbox_buctcampus.osm"
        # self.test_filename = "element_ogf_haresora_kinen.osm"
        self.carto = Carto()
        self.carto.read(
            mode="file",
            file_path=os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "..",
                "assets",
                "osm",
                self.test_filename,
            ),
        )

    def test_transform(self):
        result_df = transform(self.carto)

        self.assertTrue(isinstance(result_df, pandas.DataFrame))
        self.assertEqual(
            len(result_df),
            (
                len(self.carto.node_dict)
                + len(self.carto.way_dict)
                + len(self.carto.relation_dict)
            ),
        )

        # result_df.to_csv(
        #     self.test_filename.replace(".osm", ".csv"),
        #     encoding="utf-8",
        #     index=False,
        # )


if __name__ == "__main__":
    unittest.main()
