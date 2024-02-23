# 全量查询
# 批量查询
# 单条查询

# 是否需要初始化表格，migration

import psycopg


def get_data(mode=""):
    with psycopg.connect(
        "dbname=postgres"
        + " "
        + "user=postgres"
        + " "
        + "password=12345678"
        + " "
        + "host=localhost"
        + " "
        + "port=5432"
    ) as conn:
        with conn.cursor() as cur:
            #         cur.execute(
            #             """
            # -- Table: public.testtable
            #
            # -- DROP TABLE IF EXISTS public.testtable;
            #
            # CREATE TABLE IF NOT EXISTS public.testtable
            # (
            #     key "integer",
            #     value "integer"
            # )
            #
            # TABLESPACE pg_default;
            #
            # ALTER TABLE IF EXISTS public.testtable
            #     OWNER to postgres;
            #             """
            #         )
            cur.execute(
                "INSERT INTO testtable (key, value) VALUES ("
                + str(i * 100 + j * 2)
                + ","
                + str(j)
                + ")"
            )

            cur.execute("SELECT * FROM testtable")

            for record in cur:
                print(record)

            conn.commit()
