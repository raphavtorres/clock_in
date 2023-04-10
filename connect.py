import mysql.connector


db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='clock_in'
)

cursor = db.cursor()
