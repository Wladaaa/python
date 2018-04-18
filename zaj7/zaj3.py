#! /usr/bin/env
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import NUMERIC
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Test(Base):
    __tablename__='Library'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    length = Column(NUMERIC)
    
engine = create_engine('sqlite:///books.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
for test in session.query(Test).all():
    print(test.id, test.title, test.length)
new_data = Test(
    id = 8,
    title = u'ORM',
    length = 6.8)
session.add(new_data)
session.commit()
