from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from src.core.database import Base

class Bus(Base):
    __tablename__ = "bus"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(100))
    bus_number = Column(String(20), unique=True)

    bus_routes = relationship("BusRoute", back_populates="bus")