import heapq
from config import configuration as c
from abc import ABC, abstractmethod


class Strategy(ABC):
    def __init__(self):
        self.visited = None
        self.frontier = None
        self.expanded_nodes = 0  # Counter variable to track the number of nodes expanded before a solution is found
        self.path = 0  # Variable to store the current path

    @abstractmethod
    def get_solution(self, maze, first_pos, last_pos):
        pass

    def _get_neighbors_nodes(self, maze, parent_pos):
        """
        Given an input position (identified by a pair of coordinates), it returns a list of valid adjacent
        positions along which Pacman can move, considering the list of possible actions from its position
        to its neighboring ones and iterating on these.
        This amounts to generating all the states (positions) reachable from a given state (parent position)
        for feasible actions.
        """
        neighbors = []
        for action in c.ACTIONS:
            neighbor = (parent_pos[0] + action[0], parent_pos[1] + action[1])
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] == 0:
                neighbors.append(neighbor)
        return neighbors

    def get_name(self):
        return self.__class__.__name__.upper()


class Informed_Strategy(Strategy):

    def get_solution(self, maze, first_pos, last_pos):
        pass

    def _heuristic(self, first_pos, last_pos):
        """
        It estimates the distance to the goal position by computing the Manhattan distance between two
        positions as heuristic.
        """
        return abs(first_pos[0] - last_pos[0]) + abs(first_pos[1] - last_pos[1])


class Uninformed_Strategy(Strategy):
    def get_solution(self, maze, first_pos, last_pos):
        pass


class DFS_Strategy(Uninformed_Strategy):

    def get_solution(self, maze, first_pos, last_pos):
        """
        Depth-First Search algorithm implementation.
        """
        self.visited = set()  # Set to keep track of visited positions
        self.frontier = [(first_pos, [])]  # Initialize a stack with the current position and an empty path

        while self.frontier:
            current_pos, self.path = self.frontier.pop() # Pop the last item from the stack

            if current_pos == last_pos: # Current goal position reached
                return self.path, self.expanded_nodes

            if current_pos not in self.visited:
                self.visited.add(current_pos)
                self.expanded_nodes += 1

                for neighbor in self._get_neighbors_nodes(maze, current_pos):
                    # Append each identified neighbor to the stack along with the updated path
                    self.frontier.append((neighbor, self.path + [neighbor]))

        return self.path, self.expanded_nodes


class BFS_Strategy(Uninformed_Strategy):

    def get_solution(self, maze, first_pos, last_pos):
        """
        Breadth-First Search algorithm implementation.
        """
        self.visited = set()  # Set to keep track of visited positions
        self.frontier = [(first_pos, [])]  # Initialize a queue with the current position and an empty path


        while self.frontier:
            current_pos, self.path = self.frontier.pop(0) # Pop the item from the front of the queue

            if current_pos == last_pos:
                return self.path, self.expanded_nodes

            if current_pos not in self.visited:
                self.visited.add(current_pos)
                self.expanded_nodes += 1

                for neighbor in self._get_neighbors_nodes(maze, current_pos):
                    # Append each identified neighbor to the queue along with the updated path
                    self.frontier.append((neighbor, self.path + [neighbor]))

        return self.path, self.expanded_nodes


class UCS_Strategy(Uninformed_Strategy):

    def get_solution(self, maze, first_pos, last_pos):
        """
        Uniform-Cost Search algorithm implementation.
        """
        self.visited = set()  # Set to keep track of visited positions
        self.frontier = [
            (0, first_pos, [])]  # Initialize a priority queue with the path cost, current position, and an empty path
        heapq.heapify(self.frontier)  # Transform a populated list into a heap

        while self.frontier:
            cost, current_pos, self.path = heapq.heappop(self.frontier)  # Pop the item with the lowest path cost

            if current_pos == last_pos:
                return self.path, self.expanded_nodes

            if current_pos not in self.visited:
                self.visited.add(current_pos)
                self.expanded_nodes += 1

                for i, neighbor in enumerate(self._get_neighbors_nodes(maze, current_pos)):
                    path_cost = cost + c.ACTION_COSTS[i]
                    # Push each identified neighbor into the priority queue along with the updated path and path cost
                    heapq.heappush(self.frontier, (path_cost, neighbor, self.path + [neighbor]))

        return self.path, self.expanded_nodes


class GREEDY_Strategy(Informed_Strategy):
    def get_solution(self, maze, first_pos, last_pos):
        """
        Greedy Best-First Search algorithm implementation.
        """
        self.visited = set()
        self.frontier = [(self._heuristic(first_pos, last_pos), first_pos, [])]
        heapq.heapify(self.frontier)  # Transform a populated list into a heap

        while self.frontier:
            _, current_pos, self.path = heapq.heappop(self.frontier) # Pop the item with the lowest heuristic value

            if current_pos == last_pos:
                return self.path, self.expanded_nodes

            if current_pos not in self.visited:
                self.visited.add(current_pos)
                self.expanded_nodes += 1

                for neighbor in self._get_neighbors_nodes(maze, current_pos):
                    # Push each identified neighbor into the priority queue along with updated path and heuristic
                    heapq.heappush(self.frontier,
                                   (self._heuristic(neighbor, last_pos), neighbor, self.path + [neighbor]))


        return self.path, self.expanded_nodes


class ASTAR_Strategy(Informed_Strategy):
    def get_solution(self, maze, first_pos, last_pos):
        """
        A* Search algorithm implementation.
        """
        self.visited = set()  # Set to keep track of visited positions
        self.frontier = [(self._heuristic(first_pos, last_pos), 0, first_pos, [])]  # Initialize a priority queue with
                                                                                    # the heuristic value, the path
                                                                                    # cost, the current position, and
                                                                                    # an empty path
        heapq.heapify(self.frontier)  # Transform a populated list into a heap

        while self.frontier:
            _, cost, current_pos, self.path = heapq.heappop(
                self.frontier)  # Pop the item with the lowest combination of the path cost and heuristic value

            if current_pos == last_pos:
                return self.path, self.expanded_nodes

            if current_pos not in self.visited: # Check on already visited positions to avoid repeated states
                self.visited.add(current_pos)
                self.expanded_nodes += 1

                neighbors = self._get_neighbors_nodes(maze, current_pos)  # Get neighbors of the current position

                for i, neighbor in enumerate(neighbors):
                    path_cost = cost + c.ACTION_COSTS[i]  # Calculate the new path cost

                    # Push each identified neighbor into the priority queue along with updated path, combination of
                    # heuristic and path cost, and path cost
                    heapq.heappush(self.frontier,
                                   (path_cost + self._heuristic(neighbor, last_pos), path_cost, neighbor,
                                    self.path + [neighbor]))

        return self.path, self.expanded_nodes

