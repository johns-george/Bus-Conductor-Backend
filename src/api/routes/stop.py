from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.services.stop_service import get_all_stops
from src.services.stop_service import get_stops_by_keyword_city_district
from src.schemas.stop_schema import StopSearchRequest, StopSearchResponse

router = APIRouter(prefix="/stops")


@router.get("/get-all-stops")
def fetch_all_stops(db: Session = Depends(get_db)):
    stops = get_all_stops(db)

    return [
        {
            "id": stop.id,
            "name": stop.name,
            "address": stop.address
        }
        for stop in stops
    ]

@router.post("/get-stop")
def get_stop_by_keyword(stoprequest: StopSearchRequest, db: Session = Depends(get_db)):

    results = get_stops_by_keyword_city_district(
        db,
        keyword=stoprequest.keyword,
        city=stoprequest.city,
        district=stoprequest.district
    )

    return StopSearchResponse(stops=results)