from sqlalchemy import Column, Integer, String
from src.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    role = Column(String, default="USER")  # USER, CONDUCTOR, ADMIN
    mobile_number = Column(String, nullable=True)