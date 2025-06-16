from datetime import datetime, timezone
from on_service.domain.models import FlightEvent

# --- 1 stopover < 4h, total duration < 24h (Case 1) ---
PATH_1 = [
    FlightEvent(
        flight_number="AA100",
        departure_city="EZE",
        arrival_city="GRU",
        departure_datetime=datetime(2025, 6, 15, 8, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 15, 10, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="LA200",
        departure_city="GRU",
        arrival_city="JFK",
        departure_datetime=datetime(2025, 6, 15, 12, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 15, 20, 0, tzinfo=timezone.utc),
    ),
]

# --- 1 stopover < 4h, total duration < 24h (Case 2) ---
PATH_2 = [
    FlightEvent(
        flight_number="AF300",
        departure_city="CDG",
        arrival_city="FRA",
        departure_datetime=datetime(2025, 6, 16, 6, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 16, 8, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="LH400",
        departure_city="FRA",
        arrival_city="JFK",
        departure_datetime=datetime(2025, 6, 16, 10, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 16, 16, 0, tzinfo=timezone.utc),
    ),
]

# --- total duration > 24h (Case 3) ---
PATH_3 = [
    FlightEvent(
        flight_number="EK500",
        departure_city="DXB",
        arrival_city="SIN",
        departure_datetime=datetime(2025, 6, 17, 2, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 17, 16, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="SQ600",
        departure_city="SIN",
        arrival_city="SYD",
        departure_datetime=datetime(2025, 6, 18, 18, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 19, 6, 0, tzinfo=timezone.utc),
    ),
]

# --- stopover > 4h (Case 4) ---
PATH_4 = [
    FlightEvent(
        flight_number="UA700",
        departure_city="ORD",
        arrival_city="DEN",
        departure_datetime=datetime(2025, 6, 20, 9, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 20, 11, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="UA701",
        departure_city="DEN",
        arrival_city="SFO",
        departure_datetime=datetime(2025, 6, 20, 17, 30, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 20, 19, 30, tzinfo=timezone.utc),
    ),
]

# --- 3+ connections (Case 5) ---
PATH_5 = [
    FlightEvent(
        flight_number="IB800",
        departure_city="MAD",
        arrival_city="BCN",
        departure_datetime=datetime(2025, 6, 21, 6, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 21, 7, 30, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="VY900",
        departure_city="BCN",
        arrival_city="FCO",
        departure_datetime=datetime(2025, 6, 21, 9, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 21, 11, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="AZ100",
        departure_city="FCO",
        arrival_city="ATH",
        departure_datetime=datetime(2025, 6, 21, 13, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 21, 15, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="A3500",
        departure_city="ATH",
        arrival_city="IST",
        departure_datetime=datetime(2025, 6, 21, 16, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 21, 17, 30, tzinfo=timezone.utc),
    ),
]

# --- 3+ connections (Case 6) ---
PATH_6 = [
    FlightEvent(
        flight_number="DL100",
        departure_city="ATL",
        arrival_city="JFK",
        departure_datetime=datetime(2025, 6, 22, 7, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 22, 9, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="AA200",
        departure_city="JFK",
        arrival_city="LHR",
        departure_datetime=datetime(2025, 6, 22, 11, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 22, 21, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="BA300",
        departure_city="LHR",
        arrival_city="DXB",
        departure_datetime=datetime(2025, 6, 23, 0, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 23, 8, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="EK400",
        departure_city="DXB",
        arrival_city="BOM",
        departure_datetime=datetime(2025, 6, 23, 10, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 23, 14, 0, tzinfo=timezone.utc),
    ),
]

# --- 3+ connections (Case 7) ---
PATH_7 = [
    FlightEvent(
        flight_number="QF10",
        departure_city="PER",
        arrival_city="MEL",
        departure_datetime=datetime(2025, 6, 24, 6, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 24, 11, 0, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="VA200",
        departure_city="MEL",
        arrival_city="SYD",
        departure_datetime=datetime(2025, 6, 24, 13, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 24, 14, 30, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="JQ500",
        departure_city="SYD",
        arrival_city="BNE",
        departure_datetime=datetime(2025, 6, 24, 16, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 24, 17, 30, tzinfo=timezone.utc),
    ),
    FlightEvent(
        flight_number="QF600",
        departure_city="BNE",
        arrival_city="CNS",
        departure_datetime=datetime(2025, 6, 24, 19, 0, tzinfo=timezone.utc),
        arrival_datetime=datetime(2025, 6, 24, 21, 0, tzinfo=timezone.utc),
    ),
]
