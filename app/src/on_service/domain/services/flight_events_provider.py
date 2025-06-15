from abc import ABC, abstractmethod
from typing import List
from on_service.domain.models import FlightEvent


class FlightEventsProvider(ABC):
    """Abstract class for obtaining flight events"""

    @abstractmethod
    def get_events(self) -> List[FlightEvent]:
        """Retrieve all the flight events obtained from an endpoint."""
        pass
