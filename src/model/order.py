class Order:
    def __init__(self, order_type, origin, destination, load, delivery_load=None, pickup_load=None):
        self.type = order_type
        self.origin = origin
        self.destination = destination
        self.load = load
        self.delivery_load = delivery_load
        self.pickup_load = pickup_load

    def __str__(self):
        if self.type == 'mixed':
            return (f"Order {self.type} from {self.origin} to {self.destination} "
                    f"with delivery load {self.delivery_load} and pickup load {self.pickup_load}")
        else:
            return (f"Order {self.type} from {self.origin} to {self.destination} "
                    f"with load {self.load}")
