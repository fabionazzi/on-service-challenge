from pydantic import HttpUrl
from pydantic_settings import BaseSettings


class Configuration(BaseSettings):
    external_api_retries: int = 5
    external_api_timeout: int = 10
    external_api_url: HttpUrl = (
        "https://mock.apidog.com/m1/814105-793312-default/flight-events"
    )


config = Configuration()
