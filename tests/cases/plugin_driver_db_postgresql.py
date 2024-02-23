import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)


class TestPluginDriverDbPostgresql(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_plugin_driver_db_postgresql_full(self):
        # NOTE: conduct this part of postgresql need you deploy a server.

        from yuheng.plugin.driver_db_postgresql.__main__ import get_data

        result = get_data(
            connection_dbname="osm2pgsql",
            connection_user="postgres",
            connection_password="12345678",
            connection_host="localhost",
            connection_port="5432",
            query_mode="full",
            query_type=["line"],
        )
        print(len(result))
        # assert len(result) == 0


if __name__ == "__main__":
    unittest.main()
