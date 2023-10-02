# Import necessary modules
import pygame
from graphical_mode import drawmaze as d
from config import configuration as c

# Class for calculating the performance of search algorithms
class Performance:
    def __init__(self, algorithm, problem):
        self.path = []
        self.c_path = 0
        self.expanded_nodes = 0
        self.problem = problem
        # Set the caption of the display window
        d.set_caption(algorithm)
        # Reset the screen by clearing the display and drawing the initial positions
        d.reset_screen(self.problem.maze, self.problem.goal_nodes_list)

    # Method to calculate the performance of the strategy
    def calculate_performance(self, path, expanded_node):

        self.path.append(path)
        self.expanded_nodes += expanded_node

    # Method to calculate the length of the path
    def len_path(self, path):
        count = 0
        for p in path:
            for t in p:
                count += 1
        return count

    # Method to show the performance of the strategy
    def show_performance(self, algorithm):
        print("Solution found:")
        self.c_path = self.len_path(self.path)
        pygame.image.save(d.display, "./"+c.DEFAULT_IMAGES_FOLDER+"/path"+str(hex(id(self.problem))+"_"+str(algorithm)) + ".jpg")
        print('Saved display as ', algorithm, ".jpg", sep="")
        print(algorithm, 'Algorithm path cost:', self.c_path, 'nodes')
        print(algorithm, 'Algorithm solution expanded_nodes:', self.expanded_nodes)
        print()
        pygame.display.update()
