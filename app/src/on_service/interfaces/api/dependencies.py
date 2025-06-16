from on_service.configuration import config
from on_service.application.factories import JourneyCreatorFactory
from on_service.application.use_cases import JourneyCreatorUseCase


def get_journeys_creator_use_case() -> JourneyCreatorUseCase:
    journey_creator = JourneyCreatorFactory.create(config)
    return journey_creator
