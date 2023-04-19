# import sqlite3
import mysql.connector

# db = sqlite3.connect('../clock_in.db')

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='clock_in'
)

cursor = db.cursor()
