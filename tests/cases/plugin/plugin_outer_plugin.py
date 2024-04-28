import os
import sys
import unittest

from yuheng_plugin.yuheng_admininspect.__init__ import main

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..", "src")
sys.path.append(src_dir)

from yuheng import Carto


class TestOuterPlugin(unittest.TestCase):
    def setUp(self):
        self.world = Carto()

    def test(self):
        main(carto=self.world)


if __name__ == "__main__":
    unittest.main()
