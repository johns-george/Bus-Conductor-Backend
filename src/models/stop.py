from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from src.core.database import Base

class Stop(Base):
    __tablename__ = "stop"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    address = Column(String(255))

    # Graph relationships
    outgoing_edges = relationship("Edge", foreign_keys="Edge.from_stop", back_populates="from_stop_rel")
    incoming_edges = relationship("Edge", foreign_keys="Edge.to_stop", back_populates="to_stop_rel")

    # Route relationships
    route_stops = relationship("RouteStop", back_populates="stop")