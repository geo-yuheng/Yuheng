import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)


class TestImportNamespace(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_import_correct(self):
        import yuheng

        print(globals().get("__name__", ""))
        world = yuheng.Carto()
        del world

    def test_import_wrong(self):
        import yuheng as yh

        print(globals().get("__name__", ""))
        world = yh.Carto()
        del world


if __name__ == "__main__":
    unittest.main()
