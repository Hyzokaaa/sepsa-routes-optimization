import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, problem):
        self.problem = problem

    def plot_initial_state(self):
        depot = self.problem.depot
        clients = self.problem.clients.values()  # Accedemos a los valores directamente
        # Plot depot
        plt.scatter(depot.position[0], depot.position[1], c='red', marker='D', label='Depot')
        # Plot clients
        for client in clients:
            plt.scatter(client.position[0], client.position[1], c='blue', marker='o')
            plt.text(client.position[0], client.position[1], f' {client.loc_id}', fontsize=12)
        plt.xlabel('X coordinate')
        plt.ylabel('Y coordinate')
        plt.title('Initial State Visualization')
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_solution(self, solution):
        depot = self.problem.depot
        clients = self.problem.clients.values()  # Accedemos a los valores directamente
        # Plot depot
        plt.scatter(depot.position[0], depot.position[1], c='red', marker='D', label='Depot')
        # Plot clients
        for client in clients:
            plt.scatter(client.position[0], client.position[1], c='blue', marker='o')
            plt.text(client.position[0], client.position[1], f' {client.loc_id}', fontsize=12)
        # Plot routes
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        for idx, (vehicle_id, orders) in enumerate(solution.items()):
            route_x, route_y = [depot.position[0]], [depot.position[1]]
            for order in orders:
                if order.origin == self.problem.depot.loc_id:
                    client = self.problem.clients[order.destination]
                else:
                    client = self.problem.clients[order.origin]
                if client:
                    route_x.append(client.position[0])
                    route_y.append(client.position[1])
            route_x.append(depot.position[0])
            route_y.append(depot.position[1])
            plt.plot(route_x, route_y, colors[idx % len(colors)], label=f'Vehicle {vehicle_id}')
        plt.xlabel('X coordinate')
        plt.ylabel('Y coordinate')
        plt.title('Solution Visualization')
        plt.legend()
        plt.grid(True)
        plt.show()
