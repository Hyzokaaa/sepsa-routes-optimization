class Location:
    def __init__(self, loc_id, position):
        self.loc_id = loc_id
        self.position = position

    def __str__(self):
        return f"Location {self.loc_id} at position {self.position}"
