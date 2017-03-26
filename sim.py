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
    p_intelligence = input(p_name + "'s intelligence (0-100, enter > 100 to use default): ")
    if p_intelligence > 100:
        p_intelligence = P_INTELLIGENCE

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
            env.change_tile(e_name, 0, loc_x, loc_y)
                
    # TODO: add in more players
    # Players init
    p_x = random.randint(0, constants.GRID_WIDTH - 1)
    p_y = random.randint(0, constants.GRID_HEIGHT - 1)
    while env.global_map[p_x][p_y].name != "grass": # Keep searching for open tiles
        p_x = random.randint(0, constants.GRID_WIDTH - 1)
        p_y = random.randint(0, constants.GRID_HEIGHT - 1)
    player = classes.Player(p_name, p_x, p_y, \
                            constants.P_HEALTH, constants.P_HUNGER, constants.P_THIRST, \
                            constants.P_ENERGY, constants.P_FITNESS, constants.P_ANGER, \
                            constants.P_FEAR, constants.P_GRIEF, constants.P_JOY, \
                            p_intelligence, constants.P_SOBRIETY, constants.P_BLADDER, \
                            constants.P_DUMP)

    env.change_tile(player.name, 0, player.x_coordinate, player.y_coordinate)

    return screen, env, player

def main(args=None):
    screen, env, player = init()
    cycles = 0
    while player.health > 0:
        # Check if user pressed the close button on pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if cycles % constants.CYCLES_IN_DAY == 0:
            print("**********DAY %d**********" % int(cycles / constants.CYCLES_IN_DAY + 1))
                
        # Updates the environment with random events and returns items to interest to the players
        environment.process_environment(env)
        
        # Based on previous thoughts, mental states, and the new environment; generate actions plan
        thought.process_thoughts(player, env)
        
        # Based on action plan, execute actions plan
        action.process_actions(player, env)
        
        # Based on action plan, update how psychological state changes
        reaction.process_reactions(player)
        
        # Draw all out the environment, players, and tools aquired
        draw.process_draws(screen, env)

        cycles += 1 # TODO: Add check for when cycles overflows 
        pygame.time.delay(constants.CYCLE_DELAY)
         
    print(player.name + " has died")
    pygame.quit()

if __name__ == "__main__":
    main()