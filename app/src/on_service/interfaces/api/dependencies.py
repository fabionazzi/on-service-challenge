from on_service.configuration import config
from on_service.application.factories import JourneCreatorFactory
from on_service.application.use_cases import JourneCreatorUseCase


def get_journeys_creator_use_case() -> JourneCreatorUseCase:
    journey_creator = JourneCreatorUseCase.create(config)
    return journey_creator
