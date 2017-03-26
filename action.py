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

def find_food(person, environment):
    #Check left
    if person.x_coordinate != 0:
        if environment.global_map[x-1][y].name == "apple_tree":
            return "left"
    #Check right
    if person.x_coordinate != (GRID_WIDTH - 1):
        if environment.global_map[x+1][y].name == "apple_tree":
            return "right"
    #Check up
    if person.y_coordinate != 0:
        if environment.global_map[x][y-1] == "apple_tree":
            return "up"
    else:
        return "down"


def process_actions(person, environment):
    
    if person.action_counter != 0:
        person.action_counter += 1
        return
        
    #Increment action counter
    person.action_counter += 1

    x = person.x_coordinate
    y = person.y_coordinate

    if person.current_action == "walk_U":

        #Reset current location to grass
        environment.global_map[x][y] = classes.Thing("grass", x, y, 0)

        #Move up
        person.y_coordinate += 1

        #Set new location
        environment.global_map[x][y+1] = person

    elif person.current_action == "walk_D":

        #Reset current location to grass
        environment.global_map[x][y] = classes.Thing("grass", x, y, 0)

        #Move down
        person.y_coordinate -= 1

        #Set new location
        environment.global_map[x][y-1] = person

    elif person.current_action == "walk_L":

        #Reset current location to grass
        environment.global_map[x][y] = classes.Thing("grass", x, y, 0)

        #Move left
        person.x_coordinate -= 1

        #Set new location
        environment.global_map[x-1][y] = person

    elif person.current_action == "walk_R":

        #Reset current location to grass
        environment.global_map[x][y] = classes.Thing("grass", x, y, 0)

        #Move right
        person.x_coordinate += 1

        #Set new location
        environment.global_map[x+1][y] = person

    elif person.current_action == "sleep":
        pass

    elif person.current_action == "eat":
        #Get location of food
        food_loc = find_food(person, environment)
        if food_loc == "left":
            environment.global_map[x-1][y].resources -= 1
        elif food_loc == "right":
            environment.global_map[x+1][y].resources -= 1
        elif food_loc == "up":
            environment.global_map[x][y+1].resources -= 1
        else:
            environment.global_map[x][y-1].resources -= 1

    elif person.current_action == "drink":
        pass