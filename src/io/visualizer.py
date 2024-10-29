import matplotlib.pyplot as plt


class Visualizer:
    def __init__(self, problem):
        self.problem = problem

    def plot_initial_state(self):
        depot = self.problem.depot
        clients = self.problem.clients

        # Plot depot
        plt.scatter(depot.x, depot.y, c='red', marker='D', label='Depot')

        # Plot clients
        for client in clients:
            plt.scatter(client.x, client.y, c='blue', marker='o')
            plt.text(client.x, client.y, f' {client.id}', fontsize=12)

        plt.xlabel('X coordinate')
        plt.ylabel('Y coordinate')
        plt.title('Initial State Visualization')
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_solution(self, solution):
        depot = self.problem.depot
        clients = self.problem.clients

        # Plot depot
        plt.scatter(depot.x, depot.y, c='red', marker='D', label='Depot')

        # Plot clients
        for client in clients:
            plt.scatter(client.x, client.y, c='blue', marker='o')
            plt.text(client.x, client.y, f' {client.id}', fontsize=12)

        # Plot routes
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        for idx, (vehicle, orders) in enumerate(solution.items()):
            route_x, route_y = [depot.x], [depot.y]
            for order in orders:
                if order.origin == self.problem.depot.id:
                    client = next((c for c in clients if c.id == order.destination), None)
                else:
                    client = next((c for c in clients if c.id == order.origin), None)
                if client:
                    route_x.append(client.x)
                    route_y.append(client.y)
            route_x.append(depot.x)
            route_y.append(depot.y)
            plt.plot(route_x, route_y, colors[idx % len(colors)], label=f'Vehicle {vehicle.id}')

        plt.xlabel('X coordinate')
        plt.ylabel('Y coordinate')
        plt.title('Solution Visualization')
        plt.legend()
        plt.grid(True)
        plt.show()
