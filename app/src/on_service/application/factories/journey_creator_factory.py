from on_service.infrastructure.api_client import APIClientFactory
from on_service.infrastructure.external_services import APIDogFlightEventsProvider
from on_service.application.use_cases import JourneyCreatorUseCase


class JourneyCreatorFactory:

    @staticmethod
    def create(config) -> JourneyCreatorUseCase:
        api_client = APIClientFactory.create(
            config.external_api_retries, config.external_api_timeout
        )
        events_provider = APIDogFlightEventsProvider(
            api_client, config.external_api_url
        )
        return JourneyCreatorUseCase(events_provider)
