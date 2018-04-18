#! /usr/bin/env
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import NUMERIC
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlite3
connection =sqlite3.connect("example.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS test (id integer, name text, value real)''')
cursor.execute('''INSERT INTO test VALUES (1, 'TEST', 1.3)''')
connection.commit()
for row in cursor.execute('''SELECT * FROM test'''):
    print(row)

connection.close()
Base = declarative_base()
class Test(Base):
    __tablename__='test'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    value = Column(NUMERIC)
engine = create_engine('sqlite:///example.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
for test in session.query(Test).all():
    print(test.id, test.name, test.value)
new_data = Test(
    id = 8,
    name = u'ORM',
    value = 6.8}
session.add(new_data)
session.commit()
