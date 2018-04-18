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
    def zmienDane(self, iden, dane, dlugosc):
        engine = create_engine('sqlite:///books.db', echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        user1 = session.query(Test).filter_by(id=iden).first().title = dane
        user1 = session.query(Test).filter_by(id=iden).first().length = dlugosc
        session.commit()
        
    def usunKsiazke(self, iden):
        engine = create_engine('sqlite:///books.db', echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        user1 = session.query(Test).filter_by(id=iden).first()
        session.delete(user1)
        session.commit()
    def dodajKsiazke(self,iden, nazwa, dlugosc):
        engine = create_engine('sqlite:///books.db', echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        new_data = Test(
            id = iden,
            title = nazwa,
            length = dlugosc)
        session.add(new_data)
        session.commit()
    def printuj(self):
        for test in session.query(Test).all():
            print(test.id, test.title, test.length)
engine = create_engine('sqdanelite:///books.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
tryy = Test()
tryy.printuj()
tryy.zmienDane(4,'fafaafafaf',3434)
tryy.printuj()
