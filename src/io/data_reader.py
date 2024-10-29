class DataReader:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, 'r') as file:
            section = None
            depot = {}
            vehicles = {}
            orders = []
            clients = {}
            for line in file:
                line = line.strip()
                if line.startswith('#'):
                    section = line[1:].strip()
                elif section == 'Depot Position':
                    parts = line.split(',')
                    if len(parts) == 3:
                        depot = {'id': parts[0], 'position': (float(parts[1]), float(parts[2]))}
                elif section == 'Vehicles':
                    parts = line.split(',')
                    if len(parts) == 2:
                        vehicle_id, capacity = parts
                        vehicles[vehicle_id] = {'capacity': float(parts[1])}
                elif section == 'Orders':
                    parts = line.split(',')
                    if parts[0] == 'delivery' and len(parts) == 4:
                        orders.append({'type': parts[0], 'origin': parts[1], 'destination': parts[2], 'load': float(parts[3])})
                    elif parts[0] == 'pickup' and len(parts) == 4:
                        orders.append({'type': parts[0], 'origin': parts[1], 'destination': parts[2], 'load': float(parts[3])})
                    elif parts[0] == 'mixed' and len(parts) == 5:
                        orders.append({'type': parts[0], 'origin': parts[1], 'destination': parts[2], 'delivery_load': float(parts[3]), 'pickup_load': float(parts[4])})
                elif section == 'Clients':
                    parts = line.split(',')
                    if len(parts) == 3:
                        client_id, x, y = parts
                        clients[client_id] = {'position': (float(x), float(y))}
            return depot, vehicles, orders, clients


