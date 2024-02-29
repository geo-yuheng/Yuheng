import pymysql
import os
import json

database_profile_path = os.path.join(
    os.environ["USERPROFILE"], "database_profile_mysql.yuheng"
)
database_profile = json.load(open(database_profile_path, "r"))

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
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        for i in range(100):
            cursor.execute(sql, (f"webmaster-{i}@python.org", "very-secret"))
            connection.commit()
