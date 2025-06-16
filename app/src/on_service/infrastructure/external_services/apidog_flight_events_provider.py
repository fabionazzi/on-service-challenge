from datetime import datetime
from typing import List
from httpx import Client
from pydantic import BaseModel, TypeAdapter
from on_service.domain.services import FlightEventsProvider
from on_service.domain.models import FlightEvent


class APIDogFlightEvent(BaseModel):
    flight_number: str
    departure_city: str
    arrival_city: str
    departure_datetime: datetime
    arrival_datetime: datetime


event_list_adapter = TypeAdapter(list[APIDogFlightEvent])


class APIDogFlightEventsProvider(FlightEventsProvider):

    def __init__(self, api_client: Client, url: str):
        self._client = api_client
        self._url = url

    def get_events(self) -> List[FlightEvent]:
        response = self._client.get(str(self._url))
        response.raise_for_status()
        flight_events = event_list_adapter.validate_python(response.json())
        model_events = [FlightEvent(**event.model_dump()) for event in flight_events]
        return model_events
