import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)


class TestPluginDriverPgsql(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_plugin_driver_pgsql_full(self):
        from yuheng.plugin.driver_pgsql.__main__ import get_data

        get_data(mode="full", dbname="osm2pgsql")
        pass


if __name__ == "__main__":
    unittest.main()
