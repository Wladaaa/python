#! /usr/bin/env
import sqlite3
connection =sqlite3.connect("books.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS library (id integer NOT NULL, title text , length integer, PRIMARY KEY (id))''')
cursor.execute('''INSERT INTO library(title,length) VALUES ('ks1',300) ''')
cursor.execute('''INSERT INTO library(title,length) VALUES ('ks2',4000) ''')
cursor.execute('''UPDATE library SET title = 'Kasjer', length=1000 WHERE id=4 ''')
cursor.execute('''UPDATE library SET title = 'Kasjer', length=1000 WHERE id=4 ''')
cursor.execute('''ALTER TABLE library ADD Date_of_creation year ''')
connection.commit()
for row in cursor.execute('''SELECT * FROM library'''):
    print(row)
connection.close()
