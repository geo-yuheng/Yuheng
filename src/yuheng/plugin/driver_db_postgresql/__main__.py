from typing import Optional, List

import psycopg
import shapely
from psycopg.types import TypeInfo

from psycopg.types.shapely import register_shapely


import os
import sys
from pyproj import Proj, transform

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Waifu


def check():
    # migration if needed
    #
    pass


def geoproj(x: float, y: float):
    lon, lat = transform(Proj(init="epsg:3857"), Proj(init="epsg:4326"), x, y)
    print(f"Longitude: {lon}, Latitude: {lat}")
    return transform(Proj(init="epsg:3857"), Proj(init="epsg:4326"), x, y)


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
    # print(column_list) # debug
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
) -> Optional[Waifu]:
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
                    # print(columns) # debug
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
                    print("要么你就想查询line/point以外的表，要么你就输了太多项。目前无法支持。")
                    return None
    print("len(result)", "=", len(result))  # debug
    count = 0
    for element in result:
        count += 1
        element_type = element[0]
        element_data = list(element[1])
        # print(element_data)  # debug
        if len(query_type) == 1:
            column = columns[0]
            attrib = dict(zip(column, element_data))
            geom = attrib["way"]
            # print(attrib)  # debug
            # print(geom) # debug
            if isinstance(geom, shapely.geometry.Point):
                print("yoo")
                print(geom.x, geom.y)
                print(geoproj(geom.x, geom.y))
                if count >= 500:
                    exit(0)

    return result


def main():
    print("本数据驱动无法独立于Yuheng单独使用")


if __name__ == "__main__":
    get_data()
