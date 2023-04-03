import mysql.connector


db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='clock_point'
)

cursor = db.cursor()
