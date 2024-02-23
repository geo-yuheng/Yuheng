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
    connection_dbname="postgres",
    connection_user="postgres",
    connection_password="12345678",
    connection_host="localhost",
    connection_port="5432",
    query_mode="full",
    query_type=["line"],
    pg_schema="public",
    pg_pre_fix="planet_osm",
) -> Waifu:
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
    with psycopg.connect(
        " ".join([item + "=" + config.get(item) for item in config])
    ) as connection:
        with connection.cursor() as cursor:
            # config flag
            flag_query_directly = False
            # generate sql
            if query_mode == "full":
                if len(query_type) == 1:
                    sql = f"SELECT * FROM {pg_schema}.{pg_pre_fix}_{query_type[0]}"
                elif (
                    len(query_type) == 2
                    and "line" in query_type
                    and "point" in query_type
                ):
                    if flag_query_directly:
                        sql = f"SELECT * FROM join({pg_schema}.{pg_pre_fix}_line,{pg_schema}.{pg_pre_fix}_point)"
            # conduct and collect
            cursor.execute(sql)
            for record in cursor:
                result.append(record)
            connection.commit()
    print(len(result))
    return result


def main():
    print("本数据驱动无法独立于Yuheng单独使用")


if __name__ == "__main__":
    get_data()
