from sqlalchemy.orm import Session
from src.models.stop import Stop
from src.dao.stop_dao import fetch_stops_by_keyword
from src.schemas.stop_schema import StopResponse

def get_all_stops(db: Session):
    return db.query(Stop).order_by(Stop.id).all()

def get_stops_by_keyword_city_district(db: Session, keyword: str, city: str, district: str):
    
    stops = fetch_stops_by_keyword(db, keyword, city, district)

    return [
        StopResponse(
            id=stop.id,
            name=stop.name,
            city=stop.city,
            district=stop.district
        )
        for stop in stops
    ]