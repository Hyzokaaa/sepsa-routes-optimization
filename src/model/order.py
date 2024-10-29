class Order:
    def __init__(self, order_id, type, origin, destination, loads):
        self.order_id = order_id
        self.type = type
        self.origin = origin
        self.destination = destination
        self.loads = loads
