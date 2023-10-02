# Import necessary modules
import random
import config.intro as i
import os

# Start INTRO
i.show_name()
i.show_authors()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 127, 0)

# Set up the maze dimensions
DEFAULT_WIDTH = 500
DEFAULT_HEIGHT = 500
DEFAULT_MAZE_INSTANCES = 1
CELL_SIZE = 20

# Define the name of the folder containing project-related images
DEFAULT_IMAGES_FOLDER = "graphs&diagrams"

# Define the possible legal Pacman actions (up, down, left, right)
ACTIONS = [(0, -1), (0, 1), (1, 0), (-1, 0)]

# Define the cost of each action or weight of nodes
ACTION_COSTS = [1, 1, 1, 1]

# Check if the folder exists
if os.path.exists(DEFAULT_IMAGES_FOLDER):
    # If it exists, delete its contents
    for filename in os.listdir(DEFAULT_IMAGES_FOLDER):
        file_path = os.path.join(DEFAULT_IMAGES_FOLDER, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    print(f"The contents of '{DEFAULT_IMAGES_FOLDER}' were deleted.")
else:
    # If it doesn't exist, create it
    os.mkdir(DEFAULT_IMAGES_FOLDER)
    print(f"The folder '{DEFAULT_IMAGES_FOLDER}' was created.")

# Get user input for the number of maze instances
input_str = input(
    f"Please enter how many maze problem instances you want to generate.\n"
    f"\t\t\tIf you do not enter anything, the following default parameters will be used: \t -->{DEFAULT_MAZE_INSTANCES}\n"
)

N_MAZE_INSTANCES = (int(input_str) if input_str else DEFAULT_MAZE_INSTANCES)

print(i.r, f"Maze problem instances => {N_MAZE_INSTANCES}\n", i.reset)

# Get user input for maze dimensions
input_str = input(
    f"Please enter the height and width in pixels of the maze, separated by a space.\n"
    f"\t\t\tIf you do not enter anything, the following default parameters will be used: \tHeight -->{DEFAULT_HEIGHT}\tWidth-->{DEFAULT_WIDTH}\n"
)

# Parse user input for maze dimensions
if input_str:
    dimensions = input_str.split()
    if len(dimensions) == 2:
        try:
            WIDTH = int(dimensions[1])
            HEIGHT = int(dimensions[0])
        except ValueError:
            print("Invalid input. Using default parameters.")
            WIDTH = DEFAULT_WIDTH
            HEIGHT = DEFAULT_HEIGHT
    else:
        print("Invalid input. Using default parameters.")
        WIDTH = DEFAULT_WIDTH
        HEIGHT = DEFAULT_HEIGHT
else:
    WIDTH = DEFAULT_WIDTH
    HEIGHT = DEFAULT_HEIGHT

print(i.r, f"Maze dimensions: Width = {WIDTH}, Height = {HEIGHT}\n", i.reset)

GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# General setup variables for maze generation
DEFAULT_NUM_INTERMEDIATE_POSITIONS = random.randint(7, 15)
input_str = input(
    f"Please enter the number of Ghosts.\n"
    f"\t\t\tIf you do not enter anything, the following default parameter will be used: \tGhosts -->{DEFAULT_NUM_INTERMEDIATE_POSITIONS}\n"
)

NUM_INTERMEDIATE_POSITIONS = (
    int(input_str) if input_str else DEFAULT_NUM_INTERMEDIATE_POSITIONS
)
print(i.r, f"Number of Ghosts = {NUM_INTERMEDIATE_POSITIONS}\n", i.reset)

DEFAULT_NUM_ADDITIONAL_PATHS = random.randint(30, 70)
input_str = input(
    f"Please enter the number of alternative paths to reach the end of the maze.\n"
    f"\t\t\tIf you do not enter anything, the following default parameter will be used: \tAlternative Paths -->{DEFAULT_NUM_ADDITIONAL_PATHS}\n"
)

NUM_ADDITIONAL_PATHS = (
    int(input_str) if input_str else DEFAULT_NUM_ADDITIONAL_PATHS
)
print(i.r, f"Number of alternative paths = {NUM_ADDITIONAL_PATHS}\n", i.reset)

i.show_logo_small()

