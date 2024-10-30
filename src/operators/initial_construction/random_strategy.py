import random
from src.model.vehicle import Vehicle
from src.operators.initial_construction.construction_strategy import ConstructionStrategy


class RandomStrategy(ConstructionStrategy):
    def __init__(self, vehicles, orders):
        # Asume que vehicles es una lista de objetos Vehicle
        self.vehicles = vehicles
        self.orders = orders

    def generate_solution(self):
        solution = {vehicle.vehicle_id: [] for vehicle in self.vehicles}
        all_orders = random.sample(self.orders, len(self.orders))

        for order in all_orders:
            possible_vehicles = list(self.vehicles)
            assigned = False

            while possible_vehicles and not assigned:
                vehicle = random.choice(possible_vehicles)
                if self.can_assign_order(vehicle, order, solution[vehicle.vehicle_id]):
                    solution[vehicle.vehicle_id].append(order)
                    assigned = True
                else:
                    possible_vehicles.remove(vehicle)

            if not assigned:
                print(
                    f"Unable to assign order {order} to any vehicle. Check vehicle capacities and order requirements.")

        return solution

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
