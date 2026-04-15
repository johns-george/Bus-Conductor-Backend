from pydantic import BaseModel

class TicketResponse(BaseModel):
    id: int
    trip_id: int
    source_stop_id: int
    destination_stop_id: int
    time_of_travel: timestamp
    price: float

    class Config:
        orm_mode = True