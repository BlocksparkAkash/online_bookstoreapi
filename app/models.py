from .database import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    # hashed_password = Column(String)
    password = Column(String(255), nullable=False)



    