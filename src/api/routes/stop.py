from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.services.stop_service import get_all_stops

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