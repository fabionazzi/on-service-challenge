from typing import List
from pydantic import BaseModel, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class FilterConfiguration(BaseModel):
    name: str
    params: dict


class Configuration(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="/configuration/.env", env_file_encoding="utf-8"
    )

    external_api_retries: int = 5
    external_api_timeout: int = 10
    external_api_url: HttpUrl = (
        "https://mock.apidog.com/m1/814105-793312-default/flight-events"
    )
    filter_config: List[FilterConfiguration]


config = Configuration()
