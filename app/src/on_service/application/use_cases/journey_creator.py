from datetime import date
from typing import List
from on_service.domain.models import Journey
from on_service.domain.services import FlightEventsProvider, PathFinder
from on_service.domain.filter import JourneyFilter


class JourneyCreatorUseCase:

    def __init__(
        self,
        flight_events_provider: FlightEventsProvider,
        path_finder: PathFinder,
        filters: List[JourneyFilter],
    ):
        self._flight_events_provider = flight_events_provider
        self._path_finder = path_finder
        self._filters = filters

    def create_journeys(
        self, departure_city: str, arrival_city: str, date: date
    ) -> List[Journey]:
        events = self._flight_events_provider.get_events()
        paths = self._path_finder.create_paths(
            events, departure_city, arrival_city, date
        )
        journeys = [Journey(path=path) for path in paths]
        for filter in self._filters:
            journeys = filter.filter_journeys(journeys)

        return journeys
