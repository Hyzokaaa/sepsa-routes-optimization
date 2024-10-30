from src.model.location import Location


class Client(Location):
    def __init__(self, client_id, position):
        super().__init__(client_id, position)

    def __str__(self):
        return f"Client {self.loc_id} at position {self.position}"
