import random
from src.model.client import Client
from src.model.depot import Depot
from src.model.vehicle import Vehicle

class RoutingProblem:
    def __init__(self, depot, vehicles, orders, clients):
        self.depot = Depot(depot['id'], depot['position'])
        self.vehicles = {veh_id: Vehicle(veh_id, veh['capacity']) for veh_id, veh in vehicles.items()}
        self.orders = orders
        self.clients = {client_id: Client(client_id, client['position']) for client_id, client in clients.items()}


    def show_solution(self):
        for veh_id, vehicle in self.vehicles.items():
            print(f"Vehicle {veh_id}:")
            for order in vehicle.route:
                print(f"  {order}")

    def verify_routes(self):
        for veh_id, vehicle in self.vehicles.items():
            initial_load = sum(order['load'] for order in vehicle.route if order['type'] == 'delivery') + \
                           sum(order['delivery_load'] for order in vehicle.route if order['type'] == 'mixed')
            current_load = 0

            print(f"Vehicle {veh_id} starts with load: {current_load}")

            for order in vehicle.route:
                if order['type'] == 'delivery':
                    current_load = current_load
                elif order['type'] == 'pickup':
                    current_load += order['load']
                elif order['type'] == 'mixed':
                    current_load += order['pickup_load']

                if current_load > vehicle.capacity:
                    print(
                        f"Capacity violation in vehicle {veh_id}: Current load {current_load} exceeds capacity {vehicle.capacity}")
                    return False

                print(
                    f"Vehicle {veh_id} current load after {order['type']} from {order['origin']} to {order['destination']}: {current_load}")

        print("All routes are valid.")
        return True
