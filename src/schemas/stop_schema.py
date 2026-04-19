#Stop response dto
from pydantic import BaseModel

class StopResponse(BaseModel):
    id: int
    name: str
    city: str | None = None
    district: str | None = None

    class Config:
        orm_mode = True


class StopSearchResponse(BaseModel):
    stops: list[StopResponse]



class StopSearchRequest(BaseModel):
    keyword: str
    city: str
    district: str