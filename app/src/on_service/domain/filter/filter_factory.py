from on_service.domain.filter.journey_filter import (
    JourneyFilter,
    MaxConnectionFilter,
    MaxDurationFilter,
    MaxStopoverFilter,
)


class UnexistentFilter(Exception):
    """Raised when tries to create a non-existing filter"""


JOURNEY_FILTER_REGISTRY = {
    "max_connections_number": MaxConnectionFilter,
    "max_duration_filter": MaxDurationFilter,
    "max_stopover_filter": MaxStopoverFilter,
}


class JourneyFilterFactory:

    @staticmethod
    def create(name: str, **kwargs) -> JourneyFilter:
        try:
            ctor = JOURNEY_FILTER_REGISTRY[name]
            return ctor(**kwargs)
        except KeyError as exc:
            raise UnexistentFilter(f"Filter with name: {name} does not exist") from exc
