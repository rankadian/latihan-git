import pygame
import time 
import random

snake_speed = 15

# Window size
window_x = 720
window_y = 480

# Defining color
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialising game window
pygame.display.set_caption('PYSanke')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (Frame Per Second) Controller
fps = pygame.time.lock()

# Defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# Fruit position 
fruit_position = [random.randrange(start: 1, (window_x // 10)) * 10,
                  random.randrange(start: 1, (window_y // 10)) * 10]

fruit_spawn = True

# Setting default snake direction towards
# Right
direction = 'RIGHT'
change to = direction