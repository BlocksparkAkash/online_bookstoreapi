from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm  import relationship

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    # hashed_password = Column(String)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    orders = relationship('Orders', back_populates='user')







    

    