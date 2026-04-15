from pydantic import BaseModel

class SearchRouteRequest(BaseModel):
    from_stop_id: int
    to_stop_id: int

class WeightedStopMap(BaseModel):
    stop_name: str
    distance: float

class RouteMap(BaseModel):
    route_id: int
    stops: list[WeightedStopMap]

class SearchRouteResponse(BaseModel):
    route_ids: list[RouteMap]