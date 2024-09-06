import math

class Load:

    def __init__(self, load_num: int, pickup: list[float], dropoff: list[float]):
        self.pickup = pickup
        self.dropoff = dropoff
        self.num = load_num
        self.distance = math.sqrt((dropoff[0] - pickup[0])**2 +
                                  (dropoff[1] - pickup[1])**2)
        self.distance_to_home = math.sqrt((dropoff[0])**2 + (dropoff[1])**2)

    def get_distance_to_load(self, x: float, y: float):
        return math.sqrt((x - self.pickup[0])**2 + (y - self.pickup[1])**2)
