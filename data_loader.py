from load import Load

class DataLoader:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_loads(self) -> list[Load]:
        """
        load input data from text file into list of Loads
        """
        loads = []
        with open(self.file_path) as file:
            next(file)  #ignore header
            for line in file:
                load_line = line.split()
                id = int(load_line[0])
                pickup = self._get_location_from_str(load_line[1])
                dropoff = self._get_location_from_str(load_line[2])
                loads.append(Load(id, pickup, dropoff))
        return loads

    def _get_location_from_str(self, location_str: str) -> list[float]:
        location_str = location_str.replace("(", "").replace(")", "")
        start, end = location_str.split(",")
        return [float(start), float(end)]
