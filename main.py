from src.io.data_reader import DataReader
from src.model.problem import RoutingProblem
from src.operators.initial_construction.initial_solution import InitialSolution
from src.operators.initial_construction.random_solution_strategy import RandomConstructionStrategy


def main():
    data_reader = DataReader('data/instance1-8-3-12')
    depot, vehicles, orders, clients = data_reader.read_data()

    # Crear instancia de la estrategia de construcción aleatoria
    random_strategy = RandomConstructionStrategy(vehicles, orders)

    # Crear instancia de InitialSolution con la estrategia aleatoria
    initial_solution = InitialSolution(random_strategy)

    # Generar la solución inicial
    solution = initial_solution.generate_solution()

    # Crear una instancia del problema de ruteo
    problem = RoutingProblem(depot, vehicles, orders, clients)

    # Asignar la solución generada a los vehículos en el problema
    for veh_id, vehicle in problem.vehicles.items():
        vehicle.route = solution[veh_id]

    # Mostrar la solución generada
    print("Initial solution:")
    for vehicle, assigned_orders in solution.items():
        print(f"Vehicle {vehicle}:")
        for order in assigned_orders:
            print(f"  {order}")

    # Verificar que las rutas no violen las restricciones de capacidad
    valid = problem.verify_routes()




if __name__ == "__main__":
    main()
