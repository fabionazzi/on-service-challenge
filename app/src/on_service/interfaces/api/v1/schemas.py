from datetime import datetime
from typing import List
from pydantic import BaseModel, computed_field, Field, ConfigDict


class Flight(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    flight_number: str
    departure_city: str = Field(..., alias="from")
    arrival_city: str = Field(..., alias="to")
    departure_datetime: datetime = Field(..., alias="departure_time")
    arrival_datetime: datetime = Field(..., alias="arrival_time")


class JourneyReponse(BaseModel):
    path: List[Flight]

    @computed_field
    @property
    def connections(self) -> int:
        return len(self.path) - 1
