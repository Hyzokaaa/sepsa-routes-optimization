class Vehicle:
    def __init__(self, vehicle_id, capacity):
        self.vehicle_id = vehicle_id
        self.capacity = capacity
        self.current_load = 0.0
        self.route = []

    def __str__(self):
        return f"Vehicle {self.vehicle_id} with capacity {self.capacity}, current load {self.current_load}, route {self.route}"
