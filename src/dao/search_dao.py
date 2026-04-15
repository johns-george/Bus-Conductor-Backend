from sqlalchemy.orm import Session, aliased
from sqlalchemy import select, distinct
from src.models.route_stop import RouteStop
from src.models.stop import Stop
from src.models.edge import Edge

# returns route ids that have both from_stop_id and to_stop_id in the traveling order
def fetch_routes_by_stops(
    db: Session,
    from_stop_id: int,
    to_stop_id: int
):
    rs = aliased(RouteStop)
    rp = aliased(RouteStop)

    query = (
        select(distinct(rs.route_id))
        .join(rp, rs.route_id == rp.route_id)
        .where(
            rs.stop_id == from_stop_id,
            rp.stop_id == to_stop_id,
            rs.stop_order < rp.stop_order
        )
        .order_by(rs.route_id)
    )

    result = db.execute(query).scalars().all()
    return result





# return the ordered stops in a route
def fetch_route_stops_by_route_id(
    db: Session,
    route_id: int,
    from_stop_id: int,
    to_stop_id: int
):
    """
    DAO function that returns ordered stop names and
    distances between consecutive stops for a given route.
    """

    # Get stop orders
    from_order = db.execute(
        select(RouteStop.stop_order).where(
            RouteStop.route_id == route_id,
            RouteStop.stop_id == from_stop_id
        )
    ).scalar_one()

    to_order = db.execute(
        select(RouteStop.stop_order).where(
            RouteStop.route_id == route_id,
            RouteStop.stop_id == to_stop_id
        )
    ).scalar_one()

    rs = aliased(RouteStop)
    rs_next = aliased(RouteStop)

    # Query stops and distances
    query = (
        select(
            rs.stop_id,
            Stop.name.label("stop_name"),
            rs.stop_order,
            Edge.distance.label("distance")
        )
        .join(Stop, Stop.id == rs.stop_id)
        .outerjoin(
            rs_next,
            (rs.route_id == rs_next.route_id) &
            (rs_next.stop_order == rs.stop_order + 1)
        )
        .outerjoin(
            Edge,
            (Edge.from_stop == rs.stop_id) &
            (Edge.to_stop == rs_next.stop_id)
        )
        .where(
            rs.route_id == route_id,
            rs.stop_order >= from_order,
            rs.stop_order <= to_order
        )
        .order_by(rs.stop_order)
    )

    # Return raw rows for the service layer to map
    return db.execute(query).all()