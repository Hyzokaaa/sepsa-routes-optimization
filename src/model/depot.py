from src.model.location import Location


class Depot(Location):
    def __init__(self, depot_id, position):
        super().__init__(depot_id, position)
    def __str__(self):
        return f"Depot {self.loc_id} at position {self.position}"
