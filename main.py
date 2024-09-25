import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Movable Tiny Knight")

# Colors
WHITE = (255, 255, 255)

# Knight settings
knight_speed = 3

# Load the knight images for idle (right and left)
knight_idle = pygame.image.load("knight_idle.png")
knight_idle_down = pygame.image.load("knight_idle_down.png")
knight_idle_left = pygame.image.load("knight_idle_left.png")
knight_idle_left_down = pygame.image.load("knight_idle_left_down.png")

# Load the knight images for movement
knight_move_1 = pygame.image.load("knight_move_1.png")
knight_move_2 = pygame.image.load("knight_move_2.png")
knight_move_3 = pygame.image.load("knight_move_3.png")
knight_move_left_1 = pygame.image.load("knight_move_left_1.png")
knight_move_left_2 = pygame.image.load("knight_move_left_2.png")
knight_move_left_3 = pygame.image.load("knight_move_left_3.png")

# Resize knight images (optional)
knight_idle = pygame.transform.scale(knight_idle, (30, 40))
knight_idle_down = pygame.transform.scale(knight_idle_down, (30, 40))
knight_idle_left = pygame.transform.scale(knight_idle_left, (30, 40))
knight_idle_left_down = pygame.transform.scale(knight_idle_left_down, (30, 40))

knight_move_1 = pygame.transform.scale(knight_move_1, (30, 40))
knight_move_2 = pygame.transform.scale(knight_move_2, (30, 40))
knight_move_3 = pygame.transform.scale(knight_move_3, (30, 40))
knight_move_left_1 = pygame.transform.scale(knight_move_left_1, (30, 40))
knight_move_left_2 = pygame.transform.scale(knight_move_left_2, (30, 40))
knight_move_left_3 = pygame.transform.scale(knight_move_left_3, (30, 40))

# Store idle and movement frames in lists
idle_right_frames = [knight_idle, knight_idle_down]
idle_left_frames = [knight_idle_left, knight_idle_left_down]

move_right_frames = [knight_move_1, knight_move_2, knight_move_3, knight_move_2]
move_left_frames = [knight_move_left_1, knight_move_left_2, knight_move_left_3, knight_move_left_2]

# Get knight's width and height based on the image size
knight_width, knight_height = knight_idle.get_size()

# Set knight's initial position
knight_x = screen_width // 2 - knight_width // 2
knight_y = screen_height // 2 - knight_height // 2

# Timer settings for animation
animation_timer = 0
animation_interval = 250  # Time in milliseconds to switch frames (faster for movement)
movement_animation_interval = 75  # Time in milliseconds to switch frames
current_frame = 0

# Movement flag
is_moving = False


# Game loop
running = True
current_direction = "right"

# Clock to manage frame rate and animation timing
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Get keys pressed
    keys = pygame.key.get_pressed()
    
    # Reset movement flag
    is_moving = False
    
    # Move knight and detect direction
    if keys[pygame.K_LEFT]:
        knight_x -= knight_speed
        current_direction = "left"
        is_moving = True
    if keys[pygame.K_RIGHT]:
        knight_x += knight_speed
        current_direction = "right"
        is_moving = True
    if keys[pygame.K_UP]:
        knight_y -= knight_speed
        is_moving = True
    if keys[pygame.K_DOWN]:
        knight_y += knight_speed
        is_moving = True
    
    # Diagonal movement slowed down
    kds = knight_speed - 4
    if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        knight_x -= kds
        knight_y += kds
        current_direction = "left"
        is_moving = True
    if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        knight_x += kds
        knight_y += kds
        current_direction = "right"
        is_moving = True
    if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        knight_x -= kds
        knight_y -= kds
        current_direction = "left"
        is_moving = True
    if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        knight_x += kds
        knight_y -= kds
        current_direction = "right"
        is_moving = True
    
    # Handle animation switching
    current_time = pygame.time.get_ticks()
    
   # Use different intervals for movement and idle animations
    if is_moving:
        if current_time - animation_timer > movement_animation_interval:
            current_frame = (current_frame + 1) % len(move_right_frames)  # Loop through the frames
            animation_timer = current_time
    else:
        if current_time - animation_timer > animation_interval:
            current_frame = (current_frame + 1) % 2  # Toggle between frame 0 and 1
            animation_timer = current_time
    
    # Choose which frames to display
    if is_moving:
        if current_direction == "left":
            screen.blit(move_left_frames[current_frame], (knight_x, knight_y))
        else:
            screen.blit(move_right_frames[current_frame], (knight_x, knight_y))
    else:
        if current_direction == "left":
            screen.blit(idle_left_frames[current_frame % 2], (knight_x, knight_y))
        else:
            screen.blit(idle_right_frames[current_frame % 2], (knight_x, knight_y))
    
    # Update the display
    pygame.display.flip()
    
    # Frame rate
    clock.tick(60)
