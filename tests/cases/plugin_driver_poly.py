# 每个对象访问一边完整的内容或者指定内容看是否出错

import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

from yuheng.basic import logger


class TestPluginDriverPoly(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_plugin_driver_poly_import(self):
        from yuheng.plugin.driver_poly.__main__ import main

        ans = main(
            poly_file_path=os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "..",
                "assets",
                "poly",
                "Izaland-polyfile-20231213-laoshubabytest.poly",
            )
        )
        logger.info(ans)

    def test_plugin_driver_poly_cli(self):
        args = (
            "--poly_file_path "
            + os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "..",
                "assets",
                "poly",
                "Izaland-polyfile-20231213-laoshubabytest.poly",
            )
            + ' --schema dict --order "lat-lon" --output-format yuheng'
        )
        os.system(
            "python"
            + " "
            + os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "..",
                "..",
                "src",
                "yuheng",
                "plugin",
                "driver_poly",
                "__main__.py",
            )
            + " "
            + args
        )


if __name__ == "__main__":
    unittest.main()
