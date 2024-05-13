from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, TIMESTAMP,ARRAY,BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
import sqlalchemy

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)
    phone = Column(String)
    username = Column(String)
class Apartments(Base):
    __tablename__ = "apartments"
    id = Column(Integer,primary_key=True,autoincrement=True)
    address = Column(String)
    description = Column(String)
    images = Column(ARRAY(String))
class Database:
    def __init__(self, conn):
        self.engine = sqlalchemy.create_engine(conn)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    def create_user(self, id, phone, username):
        try:
            user = User(id=id, phone=phone,username=username)
            self.session.add(user)
            self.session.commit()
            return True
        except Exception as err:
            print("ошибка бд: ", err)
            self.session.rollback()
            return False
    def check_user(self,id) -> bool:
        existing_user = self.session.query(User).filter_by(id=id).first()
        if existing_user:
            return True
        else:
            return False

DB = Database(os.getenv("DB_CONN"))