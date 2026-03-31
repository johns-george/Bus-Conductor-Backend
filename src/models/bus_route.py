from sqlalchemy import Column, BigInteger, ForeignKey, Time, UniqueConstraint
from sqlalchemy.orm import relationship
from src.core.database import Base

class BusRoute(Base):
    __tablename__ = "bus_route"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    bus_id = Column(BigInteger, ForeignKey("bus.id"), nullable=False)
    route_id = Column(BigInteger, ForeignKey("route.id"), nullable=False)
    start_time = Column(Time, nullable=False)

    __table_args__ = (
        UniqueConstraint("bus_id", "route_id", "start_time", name="unique_bus_route_time"),
    )

    bus = relationship("Bus", back_populates="bus_routes")
    route = relationship("Route", back_populates="bus_routes")