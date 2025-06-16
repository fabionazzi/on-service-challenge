from datetime import date
import pytest
from on_service.domain.services.path_finder import PathFinder
from .data import FLIGHT_EVENTS, EXPECTED_OUTPUT_EZE_SYD


@pytest.fixture
def path_finder():
    return PathFinder()


@pytest.mark.parametrize(
    "from_city, to_city, date, expected_output",
    [
        ("EZE", "SYD", date(2025, 6, 15), EXPECTED_OUTPUT_EZE_SYD),
        ("EZE", "ANY", date(2025, 6, 15), []),
        ("ANY", "JFK", date(2025, 6, 15), []),
        ("EZE", "SYD", date(2025, 7, 7), []),
    ],
    ids=[
        "Several paths",
        "Destination not found",
        "Origin not found",
        "No flights available for date",
    ],
)
def test_path_creation(from_city, to_city, date, expected_output, path_finder):
    # When
    paths = path_finder.create_paths(FLIGHT_EVENTS, from_city, to_city, date)

    # Then
    assert paths == expected_output
