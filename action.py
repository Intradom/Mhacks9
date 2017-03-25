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

def process_actions(person, environment):
    #Increment action counter
    person.action_counter += 1

    x = person.x_coordinate
    y = person.y_coordinate

    if person.current_action == "walk_U":

        #Reset current location to grass
        environment.global_map[x][y] = Thing("grass", x, y)

        #Move up
        person.y_coordinate += 1

        #Set new location
        environment.global_map[x][y+1] = person

    elif person.current_action == "walk_D":

        #Reset current location to grass
        environment.global_map[x][y] = Thing("grass", x, y)

        #Move down
        person.y_coordinate -= 1

        #Set new location
        environment.global_map[x][y-1] = person

    elif person.current_action == "walk_L":

        #Reset current location to grass
        environment.global_map[x][y] = Thing("grass", x, y)

        #Move left
        person.x_coordinate -= 1

        #Set new location
        environment.global_map[x-1][y] = person

    elif person.current_action == "walk_R":

        #Reset current location to grass
        environment.global_map[x][y] = Thing("grass", x, y)

        #Move right
        person.x_coordinate += 1

        #Set new location
        environment.global_map[x+1][y] = person

    elif person.current_action == "sleep":
        pass

    elif person.current_action == "eat":
        pass

    elif person.current_action == "drink":
        pass