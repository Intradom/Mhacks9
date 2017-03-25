import constants
import action

#player.inventory

def field_of_view(e, p_x, p_y, r):
	notable_objects = []
	for y in range(-r, r):
		for x in range(-r, r):
			if e.global_map[p_y + y][p_x + x].name != "grass":
				notable_objects.append(e.global_map[p_y + y][p_x + x])

	return notable_objects



def process_thoughts(player, environment):
    
    fov = []
    fov = field_of_view(environment, player.x_coordinate, player.y_coordinate, constants.FOV_RADIUS)

    if player.action_counter < constants.ACTION_TIME[player.current_action]:
    	return

	if player.hunger > constants.HUNGER_THRESHOLD:
		# for invIndex in player.inventory:
		# 	if player.inventory[invIndex].is_edible():
		# 		player.current_action = "eat"
		# 		return
		
		for fovIndex in range(len(fov)):
			if fov[fovIndex].name = "apple_tree"
				if fov[fovIndex].x_coordinate < player.x_coordinate - 1:
					player.current_action = "walk_L"
				elif fov[fovIndex].x_coordinate > player.x_coordinate + 1:
					player.current_action = "walk_R"
				elif fov[fovIndex].y_coordinate < player.y_coordinate - 1:
					player.current_action = "walk_U"
				elif fov[fovIndex].y_coordinate > player.y_coordinate + 1:
					player.current_action = "walk_D"
				else:
					player.current_action = "eat"






	elif player.thirst > constants.THIRST_THRESHOLD:
		for invIndex in player.inventory:
			#if player.inventory[invIndex] is edible:
				#player.current_action = "eat"

	elif player.energy < ENERGY_THRESHOLD: 
		player.current_action = "sleep"

    #skip if current thought count hasn't reached max

    #think about current thought

    #check field of view: make variable

    #think about exploring








    #think about eating
    #think about drinking


