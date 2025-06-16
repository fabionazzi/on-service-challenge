from on_service.domain.models import FlightEvent
from on_service.domain.models import Journey


EVENT_1 = {
    "flight_number": "AA100",
    "departure_city": "BUE",
    "arrival_city": "GRU",
    "departure_datetime": "2025-06-17T08:00:00Z",
    "arrival_datetime": "2025-06-17T10:00:00Z",
}
EVENT_2 = {
    "flight_number": "LA200",
    "departure_city": "GRU",
    "arrival_city": "MAD",
    "departure_datetime": "2025-06-17T12:00:00Z",
    "arrival_datetime": "2025-06-17T20:00:00Z",
}
EVENT_3 = {
    "flight_number": "AF300",
    "departure_city": "BUE",
    "arrival_city": "FRA",
    "departure_datetime": "2025-06-17T06:00:00Z",
    "arrival_datetime": "2025-06-17T08:00:00Z",
}
EVENT_4 = {
    "flight_number": "LH400",
    "departure_city": "FRA",
    "arrival_city": "MAD",
    "departure_datetime": "2025-06-17T10:00:00Z",
    "arrival_datetime": "2025-06-17T16:00:00Z",
}


def create_flight_event(event) -> FlightEvent:
    return FlightEvent(**event)


def create_journey(path) -> Journey:
    return Journey(path=path)


PATH_1 = [create_flight_event(EVENT_1), create_flight_event(EVENT_2)]
PATH_2 = [create_flight_event(EVENT_3), create_flight_event(EVENT_4)]

JOURNEYS = [create_journey(PATH_1), create_journey(PATH_2)]
