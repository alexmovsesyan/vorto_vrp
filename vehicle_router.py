import math
import sys
from typing import Tuple

from data_loader import DataLoader
from load import Load

MAX_DRIVER_MINS = 12 * 60

class VehicleRouter:

    def __init__(self, file_path: str):
        self.loads = DataLoader(file_path).get_loads()
        self.total_time = 0

    def route_vehicles(self) -> None:
        """
        calculate the route for each driver, and print the output
        note: total cost is also calculated but not outputted
        """
        num_drivers = 0
        while self.loads:
            num_drivers += 1
            print(self._get_route_for_driver())

        total_cost = 500 * num_drivers + self.total_time

    def _get_route_for_driver(self) -> list[int]:
        """
        from the starting location (0,0), a use greedy approach to find the next closest load
        loop until the max driver time is reached or all loads have been processed
        return the route of load nums
        """
        curr_start, curr_end = 0, 0
        curr_time = 0
        route = []
        last_distance_home = 0

        while curr_time <= MAX_DRIVER_MINS and self.loads:
            next_load, distance_to_load = self._get_next_min_load(curr_start, curr_end)
            total_distance = distance_to_load + next_load.distance

            if curr_time + total_distance + next_load.distance_to_home <= MAX_DRIVER_MINS:
                curr_time += total_distance
                last_distance_home = next_load.distance_to_home
                self.loads.remove(next_load)
                curr_start, curr_end = next_load.dropoff
                route.append(next_load.num)
            else:
                break

        self.total_time += curr_time + last_distance_home
        return route

    def _get_next_min_load(self, pickup: float, dropoff: float) -> Tuple[Load, float]:
        """
        get the node with smallest distance to current location (pickup, dropoff)
        return the node along with the calculated distance
        """
        min_distance = math.inf
        min_load = None
        for load in self.loads:
            distance_to_load = load.get_distance_to_load(pickup, dropoff)

            if distance_to_load < min_distance:
                min_load = load
                min_distance = distance_to_load
        return (min_load, min_distance)


if __name__ == '__main__':
    load_data_file = sys.argv[1]
    vehicle_router = VehicleRouter(load_data_file)
    vehicle_router.route_vehicles()
