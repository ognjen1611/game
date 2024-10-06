import pygame

class Knight:
    def __init__(self, screen_width, screen_height):
        # Load the knight images for idle (right and left)
        self.knight_idle = pygame.image.load("knight_idle.png")
        self.knight_idle_down = pygame.image.load("knight_idle_down.png")
        self.knight_idle_left = pygame.image.load("knight_idle_left.png")
        self.knight_idle_left_down = pygame.image.load("knight_idle_left_down.png")

        # Load the knight images for movement
        self.knight_move_1 = pygame.image.load("knight_move_1.png")
        self.knight_move_2 = pygame.image.load("knight_move_2.png")
        self.knight_move_3 = pygame.image.load("knight_move_3.png")
        self.knight_move_left_1 = pygame.image.load("knight_move_left_1.png")
        self.knight_move_left_2 = pygame.image.load("knight_move_left_2.png")
        self.knight_move_left_3 = pygame.image.load("knight_move_left_3.png")

        # Resize knight images (optional)
        self.knight_idle = pygame.transform.scale(self.knight_idle, (30, 40))
        self.knight_idle_down = pygame.transform.scale(self.knight_idle_down, (30, 40))
        self.knight_idle_left = pygame.transform.scale(self.knight_idle_left, (30, 40))
        self.knight_idle_left_down = pygame.transform.scale(self.knight_idle_left_down, (30, 40))

        self.knight_move_1 = pygame.transform.scale(self.knight_move_1, (30, 40))
        self.knight_move_2 = pygame.transform.scale(self.knight_move_2, (30, 40))
        self.knight_move_3 = pygame.transform.scale(self.knight_move_3, (30, 40))
        self.knight_move_left_1 = pygame.transform.scale(self.knight_move_left_1, (30, 40))
        self.knight_move_left_2 = pygame.transform.scale(self.knight_move_left_2, (30, 40))
        self.knight_move_left_3 = pygame.transform.scale(self.knight_move_left_3, (30, 40))

        # Store idle and movement frames in lists
        self.idle_right_frames = [self.knight_idle, self.knight_idle_down]
        self.idle_left_frames = [self.knight_idle_left, self.knight_idle_left_down]

        self.move_right_frames = [self.knight_move_1, self.knight_move_2, self.knight_move_3, self.knight_move_2]
        self.move_left_frames = [self.knight_move_left_1, self.knight_move_left_2, self.knight_move_left_3, self.knight_move_left_2]

        # Get knight's width and height based on the image size
        self.knight_width, self.knight_height = self.knight_idle.get_size()

        #Position the knight on the screen
        self.knight_x = screen_width // 2 - self.knight_width // 2
        self.knight_y = screen_height // 2 - self.knight_height // 2

        # Camera position for infinite scrolling
        self.camera_x = 0
        self.camera_y = 0

        # Timer settings for animation
        self.animation_timer = 0
        self.animation_interval = 250  # Time in milliseconds to switch frames (faster for movement)
        self.movement_animation_interval = 75  # Time in milliseconds to switch frames
        self.current_frame = 0

        self.knight_speed = 3
        self.current_direction = "right"
        self.is_moving = False

        # Create a rect for the knight for collision detection
        self.rect = pygame.Rect(self.knight_x, self.knight_y, self.knight_width, self.knight_height)


    def move(self, keys, tree_rect):
        # Reset movement flag
        self.is_moving = False

        # Calculate potential new position
        old_x, old_y = self.knight_x, self.knight_y

        # Move knight and detect direction
        if keys[pygame.K_LEFT]:
            self.knight_x -= self.knight_speed
            self.camera_x -= self.knight_speed
            self.current_direction = "left"
            self.is_moving = True
        if keys[pygame.K_RIGHT]:
            self.knight_x += self.knight_speed
            self.camera_x += self.knight_speed
            self.current_direction = "right"
            self.is_moving = True
        if keys[pygame.K_UP]:
            self.knight_y -= self.knight_speed
            self.camera_y -= self.knight_speed
            self.is_moving = True
        if keys[pygame.K_DOWN]:
            self.knight_y += self.knight_speed
            self.camera_y += self.knight_speed
            self.is_moving = True

        # Diagonal movement adjustment
        kds = self.knight_speed - 4
        if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            self.knight_x -= kds
            self.knight_y += kds
            self.camera_x -= kds
            self.camera_y += kds
            self.current_direction = "left"
            self.is_moving = True
        if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            self.knight_x += kds
            self.knight_y += kds
            self.camera_x += kds
            self.camera_y += kds
            self.current_direction = "right"
            self.is_moving = True
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            self.knight_x -= kds
            self.knight_y -= kds
            self.camera_x -= kds
            self.camera_y -= kds
            self.current_direction = "left"
            self.is_moving = True
        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            self.knight_x += kds
            self.knight_y -= kds
            self.camera_x += kds
            self.camera_y -= kds
            self.current_direction = "right"
            self.is_moving = True

        # Update knight's rect position
        self.rect.topleft = (self.knight_x, self.knight_y)

        # Check for collision with the tree
        if self.rect.colliderect(tree_rect):
            self.knight_x, self.knight_y = old_x, old_y
            self.rect.topleft = (self.knight_x, self.knight_y)

    def handleAnimation(self, screen):
        # Handle animation switching
        self.current_time = pygame.time.get_ticks()

        # Use different intervals for movement and idle animations
        if self.is_moving:
            if self.current_time - self.animation_timer > self.movement_animation_interval:
                self.current_frame = (self.current_frame + 1) % len(self.move_right_frames)  # Loop through the frames
                self.animation_timer = self.current_time
        else:
            if self.current_time - self.animation_timer > self.animation_interval:
                self.current_frame = (self.current_frame + 1) % 2  # Toggle between frame 0 and 1
                self.animation_timer = self.current_time

        # Choose which frames to display
        if self.is_moving:
            if self.current_direction == "left":
                screen.blit(self.move_left_frames[self.current_frame], (self.knight_x - self.camera_x, self.knight_y - self.camera_y))
            else:
                screen.blit(self.move_right_frames[self.current_frame], (self.knight_x - self.camera_x, self.knight_y - self.camera_y))
        else:
            if self.current_direction == "left":
                screen.blit(self.idle_left_frames[self.current_frame % 2], (self.knight_x - self.camera_x, self.knight_y - self.camera_y))
            else:
                screen.blit(self.idle_right_frames[self.current_frame % 2], (self.knight_x - self.camera_x, self.knight_y - self.camera_y))
