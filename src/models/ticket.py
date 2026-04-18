from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from datetime import datetime
from src.core.database import Base
from pydantic import BaseModel
from typing import Optional

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)  # you can link later if user table exists
    trip_id = Column(Integer, ForeignKey("trips.id"))

    source_stop_id = Column(Integer, ForeignKey("stops.id"))
    destination_stop_id = Column(Integer, ForeignKey("stops.id"))

    booking_time = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="CONFIRMED")

class TicketUpdate(BaseModel):
    price: Optional[float] = None
    destination_stop_id: Optional[int] = None