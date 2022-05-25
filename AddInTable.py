import pymysql.cursors

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="data",
    cursorclass=pymysql.cursors.DictCursor
)

with conn:
    with conn.cursor() as cursor:
        sql = "INSERT INTO data.users (username, email, password) VALUES ('Glebka', 'glebka@mail.ru', 'hard')"
        cursor.execute(sql)
    conn.commit()

    with conn.cursor() as cursor:
        sql = "SELECT id, username, email, password FROM data.users WHERE id=1"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)



