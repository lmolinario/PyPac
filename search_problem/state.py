from abc import ABC, abstractmethod
from graphical_mode import drawmaze as d


# State Design Pattern ---> Problem State
class State(ABC):
    def __init__(self):

        self.algorithm_path = []
        self.successors = 0

    def process_input(self, problem, strategy, node):
        self.current_node = node
        self._action(problem, strategy)
        self._change_state(problem, strategy)
        return self.algorithm_path, self.successors

    def _fix_list(self):
        updated_list = []
        for item in self.algorithm_path:
            if isinstance(item, tuple):
                updated_list.append(item)
            else:
                updated_list.extend(item)
        self.algorithm_path = updated_list

    # The method is delegated to perform the action associated with the process input
    @abstractmethod
    def _action(self, problem, strategy):
        pass

    # The method is delegated to change the state
    @abstractmethod
    def _change_state(self, problem, strategy):
        pass

    # Find the path that Pacman traverses to reach the target positions, based on the specified algorithm (strategy)
    def _run_algorithm(self, problem, strategy):
        pos = problem.goal_nodes_list.index(self.current_node)
        algorithm_path,  successors_tmp = self._measure_performance(problem, problem.goal_nodes_list[pos],
                                                                             problem.goal_nodes_list[pos + 1],
                                                                             strategy)

        self.algorithm_path.append(algorithm_path)
        self.successors += successors_tmp

    # Measure the performance of the given search algorithm
    def _measure_performance(self, problem, first_node, last_node, strategy):

        # Find the path and number of maze cells visited using the specified algorithm
        path, expanded_nodes = strategy.get_solution(problem.maze, first_node, last_node)

        return path, expanded_nodes

class Initial_State(State):
    def _action(self, problem, strategy):
        if self.current_node == problem.goal_nodes_list[0]:
            print("Algorithm selected ->", strategy.get_name())
            print("Initial State -> Action")
            print("Root Node ->", self.current_node)
            d.draw_pacman(problem.goal_nodes_list[0])
            self._run_algorithm(problem, strategy)
        else:
            pass
        self._fix_list()
        d.draw_partial_path(self.algorithm_path)

    def _change_state(self, problem, strategy):
        if self.current_node == problem.goal_nodes_list[0]:
            print("Change State -> Let's go to Intermediate State")
            problem.set_state(Intermediate_State())

class Intermediate_State(State):
    def _action(self, problem, strategy):
        if self.current_node in problem.goal_nodes_list[1:-2]:
            print("Intermediate State -> Action")
            print("Intermediate Goal Node ->", self.current_node)
            print("Pacman is going to eat all ghosts... He's going fast!!!")
            self._run_algorithm(problem, strategy)
        else:
            pass
        if self.current_node == problem.goal_nodes_list[-3]:
            self._fix_list()
            d.draw_partial_path(self.algorithm_path)
        else:
            pass

    def _change_state(self, problem, strategy):
        if self.current_node == problem.goal_nodes_list[-3]:
            print("Change State -> Goal State ")
            problem.set_state(Goal_State())

class Goal_State(State):
    def _action(self, problem, strategy):
        if self.current_node == problem.goal_nodes_list[-2]:
            print("Goal State -> Action")
            print("Pacman is going to take the Exit...")
            self._run_algorithm(problem, strategy)
        else:
            pass
        self._fix_list()
        d.draw_partial_path(self.algorithm_path)

    def _change_state(self, problem, strategy):
        if self.current_node == problem.goal_nodes_list[-1]:
            print("Now we are in Goal Node!!!")
            print("Pacman has just eaten all the Ghosts!!! WOW!")
            problem.set_state(Initial_State())
        else:
            pass
