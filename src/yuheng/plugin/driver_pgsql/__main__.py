import psycopg
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(current_dir, "..", "..", "..")
sys.path.append(src_dir)
from yuheng import Waifu


def check():
    # migration if needed
    #
    pass


def get_data(
    mode="full",
    # dbname="postgres",
    dbname="osm2pgsql",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432",
    query_type="line",
    pg_schema="public",
    pg_pre_fix="planet_osm",
) -> Waifu:
    """
    # full-全量查询
    # batch-批量查询
    # single-单条查询
    """
    config = {
        "dbname": dbname,
        "user": user,
        "password": password,
        "host": host,
        "port": port,
    }
    result = []
    with psycopg.connect(
        " ".join([item + "=" + config.get(item) for item in config])
    ) as connection:
        with connection.cursor() as cursor:
            if mode == "full":
                if query_type == "line":
                    sql = f"SELECT * FROM {pg_schema}.{pg_pre_fix}_line"
            cursor.execute(sql)
            for record in cursor:
                result.append(record)
            connection.commit()
    # print(result)
    print(len(result))
    return result


def main():
    print("本数据驱动无法独立于Yuheng单独使用")


if __name__ == "__main__":
    get_data()
