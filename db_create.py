import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="12qwasXZ"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE test_db_3")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())
