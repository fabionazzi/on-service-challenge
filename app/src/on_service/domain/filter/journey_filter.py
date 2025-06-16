from abc import ABC, abstractmethod
from typing import List
from on_service.domain.models import Journey


class JourneyFilter(ABC):

    @abstractmethod
    def filter_journeys(self, journeys: List[Journey]) -> List[Journey]:
        """Filter journeys based on a condition."""
        pass


class MaxConnectionFilter(JourneyFilter):
    """Filter journeys with more than N connections."""

    def __init__(self, max_connections: int = 1):
        self._max_connections = max_connections

    def filter_journeys(self, journeys: List[Journey]) -> List[Journey]:
        return list(filter(lambda x: len(x.path) <= self._max_connections, journeys))


class MaxDurationFilter(JourneyFilter):
    """Filter journeys that last more than X hours."""

    FIRST_EVENT = 0
    LAST_EVENT = -1
    HOUR_SECS = 3600

    def __init__(self, max_duration: float = 24.0):
        self._max_duration = max_duration

    def filter_journeys(self, journeys: List[Journey]) -> List[Journey]:

        def total_hours(journey) -> float:
            path = journey.path
            return (
                path[self.LAST_EVENT].arrival_datetime
                - path[self.FIRST_EVENT].departure_datetime
            ).total_seconds() / self.HOUR_SECS

        return list(filter(lambda x: total_hours(x) <= self._max_duration, journeys))


class MaxStopoverFilter(JourneyFilter):
    """Filter journeys with a stopover that lasts more than X hours."""

    def __init__(self, max_stopover_duration: float = 4.0):
        self._max_stopover_duration = max_stopover_duration

    def filter_journeys(self, journeys: List[Journey]) -> List[Journey]:

        def max_stopover_duration(journey) -> float:
            path = journey.path
            max_duration = 0.0
            if len(path) > 1:
                stopovers = []
                path = journey.path
                for idx in range(1, len(path)):
                    stopovers.append(
                        (
                            path[idx].departure_datetime
                            - path[idx - 1].arrival_datetime
                        ).total_seconds()
                        / 3600
                    )
                    max_duration = max(stopovers)

            return max_duration

        return list(
            filter(
                lambda x: max_stopover_duration(x) <= self._max_stopover_duration,
                journeys,
            )
        )
