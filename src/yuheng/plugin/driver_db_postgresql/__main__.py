import json
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

import psycopg
import pyproj
import shapely
from psycopg.types import TypeInfo
from psycopg.types.shapely import register_shapely

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Carto
from yuheng.basic import get_yuheng_path, logger
from yuheng.component import Node, Way

database_profile = json.load(
    open(
        os.path.join(
            get_yuheng_path(), "db_profiles", "postgresql.db_profiles.yuheng"
        ),
        "r",
        encoding="utf-8",
    )
)


def check_profile(database_profile: dict) -> None:
    if "_WARNING" in database_profile:
        logger.warning("This profile is invalid!")


PROJ_TRANSFORMER = pyproj.Transformer.from_crs("epsg:3857", "epsg:4326")


def check():
    # migration if needed
    #
    pass


def prune_tag(prune_list: List[str], target_dict: Dict[str, Any]):
    return {
        key: target_dict.get(key)
        for key in target_dict
        if key not in prune_list
    }


def geoproj(x: float, y: float) -> Tuple[float, float]:
    """
    return Tuple[lon:float, lat:float]
    """
    # don't use this old api
    # return pyproj.transform(
    #     pyproj.Proj(init="epsg:3857"), pyproj.Proj(init="epsg:4326"), x, y
    # )
    return PROJ_TRANSFORMER.transform(x, y)


def get_column(
    cursor: psycopg.Cursor, table_name: str, schema: str
) -> List[str]:
    column_list = []
    sql_column = (
        f"SELECT column_name "
        + f"FROM information_schema.columns "
        + f"WHERE table_name = '{table_name}' AND table_schema = '{schema}'"
        + f"ORDER BY ordinal_position;"
    )
    cursor.execute(sql_column)
    for record in cursor:
        column_list.append(record[0])
    # logger.debug(column_list)
    return column_list


