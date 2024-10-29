import random

from src.model.vehicle import Vehicle
from src.operators.initial_construction.construction_strategy import ConstructionStrategy


class RandomConstructionStrategy(ConstructionStrategy):
    def __init__(self, vehicles, orders):
        self.vehicles = {veh_id: Vehicle(veh_id, veh['capacity']) for veh_id, veh in vehicles.items()}
        self.orders = orders

    def generate_solution(self):
        solution = {vehicle.vehicle_id: [] for vehicle in self.vehicles.values()}

        all_orders = random.sample(self.orders, len(self.orders))

        for order in all_orders:
            possible_vehicles = list(self.vehicles.keys())
            assigned = False
            while possible_vehicles and not assigned:
                vehicle_id = random.choice(possible_vehicles)
                vehicle = self.vehicles[vehicle_id]

                # Calcula la carga inicial de entregas
                initial_load = sum(
                    o['delivery_load'] if o['type'] == 'mixed' else o['load'] for o in solution[vehicle_id] if
                    o['type'] in ['delivery', 'mixed'])
                # Carga actual incluyendo recogidas
                current_load = vehicle.current_load

                if order['type'] == 'delivery':
                    if initial_load + order['load'] <= vehicle.capacity:
                        vehicle.current_load = current_load
                        solution[vehicle_id].append(order)
                        assigned = True
                elif order['type'] == 'pickup':
                    if current_load + order['load'] <= vehicle.capacity:
                        vehicle.current_load += order['load']
                        solution[vehicle_id].append(order)
                        assigned = True
                elif order['type'] == 'mixed':
                    if (initial_load + order['delivery_load'] <= vehicle.capacity and current_load +
                            order['pickup_load'] <= vehicle.capacity):
                        vehicle.current_load = current_load + order['pickup_load']
                        solution[vehicle_id].append(order)
                        assigned = True

                if not assigned:
                    possible_vehicles.remove(vehicle_id)

            if not assigned:
                print(
                    f"Unable to assign order {order} to any vehicle. Check vehicle capacities and order requirements.")

        return solution
