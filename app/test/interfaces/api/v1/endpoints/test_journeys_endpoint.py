from datetime import datetime, timezone
from unittest.mock import create_autospec, MagicMock
import pytest
from fastapi.testclient import TestClient
from on_service.main import app
from on_service.configuration import config, Configuration, FilterConfiguration
from on_service.application.use_cases import JourneyCreatorUseCase
from on_service.interfaces.api.dependencies import get_journeys_creator_use_case
from .data import JOURNEYS

client = TestClient(app)


def mock_journey_creator() -> MagicMock:
    journey_creator = create_autospec(JourneyCreatorUseCase)
    journeys = JOURNEYS
    journey_creator.create_journeys.return_value = journeys
    return journey_creator


@pytest.mark.parametrize(
    "params, expected_status",
    [
        ({}, 422),
        ({"from": "BUE"}, 422),
        ({"from": "BUE", "to": "MAD"}, 422),
        ({"from": "BUE", "to": "MAD", "date": "2025-6-17"}, 422),
    ],
)
def test_journeys_search_with_error_params(params, expected_status):
    # When
    response = client.get("journeys/search", params=params)

    # Then
    assert response.status_code == expected_status


def test_journeys_search_successfully():
    # Given
    app.dependency_overrides[get_journeys_creator_use_case] = mock_journey_creator
    params = {"from": "BUE", "to": "MAD", "date": "2025-06-17"}
    # When
    response = client.get("journeys/search", params=params)

    # Then
    assert response.status_code == 200
    assert len(response.json()) == len(JOURNEYS)
