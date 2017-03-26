import random

import constants
import action

#player.inventory

def field_of_view(e, p_x, p_y, r):
    notable_objects = []
    for y in range(-r, r):
        for x in range(-r, r):
            if (p_x + x >= 0) and (p_x + x < constants.GRID_WIDTH) and (p_y + y >= 0) and (p_y + y < constants.GRID_HEIGHT):
                if e.global_map[p_y + y][p_x + x].name != "grass":
                    notable_objects.append(e.global_map[p_y + y][p_x + x])

	return notable_objects

def random_walk(p, e, o):
    options = {}
    for i in range(len(o)):
        options[i] = o[i]
    
    keep = True
    choice = options[random.randint(0, len(o) - 1)]
    if choice == "walk_L":
        keep = e.global_map[p.x_coordinate - 1][p.y_coordinate].name == "grass"
    elif choice == "walk_R":
        keep = e.global_map[p.x_coordinate + 1][p.y_coordinate].name == "grass"
    elif choice == "walk_U":
        keep = e.global_map[p.x_coordinate][p.y_coordinate - 1].name == "grass"
    elif choice == "walk_D":
        keep = e.global_map[p.x_coordinate][p.y_coordinate + 1].name == "grass"
        
    while not keep:
        choice = options[random.randint(0, len(o) - 1)]
        if choice == "walk_L":
            keep = e.global_map[p.x_coordinate - 1][p.y_coordinate].name == "grass"
        elif choice == "walk_R":
            keep = e.global_map[p.x_coordinate + 1][p.y_coordinate].name == "grass"
        elif choice == "walk_U":
            keep = e.global_map[p.x_coordinate][p.y_coordinate - 1].name == "grass"
        elif choice == "walk_D":
            keep = e.global_map[p.x_coordinate][p.y_coordinate + 1].name == "grass"

    return choice

def search_obj(player, environment, fov, obj_name, final_action):
    current_action = "nothing"

    for fovIndex in range(len(fov)):
        if fov[fovIndex].name == obj_name:
            if fov[fovIndex].x_coordinate < player.x_coordinate - 1:
                if environment.global_map[player.x_coordinate - 1][player.y_coordinate].name != "grass":
                    current_action = random_walk(player, environment, ["walk_R", "walk_U", "walk_D"])
                else:
                    current_action = "walk_L"
            elif fov[fovIndex].x_coordinate > player.x_coordinate + 1:
                if environment.global_map[player.x_coordinate + 1][player.y_coordinate].name != "grass":
                    current_action = random_walk(player, environment, ["walk_L", "walk_U", "walk_D"])
                else:
                    current_action = "walk_R"				
            elif fov[fovIndex].y_coordinate < player.y_coordinate - 1:
                if environment.global_map[player.x_coordinate][player.y_coordinate - 1].name != "grass":
                    current_action = random_walk(player, environment, ["walk_L", "walk_R", "walk_D"])
                else:
                    current_action = "walk_U"				
            elif fov[fovIndex].y_coordinate > player.y_coordinate + 1:
                if environment.global_map[player.x_coordinate][player.y_coordinate + 1].name != "grass":
                    current_action = random_walk(player, environment, ["walk_L", "walk_R", "walk_U"])
                else:
                    current_action = "walk_D"				
            else:
                current_action = final_action
                
    return current_action
    
def process_thoughts(player, environment):
    
    fov = []
    fov = field_of_view(environment, player.x_coordinate, player.y_coordinate, constants.FOV_RADIUS)

    
    if player.current_action != "" and player.action_counter < constants.ACTION_TIME[player.current_action]:
    	return
        
    if player.hunger > constants.HUNGER_THRESHOLD:
        # for invIndex in player.inventory:
        # 	if player.inventory[invIndex].is_edible():
        # 		player.current_action = "eat"
        # 		return
        player.current_action = search_obj(player, environment, fov, "apple_tree", "eat")
    elif player.thirst > constants.THIRST_THRESHOLD:
        #for invIndex in player.inventory:
        #	if player.inventory[invIndex] is edible:
        #		#player.current_action = "eat"
        player.current_action = search_obj(player, environment, fov, "water", "drink")
    elif player.energy < constants.ENERGY_THRESHOLD: 
        player.current_action = "sleep"
    else: # Expore the world
        player.current_action = random_walk(player, environment, ["walk_R", "walk_U", "walk_D"])

    #skip if current thought count hasn't reached max

    #think about current thought

    #check field of view: make variable