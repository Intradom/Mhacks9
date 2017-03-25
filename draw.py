import pygame

import constants

def draw_environment(screen, x):
    pygame.draw.circle(screen, constants.C_BLACK, (x, constants.SCREEN_HEIGHT / 2), 100, 1)
    
def draw_players(screen):
    pass
    
def draw_tools(screen):
    pass

def process_draws(screen, x):
    # Clear screen
    screen.fill(constants.C_WHITE)
    
    draw_environment(screen, x)
    draw_players(screen)
    draw_tools(screen)
    
    pygame.display.update()