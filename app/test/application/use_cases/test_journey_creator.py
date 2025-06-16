from datetime import date
from unittest.mock import create_autospec
import pytest
from on_service.application.use_cases.journey_creator import JourneyCreatorUseCase
from on_service.domain.services import FlightEventsProvider, PathFinder
from on_service.domain.filter import JourneyFilter
from on_service.domain.models import FlightEvent

EVENT_1 = create_autospec(FlightEvent, departure_city="EZE", arrival_city="GRU")
EVENT_2 = create_autospec(FlightEvent, departure_city="GRU", arrival_city="SYD")
EVENT_3 = create_autospec(FlightEvent, departure_city="EZE", arrival_city="LHR")
EVENT_4 = create_autospec(FlightEvent, departure_city="LHR", arrival_city="AKL")
EVENT_5 = create_autospec(FlightEvent, departure_city="AKL", arrival_city="SYD")

EVENTS = [EVENT_1, EVENT_2, EVENT_3, EVENT_4, EVENT_5]
PATHS = [[EVENT_1, EVENT_2], [EVENT_3, EVENT_4, EVENT_5]]


@pytest.fixture
def flight_events_provider():
    return create_autospec(FlightEventsProvider)


@pytest.fixture
def path_finder():
    return create_autospec(PathFinder)


@pytest.fixture
def filters():
    filters = [create_autospec(JourneyFilter) for _ in range(3)]
    for filter in filters:
        filter.filter_journeys.side_effect = lambda x: x
    return filters


@pytest.fixture
def journey_creator(flight_events_provider, path_finder, filters):
    return JourneyCreatorUseCase(flight_events_provider, path_finder, filters)


def test_journey_creation(
    flight_events_provider, path_finder, filters, journey_creator
):
    # Given
    departure_city = "EZE"
    arrival_city = "SYD"
    departure_date = date(2025, 6, 15)
    flight_events_provider.get_events.return_value = EVENTS
    path_finder.create_paths.return_value = PATHS

    # When
    result = journey_creator.create_journeys(
        departure_city, arrival_city, departure_date
    )

    # Then
    assert len(result) == len(PATHS)
    flight_events_provider.get_events.assert_called_once()
    path_finder.create_paths.assert_called_once_with(
        EVENTS, departure_city, arrival_city, departure_date
    )
    for filter in filters:
        filter.filter_journeys.assert_called_once()
