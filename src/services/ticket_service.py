from sqlalchemy.orm import Session
from src.models.ticket import ticket
from datetime import datetime

def create_ticket(
    db: Session,
    user_id: int,
    trip_id: int,
    seat_id: int,
    source_stop_id: int,
    destination_stop_id: int
):
    new_ticket = ticket(
        user_id=user_id,
        trip_id=trip_id,
        seat_id=seat_id,
        source_stop_id=source_stop_id,
        destination_stop_id=destination_stop_id,
        booking_time = datetime.utcnow(),
        status = "CONFIRMED"
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

def get_all_tickets(db: Session, user_id: int):
    return db.query(ticket).filter(ticket.user_id == user_id).order_by(ticket.id).all()

def get_ticket(db: Session, ticket_id: int):
    return db.query(ticket).filter(ticket.id == ticket_id).first()

def update_ticket(db: Session, ticket_id: int, ticket_data):
    ticket = db.query(ticket).filter(ticket.id == ticket_id).first()
    if not ticket:
        return {"error": "Ticket not found"}
    update_data = ticket_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(ticket, key, value)
    ticket.booking_time = datetime.utcnow()
    db.commit()
    db.refresh(ticket)
    return ticket

def cancel_ticket(db: Session, ticket_id: int):
    ticket = db.query(ticket).filter(ticket.id == ticket_id).first()
    if not ticket:
        return {"error": "Ticket not found"}
    ticket.status = "CANCELLED"
    ticket.booking_time = datetime.utcnow()
    db.commit()
    db.refresh(ticket)
    return ticket