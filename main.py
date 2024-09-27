import pygame
import sys
from knight import Knight
from knight import Knight

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("Movable Tiny Knight")

# Create a Knight instance
knight = Knight(screen_width, screen_height)

# Load Terrain (Grassland image)
grassland = pygame.image.load("Grassland.png")

# Create a Knight instance
knight = Knight(screen_width, screen_height)

# Load Terrain (Grassland image)
grassland = pygame.image.load("Grassland.png")

# Colors
WHITE = (255, 255, 255)

# Clock to manage frame rate and animation timing
clock = pygame.time.Clock()

# Game loop
running = True

# Game loop
running = True

# Camera position for infinite scrolling
camera_x, camera_y = 0, 0

# Parallelogram parameters
parallelogram_width = 40  # Width of each parallelogram
parallelogram_height = 30  # Height of each parallelogram
slant_offset = 17  # Slant offset for the parallelogram

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move the knight based on keys
    knight.move(keys)
    
    # Clear the screen with the background color
    screen.fill(WHITE)

    # Tile the grassland image as the terrain (Greenland) across the screen
    grassland_width, grassland_height = grassland.get_size()

    # Draw the tiled grassland background based on the camera position
    for row in range(0, screen_height + grassland_height, grassland_height):
        for col in range(0, screen_width + grassland_width, grassland_width):
            screen.blit(grassland, (col - knight.camera_x % grassland_width, row - knight.camera_y % grassland_height))

    # Draw knight's animation on top of the background
    knight.handleAnimation(screen)


    # Move the knight based on keys
    knight.move(keys)
    

    # Clear the screen with the background color
    screen.fill(WHITE)

    # Tile the grassland image as the terrain (Greenland) across the screen
    grassland_width, grassland_height = grassland.get_size()

    # Draw the tiled grassland background based on the camera position
    for row in range(0, screen_height + grassland_height, grassland_height):
        for col in range(0, screen_width + grassland_width, grassland_width):
            screen.blit(grassland, (col - knight.camera_x % grassland_width, row - knight.camera_y % grassland_height))

    # Draw knight's animation on top of the background
    knight.handleAnimation(screen)

    # Update the display
    pygame.display.flip()


    # Frame rate
    clock.tick(60)
