
class InitialSolution:
    def __init__(self, construction_strategy):
        self.construction_strategy = construction_strategy

    def generate_solution(self):
        return self.construction_strategy.generate_solution()


