from sqlalchemy import Column, BigInteger, String, Index
from sqlalchemy.orm import relationship
from src.core.database import Base

class Stop(Base):
    __tablename__ = "stop"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    city = Column(String(100))
    district = Column(String(100))
    # Graph relationships
    outgoing_edges = relationship("Edge", foreign_keys="Edge.from_stop", back_populates="from_stop_rel")
    incoming_edges = relationship("Edge", foreign_keys="Edge.to_stop", back_populates="to_stop_rel")

    # Route relationships
    route_stops = relationship("RouteStop", back_populates="stop")
    
    #Indexing for faster search by name
    __table_args__ = (
        Index("idx_stop_city", "city"),
        Index("idx_stop_district", "district"),
        Index(
            "idx_stop_name_trgm",
            "name",
            postgresql_using="gin",
            postgresql_ops={"name": "gin_trgm_ops"}
        ),
    )