from datetime import date
from typing import List
from on_service.domain.models import FlightEvent


class PathFinder:

    @staticmethod
    def create_paths(
        events: List[FlightEvent], from_city: str, to_city: str, date: date
    ) -> List[List[FlightEvent]]:
        """Create all possible flight combinations between two cities."""

        def get_origins(events: List[FlightEvent], origin: str) -> List[FlightEvent]:
            filtered_events = list(filter(lambda x: x.departure_city == origin, events))
            for event in filtered_events:
                events.remove(event)
            return filtered_events

        def remove_visited(
            events: List[FlightEvent], visited: List[str]
        ) -> List[FlightEvent]:
            result = list(filter(lambda x: x.arrival_city not in visited, events))
            return result

        def get_next_steps(
            events: List[FlightEvent], next_city: str
        ) -> List[FlightEvent]:
            next_steps = list(filter(lambda x: x.departure_city == next_city, events))
            return next_steps

        def create_connections(
            origin: FlightEvent,
            destination: str,
            events: List[FlightEvent],
            next_steps: List[FlightEvent],
            paths: List[List[FlightEvent]],
            path: List = None,
        ):
            path = path or []
            if origin.arrival_city == destination:
                path.append(origin)
                paths.append(path)
            elif len(next_steps) > 0:
                path.append(origin)
                for step in next_steps:
                    next_steps = get_next_steps(events, step.arrival_city)
                    visited = [event.departure_city for event in path]
                    next_steps = remove_visited(next_steps, visited)
                    subpath = path.copy()
                    create_connections(
                        step, destination, events, next_steps, paths, subpath
                    )
            elif not next_steps:
                print("Destination cannot be reached.")

        departure_events = list(
            filter(
                lambda x: x.departure_datetime.date() == date,
                get_origins(events, from_city),
            )
        )
        events = remove_visited(events, [from_city])

        paths = []
        for origin in departure_events:
            next_steps = get_next_steps(events, origin.arrival_city)
            create_connections(origin, to_city, events, next_steps, paths)

        return paths
