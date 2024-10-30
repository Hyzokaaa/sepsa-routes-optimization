from src.io.data_reader import DataReader
from src.io.visualizer import Visualizer
from src.model.problem import Problem
from src.operators.initial_construction.initial_solution import InitialSolution
from src.operators.initial_construction.nearest_neighbor_strategy import NearestNeighborStrategy
from src.operators.initial_construction.random_strategy import RandomStrategy


def random_strategy():
    data_reader = DataReader('data/instance1-8-3-12')
    problem = data_reader.read_data()  # Ahora read_data devuelve un objeto Problem

    # Crear instancia de la estrategia de construcción aleatoria
    random_strategy = RandomStrategy(list(problem.vehicles.values()), problem.orders)

    # Crear instancia de InitialSolution con la estrategia aleatoria
    initial_solution = InitialSolution(random_strategy)

    # Generar la solución inicial
    solution = initial_solution.generate_solution()

    # Asignar la solución generada a los vehículos en el problema
    for veh_id, vehicle in problem.vehicles.items():
        vehicle.route = solution[veh_id]

    visualizer = Visualizer(problem)
    visualizer.plot_initial_state()
    visualizer.plot_solution(solution)

    # Mostrar la solución generada
    print("Initial solution:")
    for vehicle, assigned_orders in solution.items():
        print(f"Vehicle {vehicle}:")
        for order in assigned_orders:
            print(f"  {order}")

    # Verificar que las rutas no violen las restricciones de capacidad
    problem.verify_routes()


def nearest_neighbor():
    data_reader = DataReader('data/instance1-8-3-12')
    problem = data_reader.read_data()

    # Crear instancia de la estrategia de construcción de vecino más cercano
    nearest_neighbor_strategy = NearestNeighborStrategy(list(problem.vehicles.values()), problem.orders,
                                                        problem.clients, problem.depot)

    # Crear instancia de InitialSolution con la estrategia de vecino más cercano
    initial_solution = InitialSolution(nearest_neighbor_strategy)

    # Generar la solución inicial
    solution = initial_solution.generate_solution()

    # Asignar la solución generada a los vehículos en el problema
    for veh_id, vehicle in problem.vehicles.items():
        vehicle.route = solution[veh_id]

    visualizer = Visualizer(problem)
    visualizer.plot_initial_state()
    visualizer.plot_solution(solution)

    # Mostrar la solución generada
    print("Initial solution:")
    for vehicle, assigned_orders in solution.items():
        print(vehicle)
        for order in assigned_orders:
            print(f"  {order}")

    # Verificar que las rutas no violen las restricciones de capacidad
    problem.verify_routes()
    # Verificar si todas las órdenes fueron satisfechas
    satisfied_orders = [order for vehicle in problem.vehicles.values() for order in vehicle.route]
    if len(satisfied_orders) == len(problem.orders):
        print("All orders have been satisfied.")
    else:
        print(
            f"Not all orders have been satisfied. {len(problem.orders) - len(satisfied_orders)} orders are still unassigned.")


if __name__ == "__main__":
    random_strategy()



