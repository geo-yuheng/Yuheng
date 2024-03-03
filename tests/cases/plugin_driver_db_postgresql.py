import json
import os
import sys
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "../../src")
sys.path.append(src_dir)

from yuheng import Carto
from yuheng.basic import get_yuheng_path, logger


class TestPluginDriverDbPostgresql(unittest.TestCase):
    def setUp(self) -> None:
        # NOTE: conduct this part of postgresql need you deploy a server.
        self.database_profile = json.load(
            open(
                os.path.join(
                    get_yuheng_path(),
                    "db_profiles",
                    "postgresql.db_profiles.yuheng",
                ),
                "r",
                encoding="utf-8",
            )
        )

    def test_plugin_driver_db_postgresql_full_type_node(self):
        import time

        from yuheng.plugin.driver_db_postgresql.__main__ import get_data

        start_time = time.time()
        world = get_data(
            connection_dbname=database_profile["dbname"],
            connection_user=database_profile["dbname"],
            connection_password=database_profile["password"],
            connection_host=database_profile["host"],
            connection_port=database_profile["port"],
            query_mode="full",
            query_type=["point"],
        )
        logger.info(f"len(world.node_dict): {len(world.node_dict)}")
        logger.info(f"len(world.way_dict): {len(world.way_dict)}")
        end_time = time.time()
        duration = end_time - start_time
        logger.info(f"total time: {duration}s")
        assert isinstance(world, Carto)

    def test_plugin_driver_db_postgresql_full_type_way(self):
        import time

        from yuheng.plugin.driver_db_postgresql.__main__ import get_data

        start_time = time.time()
        world = get_data(
            connection_dbname=database_profile["dbname"],
            connection_user=database_profile["user"],
            connection_password=database_profile["password"],
            connection_host=database_profile["host"],
            connection_port=database_profile["port"],
            query_mode="full",
            query_type=["line"],
        )
        logger.info(f"len(carto.node_dict): {len(carto.node_dict)}")
        logger.info(f"len(carto.way_dict): {len(carto.way_dict)}")
        end_time = time.time()
        duration = end_time - start_time
        logger.info(f"total time: {duration}s")
        assert isinstance(world, Carto)

    def test_plugin_driver_db_postgresql_full_type_multi(self):
        import time

        from yuheng.plugin.driver_db_postgresql.__main__ import get_data

        start_time = time.time()
        carto = get_data(
            connection_dbname=database_profile["dbname"],
            connection_user=database_profile["user"],
            connection_password=database_profile["password"],
            connection_host=database_profile["host"],
            connection_port=database_profile["port"],
            query_mode="full",
            query_type=["line", "point"],
        )
        logger.info(f"len(carto.node_dict): {len(carto.node_dict)}")
        logger.info(f"len(carto.way_dict): {len(carto.way_dict)}")
        end_time = time.time()
        duration = end_time - start_time
        logger.info(f"total time: {duration}s")

    def test_plugin_driver_db_postgresql_full_invalidtype(self):
        from yuheng.plugin.driver_db_postgresql.__main__ import get_data

        result = get_data(
            connection_dbname=database_profile["dbname"],
            connection_user=database_profile["user"],
            connection_password=database_profile["password"],
            connection_host=database_profile["host"],
            connection_port=database_profile["port"],
            query_mode="full",
            query_type=["line", "point", "polygon"],
        )
        assert result == None


if __name__ == "__main__":
    unittest.main()
