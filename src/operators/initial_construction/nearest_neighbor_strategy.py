from src.operators.initial_construction.construction_strategy import ConstructionStrategy


class NearestNeighborStrategy(ConstructionStrategy):
    def __init__(self, vehicles, orders, clients, depot):
        self.vehicles = vehicles
        self.orders = orders
        self.clients = clients
        self.depot = depot

    def generate_solution(self):
        solution = {vehicle.vehicle_id: [] for vehicle in self.vehicles}
        unassigned_orders = self.orders[:]

        for vehicle in self.vehicles:
            current_location = self.depot.position
            assigned = True
            while unassigned_orders and assigned:
                assigned = False
                nearest_order = min(unassigned_orders, key=lambda order: self._distance(current_location,
                                                                                        self._get_location(
                                                                                        order.origin).position))
                if self.can_assign_order(vehicle, nearest_order, solution[vehicle.vehicle_id]):
                    solution[vehicle.vehicle_id].append(nearest_order)
                    unassigned_orders.remove(nearest_order)
                    current_location = self._get_location(nearest_order.destination).position
                    assigned = True
        if unassigned_orders:
            print(f"Some orders couldn't be assigned: {unassigned_orders}")

        return solution

    def _get_location(self, loc_id):
        if loc_id == self.depot.loc_id:
            return self.depot
        return self.clients[loc_id]

    def can_assign_order(self, vehicle, order, vehicle_orders):
        initial_load = sum(
            o.delivery_load if o.type == 'mixed' else o.load for o in vehicle_orders if o.type in ['delivery', 'mixed'])
        current_load = vehicle.current_load

        if order.type == 'delivery':
            if initial_load + order.load <= vehicle.capacity:
                return True
        elif order.type == 'pickup':
            if current_load + order.load <= vehicle.capacity:
                vehicle.current_load += order.load
                return True
        elif order.type == 'mixed':
            if (
                    initial_load + order.delivery_load <= vehicle.capacity and current_load + order.pickup_load <= vehicle.capacity):
                vehicle.current_load += order.pickup_load
                return True

        return False

    def _distance(self, loc1, loc2):
        return ((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2) ** 0.5
