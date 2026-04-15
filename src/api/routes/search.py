from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.types.search_types import SearchRouteRequest
from src.core.database import get_db
from src.services.stop_service import get_all_stops
from src.services.search_service import get_mapped_routes, get_routes_by_stops
from src.types.search_types import SearchRouteResponse

router = APIRouter(prefix="/search")


@router.post("/")
def search_route( search_request:SearchRouteRequest, db: Session = Depends(get_db)):
    # for getting all routes from from_stop_id to to_stop_id
    route_ids = get_routes_by_stops(search_request.from_stop_id, search_request.to_stop_id, db)

    # mapping stops in the routes
    mapped_routes = get_mapped_routes(db, route_ids, search_request.from_stop_id, search_request.to_stop_id)
    
    return mapped_routes