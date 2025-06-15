from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class FlightEvent:
    flight_number: str
    departure_city: str
    arrival_city: str
    departure_datetime: datetime
    arrival_datetime: datetime


@dataclass
class Journey:
    path: List[FlightEvent]
