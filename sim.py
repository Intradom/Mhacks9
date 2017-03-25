import sys
import random
import pygame

# User files
import constants
import classes
import environment
import thought
import action
import reaction
import draw

def init():
    # Gather user input before launching
    p_name = raw_input("Player name: ")

    # Pygame init
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    # Random seed
    random.seed()
    
    # Environment init
    env = classes.Environment()
    env_to_add = ("reg_tree", "apple_tree", "water")
    for e_name in env_to_add:
        num_to_add = 0
        if e_name == "reg_tree":
            num_to_add = constants.E_NUM_REG_TREES
        elif e_name == "apple_tree":
            num_to_add = constants.E_NUM_APPLE_TREES
        elif e_name == "water":
            num_to_add = constants.E_NUM_WATER_SPOTS
        for i in range(num_to_add):
            loc_x = random.randint(0, constants.GRID_WIDTH - 1)
            loc_y = random.randint(0, constants.GRID_HEIGHT - 1)
            while env.global_map[loc_x][loc_y].name != "grass": # Keep searching for open tiles
                loc_x = random.randint(0, constants.GRID_WIDTH - 1)
                loc_y = random.randint(0, constants.GRID_HEIGHT - 1)
            env.change_tile(loc_x, loc_y, e_name)
            
    print(env)
    
    # TODO: add in more players
    # Players init
    p_x = random.randint(0, constants.GRID_WIDTH - 1)
    p_y = random.randint(0, constants.GRID_HEIGHT - 1)
    player = classes.Player(p_name, p_x, p_y, \
                            constants.P_HEALTH, constants.P_HUNGER, constants.P_THIRST, \
                            constants.P_ENERGY, constants.P_FITNESS, constants.P_ANGER, \
                            constants.P_FEAR, constants.P_GRIEF, constants.P_JOY, \
                            constants.P_INTELLIGENCE, constants.P_SOBRIETY, constants.P_BLADDER, \
                            constants.P_DUMP)
                                    
    return screen, env, player

def main(args=None):
    screen, env, player = init()
    cycles = 0
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
        draw.process_draws(screen, cycles)

        cycles += 1 # TODO: Add check for when cycles overflows 
        pygame.time.delay(constants.CYCLE_DELAY)

if __name__ == "__main__":
    main()