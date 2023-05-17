import mysql.connector as mysql

# Напечатайте номер заказа, дату заказа и количество для каждого заказа, который продал продавец под номером: 5002
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="12qwasXZ",
    database="test_db_3"
)

cursor = db.cursor()
try:
    query = "SELECT ord_no, ord_date, purch_amt FROM orders WHERE salesman_id = 5002"
    cursor.execute(query)
    result = cursor.fetchall()
    print("")
    print("ord_no    ord_date    purch_amt")
    for row in result:
        print("%s    %s    %s" % (row[0], row[1], row[2]))
except:
    db.rollback()
db.close()

# Напечатайте уникальные id продавца(salesman_id). Используйте distinct
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="12qwasXZ",
    database="test_db_3"
)

cursor = db.cursor()
try:
    query = "SELECT DISTINCT salesman_id FROM orders ORDER BY salesman_id"
    cursor.execute(query)
    result = cursor.fetchall()
    print("")
    print("salesman_id")
    for row in result:
        print("%s" % (row[0]))
except:
    db.rollback()
db.close()

# Напечатайте по порядку данные о дате заказа, id продавца, номер заказа, количество
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="12qwasXZ",
    database="test_db_3"
)

cursor = db.cursor()
try:
    query = "SELECT ord_date, salesman_id, ord_no, purch_amt FROM orders ORDER BY ord_date"
    cursor.execute(query)
    result = cursor.fetchall()
    print("")
    print("ord_date    salesman_id    ord_no    purch_amt")
    for row in result:
        print("%s    %s    %s    %s" % (row[0], row[1], row[2], row[3]))
except:
    db.rollback()

db.close()

# Напечатайте заказы между 70001 и 70007(используйте between, and)
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="12qwasXZ",
    database="test_db_3"
)

cursor = db.cursor()
try:
    query = "SELECT ord_no FROM orders WHERE ord_no BETWEEN 70001  AND 70007 ORDER BY ord_no"
    cursor.execute(query)
    result = cursor.fetchall()
    print("")
    print("salesman_id")
    for row in result:
        print("%s" % (row[0]))
except:
    db.rollback()
db.close()
