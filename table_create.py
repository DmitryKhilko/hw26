import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="12qwasXZ",
    database="test_db_3"
)

cursor = db.cursor()
cursor.execute(
    "CREATE TABLE orders (ord_no INT, purch_amt DECIMAL(10,1), ord_date DATE, "
    "customer_id INT, salesman_id INT)"
)

cursor.execute("SHOW TABLES")
print(cursor.fetchall())
