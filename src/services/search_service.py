
from src.dao.search_dao import (fetch_routes_by_stops, fetch_route_stops_by_route_id)
from src.types.search_types import RouteMap, WeightedStopMap
from sqlalchemy.orm import Session  
from typing import List

def get_routes_by_stops(from_stop_id: int, to_stop_id: int, db):
    
    route_ids = fetch_routes_by_stops(
        db,
        from_stop_id=from_stop_id,
        to_stop_id=to_stop_id
    )

    return route_ids



# returns stops well mapped for routes
def get_mapped_routes(
    db: Session,
    route_ids: List[int],
    from_stop_id: int,
    to_stop_id: int
) -> List[RouteMap]:
    
    # Service function that:
    # 1. Retrieves ordered stop segments with distances.
    # 2. Maps them into RouteMap response objects.

    mapped_routes: List[RouteMap] = []

    for route_id in route_ids:
        rows = fetch_route_stops_by_route_id(
            db, route_id, from_stop_id, to_stop_id
        )

        stops = [
            WeightedStopMap(
                stop_name=row.stop_name,
                distance=float(row.distance) if row.distance is not None else 0.0
            )
            for row in rows
        ]

        mapped_routes.append(
            RouteMap(
                route_id=route_id,
                stops=stops
            )
        )

    return mapped_routes