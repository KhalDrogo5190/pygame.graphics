# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (1300, 700)
TITLE = "GBA Pokémon Fire Red"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

#Functions
def screen_glitch():
    for i in range(500):
        x = random.randrange(455,851)
        y = random.randrange(180,521)
        r = random.randrange(1,10)
        pygame.draw.ellipse(screen, BLACK, [x, y, r, r])
def color_change():
    pygame.draw.rect(screen, GREEN, [450, 175, 400, 350])
def draw_body():
    pygame.draw.rect(screen, PURPLE, [400, 100, 500, 500])
    pygame.draw.rect(screen, PURPLE, [375, 112.5, 550, 475])
    pygame.draw.rect(screen, PURPLE, [200, 150, 900, 400])
    pygame.draw.rect(screen, PURPLE, [175, 175, 950, 350])
    pygame.draw.rect(screen, PURPLE, [250, 125, 800, 450])
    pygame.draw.rect(screen, RED, [450, 75, 400, 25])
    
def draw_buttons():
    pygame.draw.rect(screen, GRAY, [275, 225, 30, 120])
    pygame.draw.rect(screen, GRAY, [230, 275, 120, 30])
    
    pygame.draw.rect(screen, GRAY, [380, 450 , 35, 35])
    pygame.draw.rect(screen, GRAY, [380, 500 , 35, 35])
    
    pygame.draw.rect(screen, GRAY, [928, 325, 30, 60])
    pygame.draw.rect(screen, GRAY, [912.5, 338, 60, 30])
    
    pygame.draw.rect(screen, GRAY, [1000, 250, 30, 60])
    pygame.draw.rect(screen, GRAY, [985, 267.5, 60, 30])
    
def draw_screen():
    pygame.draw.rect(screen, BLACK, [425, 125, 450, 450])
    pygame.draw.rect(screen, WHITE, [450, 175, 400, 350])
    
# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
YELLOW = (255,255,0)
DARK_GREEN = (4, 137, 19)
GRAY = (125, 124, 127)
PURPLE = (72, 56, 175)
BLACK = (0,0,0)

# Game loop
done = False
ticks = 0
glitch = True
while not done:
    
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Drawing code
    screen.fill(WHITE)

    draw_body()
    
    draw_screen()
   
    draw_buttons()
    
    ticks = (ticks+1)
    if ticks%6 == 0:
        color_change()
        screen_glitch()
        
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()

