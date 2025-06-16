from datetime import date, datetime, timezone
from on_service.domain.models import FlightEvent

FLIGHT_EVENTS = [
    FlightEvent(
        flight_number="AA110",
        departure_city="EZE",
        arrival_city="SYD",
        departure_datetime=datetime(2025, 6, 15, 20, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 17, 5, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="AA101",
        departure_city="EZE",
        arrival_city="MIA",
        departure_datetime=datetime(2025, 6, 15, 20, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 16, 5, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="LA800",
        departure_city="MIA",
        arrival_city="SCL",
        departure_datetime=datetime(2025, 6, 16, 8, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 16, 16, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="LA810",
        departure_city="MIA",
        arrival_city="SCL",
        departure_datetime=datetime(2025, 6, 16, 10, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 16, 18, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="QF12",
        departure_city="SCL",
        arrival_city="SYD",
        departure_datetime=datetime(2025, 6, 16, 23, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 18, 6, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="BA246",
        departure_city="EZE",
        arrival_city="LHR",
        departure_datetime=datetime(2025, 6, 15, 21, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 16, 15, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="QF2",
        departure_city="LHR",
        arrival_city="SYD",
        departure_datetime=datetime(2025, 6, 16, 21, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 18, 5, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="NZ247",
        departure_city="EZE",
        arrival_city="AKL",
        departure_datetime=datetime(2025, 6, 15, 22, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 17, 6, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="NZ103",
        departure_city="AKL",
        arrival_city="SYD",
        departure_datetime=datetime(2025, 6, 17, 5, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 17, 6, 30, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="UA900",
        departure_city="EZE",
        arrival_city="SFO",
        departure_datetime=datetime(2025, 6, 15, 23, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 16, 9, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="QF74",
        departure_city="SFO",
        arrival_city="SYD",
        departure_datetime=datetime(2025, 6, 16, 22, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 18, 6, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="JL771",
        departure_city="NRT",
        arrival_city="SYD",
        departure_datetime=datetime(2025, 6, 17, 22, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 18, 8, 30, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="QF26",
        departure_city="NRT",
        arrival_city="BNE",
        departure_datetime=datetime(2025, 6, 17, 21, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 18, 7, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="QF524",
        departure_city="BNE",
        arrival_city="SYD",
        departure_datetime=datetime(2025, 6, 18, 9, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 18, 10, 30, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="AF123",
        departure_city="CDG",
        arrival_city="JFK",
        departure_datetime=datetime(2025, 6, 16, 14, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 16, 17, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="DL200",
        departure_city="ATL",
        arrival_city="LAX",
        departure_datetime=datetime(2025, 6, 16, 12, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 16, 14, 30, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="QF400",
        departure_city="SYD",
        arrival_city="MEL",
        departure_datetime=datetime(2025, 6, 18, 7, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 18, 8, 30, tzinfo=timezone.utc),
    ),
]

EXPECTED_OUTPUT_EZE_SYD = [
    [
        FlightEvent(
            flight_number="AA110",
            departure_city="EZE",
            arrival_city="SYD",
            departure_datetime=datetime(2025, 6, 15, 20, 0, tzinfo=timezone.utc),
            arrival_datetime=datetime(2025, 6, 17, 5, 0, tzinfo=timezone.utc),
        )
    ],
    [
        FlightEvent(
            flight_number="AA101",
            departure_city="EZE",
            arrival_city="MIA",
            departure_datetime=datetime(2025, 6, 15, 20, 0, tzinfo=timezone.utc),
            arrival_datetime=datetime(2025, 6, 16, 5, 0, tzinfo=timezone.utc),
        ),
        FlightEvent(
            flight_number="LA800",
            departure_city="MIA",
            arrival_city="SCL",
            departure_datetime=datetime(2025, 6, 16, 8, 0, tzinfo=timezone.utc),
            arrival_datetime=datetime(2025, 6, 16, 16, 0, tzinfo=timezone.utc),
        ),
        FlightEvent(
            flight_number="QF12",
            departure_city="SCL",
            arrival_city="SYD",
            departure_datetime=datetime(2025, 6, 16, 23, 0, tzinfo=timezone.utc),
            arrival_datetime=datetime(2025, 6, 18, 6, 0, tzinfo=timezone.utc),
        ),
    ],
    [
        FlightEvent(
            flight_number="AA101",
            departure_city="EZE",
            arrival_city="MIA",
            departure_datetime=datetime(2025, 6, 15, 20, 0, tzinfo=timezone.utc),
            arrival_datetime=datetime(2025, 6, 16, 5, 0, tzinfo=timezone.utc),
        ),
        FlightEvent(
            flight_number="LA810",
            departure_city="MIA",
            arrival_city="SCL",
            departure_datetime=datetime(2025, 6, 16, 10, 0, tzinfo=timezone.utc),
            arrival_datetime=datetime(2025, 6, 16, 18, 0, tzinfo=timezone.utc),
        ),
        FlightEvent(
            flight_number="QF12",
            departure_city="SCL",
            arrival_city="SYD",
            departure_datetime=datetime(2025, 6, 16, 23, 0, tzinfo=timezone.utc),
            arrival_datetime=datetime(2025, 6, 18, 6, 0, tzinfo=timezone.utc),
        ),
    ],
    [
        FlightEvent(
            flight_number="BA246",
            departure_city="EZE",
            arrival_city="LHR",
            departure_datetime=datetime(2025, 6, 15, 21, 0, tzinfo=timezone.utc),
            arrival_datetime=datetime(2025, 6, 16, 15, 0, tzinfo=timezone.utc),
        ),
        FlightEvent(
            flight_number="QF2",
            departure_city="LHR",
            arrival_city="SYD",
            departure_datetime=datetime(2025, 6, 16, 21, 0, tzinfo=timezone.utc),
            arrival_datetime=datetime(2025, 6, 18, 5, 0, tzinfo=timezone.utc),
        ),
    ],
    [
        FlightEvent(
            flight_number="UA900",
            departure_city="EZE",
            arrival_city="SFO",
            departure_datetime=datetime(2025, 6, 15, 23, 0, tzinfo=timezone.utc),
            arrival_datetime=datetime(2025, 6, 16, 9, 0, tzinfo=timezone.utc),
        ),
        FlightEvent(
            flight_number="QF74",
            departure_city="SFO",
            arrival_city="SYD",
            departure_datetime=datetime(2025, 6, 16, 22, 0, tzinfo=timezone.utc),
            arrival_datetime=datetime(2025, 6, 18, 6, 0, tzinfo=timezone.utc),
        ),
    ],
]
