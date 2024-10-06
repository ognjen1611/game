import pygame
import random

class Tree:
    def __init__(self, screen_width, screen_height):
        # Load the tree image and store its dimensions
        self.image = pygame.image.load("textures/tree_1.png")
        self.image = pygame.transform.scale(self.image, (170, 180))
        self.width, self.height = self.image.get_size()

        # Randomly place the tree within the screen boundaries
        self.tree_x = random.randint(0, screen_width - self.width)
        self.tree_y = random.randint(0, screen_height - self.height)

        # Create a rect for the tree for collision detection
        self.rect = pygame.Rect(self.tree_x, self.tree_y, self.width, self.height)

    def draw(self, screen, camera_x, camera_y):
        # Draw the tree image on the screen, adjusting for camera movement
        screen.blit(self.image, (self.tree_x - camera_x, self.tree_y - camera_y))
