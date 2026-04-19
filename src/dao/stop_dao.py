from sqlalchemy.orm import Session
from sqlalchemy import select, case
from src.models.stop import Stop

def fetch_stops_by_keyword(
    db: Session,
    keyword: str,
    city: str,
    district: str,
    limit: int = 20
):
    query = (
        select(Stop)
        .where(Stop.name.ilike(f"{keyword}%"))
        .order_by(
            case(
                (Stop.city == city, 1),
                (Stop.district == district, 2),
                else_=3
            ),
            Stop.name
        )
        .limit(limit)
    )

    return db.execute(query).scalars().all()