#! /usr/bin/env
import sqlite3
connection =sqlite3.connect("books.db")
cursor = connection.cursor()
cursor.execute('''ALTER TABLE library ADD Date_of_creation year ''')
for row in cursor.execute('''SELECT * FROM library'''):
    print(row)
connection.rollback()
for row in cursor.execute('''SELECT * FROM library'''):
    print(row)
connection.close()
