import random
import math

import constants
import action

#player.inventory

def field_of_view(e, p_x, p_y, r):
    notable_objects = []
    
    for x in range(-r, r + 1):
        for y in range(-r, r + 1):
            if (p_x + x >= 0) and (p_x + x < constants.GRID_WIDTH) and (p_y + y >= 0) and (p_y + y < constants.GRID_HEIGHT):
                if e.global_map[p_x + x][p_y + y].name != "grass":
                    notable_objects.append(e.global_map[p_x + x][p_y + y])
    
    return notable_objects

def random_walk(p, e, o):
    options = {}
    for i in range(len(o)):
        options[i] = o[i]
    
    keep = False
    choice = options[random.randint(0, len(o) - 1)]
    if choice == "walk_L":
        keep = p.x_coordinate - 1 >= 0 and e.global_map[p.x_coordinate - 1][p.y_coordinate].name == "grass"
    elif choice == "walk_R":
        keep = p.x_coordinate + 1 < constants.GRID_WIDTH and e.global_map[p.x_coordinate + 1][p.y_coordinate].name == "grass"
    elif choice == "walk_U":
        keep = p.y_coordinate - 1 >= 0 and e.global_map[p.x_coordinate][p.y_coordinate - 1].name == "grass"
    elif choice == "walk_D":
        keep = p.y_coordinate + 1 < constants.GRID_HEIGHT and e.global_map[p.x_coordinate][p.y_coordinate + 1].name == "grass"
        
    while not keep:
        choice = options[random.randint(0, len(o) - 1)]
        if choice == "walk_L":
            keep = p.x_coordinate - 1 >= 0 and e.global_map[p.x_coordinate - 1][p.y_coordinate].name == "grass"
        elif choice == "walk_R":
            keep = p.x_coordinate + 1 < constants.GRID_WIDTH and e.global_map[p.x_coordinate + 1][p.y_coordinate].name == "grass"
        elif choice == "walk_U":
            keep = p.y_coordinate - 1 >= 0 and e.global_map[p.x_coordinate][p.y_coordinate - 1].name == "grass"
        elif choice == "walk_D":
            keep = p.y_coordinate + 1 < constants.GRID_HEIGHT and e.global_map[p.x_coordinate][p.y_coordinate + 1].name == "grass"

    return choice

def search_obj(player, environment, fov, obj_name, final_action):
    current_action = ""

    for fovIndex in range(len(fov)):
        if fov[fovIndex].name == obj_name:
            if abs(fov[fovIndex].x_coordinate - player.x_coordinate) + abs(fov[fovIndex].y_coordinate - player.y_coordinate) <= 1:
                current_action = final_action
            elif fov[fovIndex].x_coordinate < player.x_coordinate - 1:
                if player.x_coordinate - 1 >= 0 and environment.global_map[player.x_coordinate - 1][player.y_coordinate].name == "grass":
                    current_action = "walk_L"
                else:
                    current_action = random_walk(player, environment, ["walk_R", "walk_U", "walk_D"])
            elif fov[fovIndex].x_coordinate > player.x_coordinate + 1:
                if player.x_coordinate + 1 < constants.GRID_WIDTH and environment.global_map[player.x_coordinate + 1][player.y_coordinate].name == "grass":
                    current_action = "walk_R"
                else:
                    current_action = random_walk(player, environment, ["walk_L", "walk_U", "walk_D"])
            elif fov[fovIndex].y_coordinate < player.y_coordinate - 1:
                if player.y_coordinate - 1 >= 0 and environment.global_map[player.x_coordinate][player.y_coordinate - 1].name == "grass":
                    current_action = "walk_U"
                else:
                    current_action = random_walk(player, environment, ["walk_L", "walk_R", "walk_D"])				
            elif fov[fovIndex].y_coordinate > player.y_coordinate + 1:
                if player.y_coordinate + 1 < constants.GRID_HEIGHT and environment.global_map[player.x_coordinate][player.y_coordinate + 1].name == "grass":
                    current_action = "walk_D"
                else:
                    current_action = random_walk(player, environment, ["walk_L", "walk_R", "walk_U"])
            continue
                
    if current_action == "":
        current_action = random_walk(player, environment, ["walk_L", "walk_R", "walk_U", "walk_D"])
               
    return current_action
    
def process_thoughts(player, environment):
    
    fov = []
    fov = field_of_view(environment, player.x_coordinate, player.y_coordinate, constants.FOV_RADIUS)
    
    if player.action_counter < constants.ACTION_TIME[player.current_action]:
    	return
    player.action_counter = 0
        
    drink_low = 0
    drink_high = drink_low + math.exp(1.0 / player.intelligence * player.thirst)
    eat_low = drink_high
    eat_high = eat_low + math.exp(1.0 / player.intelligence * player.hunger)
    sleep_low = eat_high
    sleep_high = sleep_low + math.exp(1.0 / player.intelligence * (100 - player.energy))
    explore_low = sleep_high
    explore_high = explore_low + math.exp(1.0 / player.intelligence * player.energy) / (player.intelligence / 10.0)
    dance_low = explore_high
    dance_high = dance_low + math.exp(1.0 / player.intelligence * player.joy) / (player.intelligence / 10.0)
    pushup_low = dance_high
    pushup_high = pushup_low + math.exp(1.0 / player.intelligence * player.energy) / (player.intelligence / 10.0)
    pee_low = pushup_high
    pee_high = pee_low + math.exp(1.0 / player.intelligence * player.bladder)
    poo_low = pee_high
    poo_high = poo_low + math.exp(1.0 / player.intelligence * player.dump)
    donothing_low = poo_high
    donothing_high = donothing_low + (100 - player.intelligence) * 5 + (100 - player.energy)
    
    print(donothing_high)
    choice = random.randint(drink_low, int(donothing_high))
    
    if choice >= drink_low and choice < drink_high:
        player.current_action = search_obj(player, environment, fov, "water", "drink")
        print(player.name + " wants to drink water")
    elif choice >= eat_low and choice < eat_high:
        player.current_action = search_obj(player, environment, fov, "apple_tree", "eat")
        print(player.name + " wants to eat")
    elif choice >= sleep_low and choice < sleep_high:
        player.current_action = "sleep"
        print(player.name + " wants to sleep")
    elif choice >= explore_low and choice < explore_high:
        slow = random.randint(0, 2)
        if slow == 0:
            player.current_action = random_walk(player, environment, ["walk_L", "walk_R", "walk_U", "walk_D"])
        else:
            player.current_action = random_walk(player, environment, ["run_L", "run_R", "run_U", "run_D"])
        print(player.name + " wants to explore")
    elif choice >= dance_low and choice < dance_high:
        player.current_action = "dance"
        print(player.name + " wants to dance")
    elif choice >= pushup_low and choice < pushup_high:
        player.current_action = "pushup"
        print(player.name + " wants to do push-ups")
    elif choice >= pee_low and choice < pee_high:
        player.current_action = "pee"
        print(player.name + " wants to pee")
    elif choice >= poo_low and choice < poo_high:
        player.current_action = "poo"
        print(player.name + " wants to poo")
    else: # Do nothing
        player.current_action = ""
        print(player.name + " wants to do nothing")