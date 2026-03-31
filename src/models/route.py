from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from src.core.database import Base

class Route(Base):
    __tablename__ = "route"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(100))

    route_stops = relationship("RouteStop", back_populates="route")
    bus_routes = relationship("BusRoute", back_populates="route")