def get_data(
    connection_dbname="postgres",
    connection_user="postgres",
    connection_password="12345678",
    connection_host="localhost",
    connection_port="5432",
    query_mode="full",
    query_type=["line"],
    pg_schema="public",
    pg_pre_fix="planet_osm",
) -> Optional[Carto]:
    """
    # full-全量查询
    # batch-批量查询
    # single-单条查询
    """
    config = {
        "dbname": connection_dbname,
        "user": connection_user,
        "password": connection_password,
        "host": connection_host,
        "port": connection_port,
    }
    result = []
    columns = []
    with psycopg.connect(
        " ".join([item + "=" + config.get(item) for item in config])
    ) as connection:
        info = TypeInfo.fetch(connection, "geometry")
        register_shapely(info, connection)
        # 不确定 ST_AsText 和 ST_AsGeoJSON 是否可用，依照 https://www.psycopg.org/psycopg3/docs/basic/pgtypes.html#geometry-adaptation-using-shapely 为准。
        # Shapely.LineString https://shapely.readthedocs.io/en/stable/reference/shapely.LineString.html
        # Shapely.Point https://shapely.readthedocs.io/en/stable/reference/shapely.Point.html
        with connection.cursor() as cursor:
            if query_mode == "full":
                if len(query_type) == 1 and (
                    "line" in query_type or "point" in query_type
                ):
                    # column
                    column = get_column(
                        cursor=cursor,
                        table_name=pg_pre_fix + "_" + query_type[0],
                        schema=pg_schema,
                    )
                    columns.append(column)
                    # logger.debug(columns)
                    # table
                    sql_table = f"SELECT * FROM {pg_schema}.{pg_pre_fix}_{query_type[0]}"
                    cursor.execute(sql_table)
                    for record in cursor:
                        result.append((query_type[0], record))

                elif (
                    len(query_type) == 2
                    and "line" in query_type
                    and "point" in query_type
                ):
                    # column
                    column_a = get_column(
                        cursor=cursor,
                        table_name=pg_pre_fix + "_" + query_type[0],
                        schema=pg_schema,
                    )
                    columns.append(column_a)
                    column_b = get_column(
                        cursor=cursor,
                        table_name=pg_pre_fix + "_" + query_type[1],
                        schema=pg_schema,
                    )
                    columns.append(column_b)
                    # table
                    sql_table_a = f"SELECT * FROM {pg_schema}.{pg_pre_fix}_{query_type[0]}"
                    cursor.execute(sql_table_a)
                    for record in cursor:
                        result.append((query_type[0], record))
                    sql_table_b = f"SELECT * FROM {pg_schema}.{pg_pre_fix}_{query_type[1]}"
                    cursor.execute(sql_table_b)
                    for record in cursor:
                        result.append((query_type[1], record))
                else:
                    logger.error("要么是想查询line/point以外的表，要么是输入了太多项类型；故目前无法支持。")
                    return None
    logger.info("len(result)", "=", len(result))

    control_count = 0  # debug
    control_count_way = 0
    control_count_node = 0
    # transform and insert
    node_remap_count = -1
    way_remap_count = -1
    node_list = []
    way_list = []
    world = Carto()
    for element in result:
        element_type = element[0]
        element_data = list(element[1])
        # logger.debug(element_data)

        if element_type == "line" or element_type == "way":
            control_count_way += 1
        elif element_type == "point" or element_type == "node":
            control_count_node += 1
        else:
            control_count += 1

        column = columns[0]
        tag_dict = dict(zip(column, element_data))
        osm_id = tag_dict.get("osm_id")
        geom = tag_dict.get("way")
        tag_dict = prune_tag(
            prune_list=["osm_id", "z_order", "way_area", "way"],
            target_dict=tag_dict,
        )  # 第一项和后三项，不是tag内容而是osm2pgsql加的
        # logger.debug(tag_dict)
        # logger.debug(geom)
        if isinstance(geom, shapely.geometry.Point):
            pos = geoproj(geom.x, geom.y)
            this_node = Node(
                attrib={
                    "id": node_remap_count if osm_id <= 0 else osm_id,
                    "visible": True,
                    "version": 1,
                    "changeset": 1,
                    "lat": pos[1],
                    "lon": pos[0],
                },
                tag_dict=tag_dict,
            )
            node_list.append(this_node)
            node_remap_count -= 1
            if control_count_node >= 100:
                break
        if isinstance(geom, shapely.geometry.LineString):
            import time

            start_time = time.time()
            point_list = [
                geoproj(x=i[0], y=i[1])
                for i in list(zip(list(geom.xy[0]), list(geom.xy[1])))
            ]
            temp_node_list: List[int] = []
            for point in point_list:
                temp_node = Node(
                    attrib={
                        "id": node_remap_count,
                        "visible": True,
                        "version": 1,
                        "changeset": 1,
                        "lat": point[1],
                        "lon": point[0],
                    },
                    tag_dict={"type": "virtual_node"},
                )
                temp_node_list.append(node_remap_count)
                node_list.append(temp_node)
                node_remap_count -= 1
            temp_way = Way(
                attrib={
                    "id": way_remap_count if osm_id <= 0 else osm_id,
                    "visible": True,
                    "version": 1,
                    "changeset": 1,
                },
                tag_dict=tag_dict,
                nd_list=temp_node_list,
            )
            way_list.append(temp_way)
            way_remap_count -= 1

            end_time = time.time()
            duration = end_time - start_time
            logger.info(f"time: {duration}s")

            if control_count_way >= 100:
                break

    world.insert_to_dict(world.node_dict, node_list)
    world.insert_to_dict(world.way_dict, way_list)
    return world

def read() -> Carto:
    pass

def write() -> None:
    logger.error("暂无法向PGSQL数据来源写入数据")


def main():
    logger.error("本数据驱动无法独立于Yuheng单独使用")


if __name__ == "__main__":
    main()
