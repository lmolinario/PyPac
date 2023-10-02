import pygame
from non_graphical_mode import drawmaze_NG as d
from config import configuration as c

class Performance:
    def __init__(self, algorithm, problem):
        self.path = []
        self.c_path = 0
        self.expanded_nodes = 0
        self.problem=problem
        # Set the caption of the display window
        d.set_caption(algorithm)
        # Reset the screen by clearing the display and drawing the initial positions
        d.reset_screen(self.problem.maze, self.problem.goal_nodes_list)

    # Function to calculate Strategy performance
    def calculate_performance(self, path, depth):

        self.path.append(path)
        self.expanded_nodes += depth

    # Function to calculate path lenght
    def len_path(self, path):
        count = 0
        for p in path:
            for t in p:
                count += 1
        return count

    # Function to show Strategy Performance
    def show_performance(self, algorithm):
        print("Solution found:")
        self.c_path = self.len_path(self.path)
        pygame.image.save(d.display, "./"+c.DEFAULT_IMAGES_FOLDER+"/path"+str(hex(id(self.problem))+"_"+str(algorithm)) + ".jpg")
        print('Saved display as ', algorithm, ".jpg", sep="")
        print(algorithm, 'Algorithm path cost:', self.c_path, 'nodes')
        print(algorithm, 'Algorithm solution expanded_nodes:', self.expanded_nodes)
        print()
        pygame.display.update()
