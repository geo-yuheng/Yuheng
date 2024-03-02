import json
import os
import sys

import pymysql

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Carto
from yuheng.basic import get_yuheng_path

database_profile = json.load(
    open(
        os.path.join(
            get_yuheng_path(), "db_profiles", "mysql.db_profiles.yuheng"
        ),
        "r",
        encoding="utf-8",
    )
)


def check_profile(database_profile: dict) -> None:
    if "_WARNING" in database_profile:
        print("WARNING: this profile is invalid!")


connection = pymysql.connect(
    host=database_profile["host"],
    port=database_profile["port"],
    user=database_profile["user"],
    password=database_profile["password"],
    database=database_profile["database"],
    charset=database_profile["charset"],
    # required if using mysql compatible tidb.
    ssl_verify_cert=database_profile["ssl_verify_cert"],
    ssl_verify_identity=database_profile["ssl_verify_identity"],
    ssl_key=database_profile["ssl_key"],
)


with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "SELECT * FROM osm_nodes;"
        # table definition can be seen at https://github.com/iandees/osm2mysql/blob/master/osmarchive.sql
        # osm_changesets
        # osm_changeset_tags
        # osm_nodes
        # osm_node_tags
        # osm_relations
        # osm_relation_members
        # osm_relation_tags
        # osm_ways
        # osm_way_nodes
        # osm_way_tags
        cursor.execute(sql)
        connection.commit()
