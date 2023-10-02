# Import necessary modules
import random, non_graphical_mode.state_NG as st
from config import configuration as c


class Maze:
    def __init__(self):
        # Initialize maze properties
        self.state = st.Initial_State()
        self.root_node = None
        self.goal_node = None
        self.intermediate_nodes_goal = None
        self.goal_nodes_list = None
        self.maze = [[1 for _ in range(c.GRID_HEIGHT)] for _ in range(c.GRID_WIDTH)]

        # Function to backtrack and generate the maze
        def backtrack(x, y):
            self.maze[x][y] = 0

            random.shuffle(c.ACTIONS)

            for dx, dy in c.ACTIONS:
                nx, ny = x + dx * 2, y + dy * 2

                if 0 <= nx < c.GRID_WIDTH and 0 <= ny < c.GRID_HEIGHT and self.maze[nx][ny] == 1:
                    self.maze[x + dx][y + dy] = 0
                    self.maze[nx][ny] = 0
                    backtrack(nx, ny)

        # Generate the maze using backtrack algorithm
        start_x = random.randint(0, c.GRID_WIDTH // 2) * 2
        start_y = random.randint(0, c.GRID_HEIGHT // 2) * 2
        backtrack(start_x, start_y)

        # Find the starting position on "0" cell
        self.root_node = None
        for i in range(c.GRID_WIDTH):
            for j in range(c.GRID_HEIGHT):
                if self.maze[i][j] == 0:
                    self.root_node = (i, j)
                    break
            if self.root_node is not None:
                break

        # Find the goal_node position on a different "0" cell
        self.goal_node = None
        for i in range(c.GRID_WIDTH - 1, -1, -1):
            for j in range(c.GRID_HEIGHT - 1, -1, -1):
                if self.maze[i][j] == 0 and (i, j) != self.root_node:
                    self.goal_node = (i, j)
                    break
            if self.goal_node is not None:
                break

        # Find intermediate positions on "0" cells
        self.intermediate_nodes_goal = []
        for _ in range(c.NUM_INTERMEDIATE_POSITIONS):
            while True:
                x = random.randint(0, c.GRID_WIDTH - 1)
                y = random.randint(0, c.GRID_HEIGHT - 1)
                if self.maze[x][y] == 0 and (x, y) not in [self.root_node, self.goal_node] and (
                        x, y) not in self.intermediate_nodes_goal:
                    self.intermediate_nodes_goal.append((x, y))
                    break

        # Add additional paths
        for _ in range(c.NUM_ADDITIONAL_PATHS):
            while True:
                x = random.randint(0, c.GRID_WIDTH - 1)
                y = random.randint(0, c.GRID_HEIGHT - 1)
                if self.maze[x][y] == 1:
                    self.maze[x][y] = 0
                    break

        # Create the initial goal_nodes_list list of all states node
        self.goal_nodes_list = [self.root_node] + self.intermediate_nodes_goal + [self.goal_node]
        self.goal_nodes_list.sort()

        print("Maze is just generated... Let's start!")
        print("Maze Problem ID --->", hex(id(self)))
        print("All Goal Nodes ->", self.goal_nodes_list)
        print()

    # Function to process input variables using the State Design Pattern
    def process_input(self, strategy, node):
        return self.state.process_input(self, strategy, node)

    # Function to set the current state
    def set_state(self, new_state):
        self.state = new_state

    # Function to get the current state
    def get_state(self):
        return self.state

    # Function to verify if the current state is the Goal State
    def is_goal_state(self):
        return self.state.__class__.__name__ == st.Goal_State().__class__.__name__
