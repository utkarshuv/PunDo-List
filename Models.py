from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(String(16), primary_key=True)
    user_name = Column(String(16))
    pswd = Column(String(16))
    email = Column(String(64))