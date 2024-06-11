from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, TIMESTAMP,ARRAY,BigInteger,ForeignKeyConstraint
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

    def to_dict(self):
        return {
            "id":self.id,
            "phone":self.phone,
            "username":self.username
        }
           
class Apartments(Base):
    __tablename__ = "apartments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String)
    description = Column(String)
    price = Column(Integer)

    media = relationship("Media", backref="apartment")

    def to_dict(self):
        return { 
            'id': self.id,
            'address': self.address,
            'description': self.description,
            'price': self.price,
            'media': [m.to_dict() for m in self.media]
        }

class Media(Base):
    __tablename__ = "media"
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    apartment_id = Column(BigInteger, ForeignKey('apartments.id'))
    media_id = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'apartment_id': self.apartment_id,
            'media_id': self.media_id
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
    def add_apartment(self, address: str, description: str, medias: list, price: int):
        try:  
            apartment = Apartments(address=address, description=description, price=price)
            self.session.add(apartment)
            self.session.commit()

            for media_id in medias:
                media = Media(apartment_id=apartment.id, media_id=media_id)
                self.session.add(media)
            
            self.session.commit()
            return True
        except Exception as err:
            self.session.rollback()
            print("Ошибка БД:", err)
            return False
        
    def get_apartments_list(self):
        existing_apartments = self.session.query(Apartments).all()
        if existing_apartments:
            apartments_list = [apartment.to_dict() for apartment in existing_apartments]
            return apartments_list
        else:
            return None
    def get_apartment_byId(self,id:int):
        existing_apartment = self.session.query(Apartments).filter_by(id=id).first()
        if existing_apartment:
            return existing_apartment.to_dict()
        else:
            return None
    def remove_apartment_byId(self, id:int):
        existing_apartment = self.session.query(Apartments).filter_by(id=int(id)).first()
        if existing_apartment:
            self.session.delete(existing_apartment)
            self.session.commit()
            return True
        else:
            return False
    def edit_apartment_byParameter(self, id:int, parameter:str,new_value):
        try:
            existing_apartment = self.session.query(Apartments).filter_by(id=int(id)).first()
            if existing_apartment:
                if parameter == "address":
                    existing_apartment.address = new_value
                elif parameter == "description":
                    existing_apartment.description = new_value
                elif parameter == "price":
                    existing_apartment.price = int(new_value)
                self.session.commit()
                return True
        except Exception:
            return False
        
    def get_all_users(self):
        users = self.session.query(User).all()
        if users:
            return [user.to_dict() for user in users]
        else:
            return None
DB = Database(os.getenv("DB_CONN"))