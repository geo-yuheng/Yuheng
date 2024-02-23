import psycopg

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
    with psycopg.connect(
        " ".join([item + "=" + config.get(item) for item in config])
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM public.planet_osm_line")

            for record in cursor:
                print(record)

            connection.commit()


def main():
    print("本数据驱动无法独立于Yuheng单独使用")


if __name__ == "__main__":
    main()
