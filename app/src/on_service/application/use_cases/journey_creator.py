from typing import List
from on_service.domain.models import FlightEvent, Journey
from on_service.domain.services import FlightEventsProvider


class JourneyCreatorUseCase:

    def __init__(self, flight_events_provider: FlightEventsProvider):
        self._flight_events_provider = flight_events_provider

    def create_journeys(self, departure_city: str, arrival_city: str) -> List[Journey]:
        events = self._flight_events_provider.get_events()
