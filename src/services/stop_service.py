from sqlalchemy.orm import Session
from src.models.stop import Stop


def get_all_stops(db: Session):
    return db.query(Stop).order_by(Stop.id).all()