# Import necessary modules
import time
import pygame
from config import configuration as c

# Initialize pygame
pygame.init()

# Set up the display
display = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("Pathfinding Visualization")

# Initialize the music player
pygame.mixer.init()

# Load and play the MP3 song in a loop
pygame.mixer.music.load("./miscellaneous/Pac-Man.mp3")
pygame.mixer.music.play(-1)


# Function to set the caption of the window
def set_caption(algorithm):
    pygame.display.set_caption(
        "Pathfinding Visualization: \"" + algorithm + "\". Number of Ghosts: "
        + str(c.NUM_INTERMEDIATE_POSITIONS) + ". Number of alternative paths in the 1st_implementation_maze: "
        + str(c.NUM_ADDITIONAL_PATHS)
    )


# Function to draw the maze on the display
def draw_maze(maze):
    for i in range(c.GRID_WIDTH):
        for j in range(c.GRID_HEIGHT):
            rect = pygame.Rect(i * c.CELL_SIZE, j * c.CELL_SIZE, c.CELL_SIZE, c.CELL_SIZE)
            pygame.draw.rect(display, c.WHITE, rect, 1)
            if maze[i][j] == 1:
                pygame.draw.rect(display, c.BLUE, rect)


# Function to draw Pacman at the given position
def draw_pacman(coordinates):
    x = coordinates[0] * c.CELL_SIZE
    y = coordinates[1] * c.CELL_SIZE
    image_path = "./miscellaneous/pacman.png"  # Replace "pacman.png" with the path to your Pacman image file
    image = pygame.image.load(image_path)
    display.blit(image, (x, y))


# Function to draw a ghost at the given position
def draw_ghost(coordinates):
    x = coordinates[0] * c.CELL_SIZE
    y = coordinates[1] * c.CELL_SIZE
    image_path = "./miscellaneous/ghost.png"  # Replace "ghost.png" with the path to your ghost image file
    image = pygame.image.load(image_path)
    display.blit(image, (x, y))


# Function to draw a position with the specified color
def draw_pos(coordinates, color):
    x = coordinates[0] * c.CELL_SIZE + c.CELL_SIZE // 2
    y = coordinates[1] * c.CELL_SIZE + c.CELL_SIZE // 2
    pygame.draw.circle(display, color, (x, y), c.CELL_SIZE // 3)
    pygame.draw.circle(display, c.BLACK, (x, y), c.CELL_SIZE // 6)


# Function to draw a path on the display with the specified color
def draw_path(path):
    for nodes in path:
        x = nodes[0] * c.CELL_SIZE + c.CELL_SIZE // 2
        y = nodes[1] * c.CELL_SIZE + c.CELL_SIZE // 2
        pygame.draw.circle(display, c.RED, (x, y), c.CELL_SIZE // 6)


# Function to reset the screen and draw the maze, goal positions, and ghosts
def reset_screen(maze, goal_state_list):
    # Clear the display and draw the grid
    display.fill(c.BLACK)
    draw_maze(maze)

    # Draw goal positions in red and green
    draw_pos(goal_state_list[0], c.RED)
    draw_pos(goal_state_list[-1], c.GREEN)

    # Draw ghosts at intermediate positions
    for position in goal_state_list[1:-2]:
        draw_ghost(position)

    # Save the current display as an image
    pygame.image.save(display, "./"+c.DEFAULT_IMAGES_FOLDER+"/maze"+str(hex(id(maze)))+".jpg")


# Function to draw the partial path step by step with animation
def draw_partial_path(partial_path):
    for p in partial_path:
        draw_pacman(p)
        draw_path(partial_path)
        pygame.display.update()
        time.sleep(0.03)
