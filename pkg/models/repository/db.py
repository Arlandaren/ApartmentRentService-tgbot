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
    images = Column(ARRAY(Integer))
    price = Column(Integer)
    def to_dict(self):
        return {
            'id': self.id,
            'address': self.address,
            'description': self.description,
            'images': self.images,
            'price': self.price
        }
class Database:
    def __init__(self, conn):
        if conn and conn.startswith("postgres://"):
            conn = conn.replace("postgres://", "postgresql://", 1)
        self.engine = sqlalchemy.create_engine(conn)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    def create_user(self, id, phone, username):
        try:
            user = User(id=id, phone=phone,username=f"@{username}")
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
    def add_apartment(self, address:str, description:str, images:list):
        try:
            apartment = Apartments(address=address,description=description,images=images)
            self.session.add(apartment)
            self.session.commit()
            return True
        except Exception as err:
            self.session.rollback()
            print("Ошибка бд:",err)
            return False
    def get_apartments_list(self):
        existing_apartments = self.session.query(Apartments).all()
        if existing_apartments:
            apartments_list = [apartment.to_dict() for apartment in existing_apartments]
            return apartments_list
        else:
            return None
DB = Database(os.getenv("DB_CONN"))