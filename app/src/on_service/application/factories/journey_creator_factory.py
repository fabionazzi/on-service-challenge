from on_service.infrastructure.api_client import APIClientFactory
from on_service.infrastructure.external_services import APIDogFlightEventsProvider
from on_service.application.use_cases import JourneyCreatorUseCase
from on_service.domain.services import PathFinder
from on_service.domain.filter import JourneyFilterFactory


class JourneyCreatorFactory:

    @staticmethod
    def create(config) -> JourneyCreatorUseCase:
        api_client = APIClientFactory.create(
            config.external_api_retries, config.external_api_timeout
        )
        events_provider = APIDogFlightEventsProvider(
            api_client, config.external_api_url
        )
        path_finder = PathFinder()
        filters = []
        for filter_config in config.filter_config:
            name = filter_config.name
            params = filter_config.params
            filter = JourneyFilterFactory.create(name, **params)
            filters.append(filter)
        return JourneyCreatorUseCase(events_provider, path_finder, filters)
