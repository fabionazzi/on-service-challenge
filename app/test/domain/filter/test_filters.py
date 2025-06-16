import pytest
from on_service.domain.filter.journey_filter import (
    MaxConnectionFilter,
    MaxDurationFilter,
    MaxStopoverFilter,
)
from on_service.domain.models import Journey
from .data import PATH_1, PATH_2, PATH_3, PATH_4, PATH_5, PATH_6, PATH_7


def create_journey(path) -> Journey:
    return Journey(path=path)


@pytest.fixture
def max_connection_filter(request):
    return MaxConnectionFilter(request.param)


@pytest.fixture
def max_duration_filter(request):
    return MaxDurationFilter(request.param)


@pytest.fixture
def max_stopover_filter(request):
    return MaxStopoverFilter(request.param)


@pytest.mark.parametrize(
    "journeys, expected_output, max_connection_filter, max_duration_filter, max_stopover_filter",
    [
        (
            [create_journey(PATH_1), create_journey(PATH_2)],
            [create_journey(PATH_1), create_journey(PATH_2)],
            2,
            24.0,
            4.0,
        )
    ],
    indirect=["max_connection_filter", "max_duration_filter", "max_stopover_filter"],
)
def test_journeys_not_filtered(
    journeys,
    expected_output,
    max_connection_filter,
    max_duration_filter,
    max_stopover_filter,
):
    # Given
    filters = [max_connection_filter, max_duration_filter, max_stopover_filter]

    # When
    for filter in filters:
        journeys = filter.filter_journeys(journeys)

    # Then
    assert journeys == expected_output


@pytest.mark.parametrize(
    "journeys, expected_output, max_connection_filter",
    [
        (
            [create_journey(PATH_1), create_journey(PATH_2)],
            [create_journey(PATH_1), create_journey(PATH_2)],
            2,
        ),
        (
            [create_journey(PATH_1), create_journey(PATH_6)],
            [create_journey(PATH_1)],
            2,
        ),
        (
            [create_journey(PATH_5), create_journey(PATH_6), create_journey(PATH_7)],
            [],
            3,
        ),
    ],
    indirect=["max_connection_filter"],
    ids=["No journeys filtered", "One journey filtered", "All journeys filtered"],
)
def test_filter_journey_with_more_connections_than_allowed(
    journeys, expected_output, max_connection_filter
):
    # When
    journeys = max_connection_filter.filter_journeys(journeys)

    # Then
    assert journeys == expected_output


@pytest.mark.parametrize(
    "journeys, expected_output, max_duration_filter",
    [
        (
            [create_journey(PATH_1), create_journey(PATH_2)],
            [create_journey(PATH_1), create_journey(PATH_2)],
            24.0,
        ),
        (
            [create_journey(PATH_1), create_journey(PATH_3)],
            [create_journey(PATH_1)],
            24.0,
        ),
        (
            [create_journey(PATH_3), create_journey(PATH_6)],
            [],
            12.0,
        ),
    ],
    indirect=["max_duration_filter"],
    ids=["No journeys filtered", "One journey filtered", "All journeys filtered"],
)
def test_filter_journey_lasting_more_than_allowed_duration(
    journeys, expected_output, max_duration_filter
):
    # When
    journeys = max_duration_filter.filter_journeys(journeys)

    # Then
    assert journeys == expected_output


@pytest.mark.parametrize(
    "journeys, expected_output, max_stopover_filter",
    [
        (
            [create_journey(PATH_1), create_journey(PATH_2)],
            [create_journey(PATH_1), create_journey(PATH_2)],
            4.0,
        ),
        (
            [create_journey(PATH_1), create_journey(PATH_4)],
            [create_journey(PATH_1)],
            4.0,
        ),
        (
            [create_journey(PATH_3), create_journey(PATH_6)],
            [],
            2.5,
        ),
    ],
    indirect=["max_stopover_filter"],
    ids=["No journeys filtered", "One journey filtered", "All journeys filtered"],
)
def test_filter_journey_with_stopover_more_than_allowed_stopover(
    journeys, expected_output, max_stopover_filter
):
    # When
    journeys = max_stopover_filter.filter_journeys(journeys)

    # Then
    assert journeys == expected_output
