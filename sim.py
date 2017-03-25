import sys
import pygame

# User files
import constants
import environment
import thought
import action
import reaction
import draw

def init():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

def main(args=None):
    init()
    while True:
        # Check if user pressed the close button on pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # TODO: Make loop that iterates these functions for each character alive
        # Updates the environment with random events and returns items to interest to the players
        environment.process_environment()
        
        # Based on previous thoughts, mental states, and the new environment; generate actions plan
        thought.process_thoughts()
        
        # Based on action plan, execute actions plan
        action.process_actions()
        
        # Based on action plan, update how psychological state changes
        reaction.process_reactions()
        
        # Draw all out the environment, players, and tools aquired
        draw.process_draws()
        
        pygame.time.delay(constants.CYCLE_DELAY)

if __name__ == "__main__":
    main()