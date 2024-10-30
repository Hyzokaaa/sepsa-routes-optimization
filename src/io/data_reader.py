from src.model.client import Client
from src.model.depot import Depot
from src.model.order import Order
from src.model.problem import Problem
from src.model.vehicle import Vehicle


class DataReader:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, 'r') as file:
            section = None
            depot = None
            vehicles = []
            orders = []
            clients = {}
            for line in file:
                line = line.strip()
                if line.startswith('#'):
                    section = line[1:].strip()
                elif section == 'Depot Position':
                    parts = line.split(',')
                    if len(parts) == 3:
                        depot = Depot(parts[0].strip(), (float(parts[1]), float(parts[2])))
                elif section == 'Vehicles':
                    parts = line.split(',')
                    if len(parts) == 2:
                        vehicle_id, capacity = parts
                        vehicles.append(Vehicle(vehicle_id.strip(), float(capacity)))
                elif section == 'Orders':
                    parts = line.split(',')
                    if parts[0] == 'delivery' and len(parts) == 4:
                        orders.append(Order(parts[0].strip(), parts[1].strip(), parts[2].strip(), float(parts[3])))
                    elif parts[0] == 'pickup' and len(parts) == 4:
                        orders.append(Order(parts[0].strip(), parts[1].strip(), parts[2].strip(), float(parts[3])))
                    elif parts[0] == 'mixed' and len(parts) == 5:
                        orders.append(Order(parts[0].strip(), parts[1].strip(), parts[2].strip(), None, float(parts[3]), float(parts[4])))
                elif section == 'Clients':
                    parts = line.split(',')
                    if len(parts) == 3:
                        client_id, x, y = parts
                        clients[client_id.strip()] = Client(client_id.strip(), (float(x), float(y)))
            return Problem(depot, vehicles, orders, clients)
