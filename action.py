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

def find_food(x, y, person, environment):
    #Check left
    if person.x_coordinate != 0:
        if environment.global_map[x-1][y].name == "apple_tree":
            return "left"
    #Check right
    if person.x_coordinate != (constants.GRID_WIDTH - 1):
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
        return

    x = person.x_coordinate
    y = person.y_coordinate

    if person.current_action == "walk_U" or person.current_action == "run_U":

        if person.energy <= constants.ENERGY_THRESHOLD:
            person.current_action = "walk_U"
    
        #Reset current location to grass
        environment.global_map[x][y] = classes.Thing("grass", x, y, 0)

        #Move up
        person.y_coordinate -= 1

        #Set new location
        environment.global_map[x][y-1] = person
        
        if person.current_action == "walk_U":
            print("\t" + person.name + " walked upwards")
        else:
            print("\t" + person.name + " ran upwards")

    elif person.current_action == "walk_D" or person.current_action == "run_D":

        if person.energy <= constants.ENERGY_THRESHOLD:
            person.current_action = "walk_D"
    
        #Reset current location to grass
        environment.global_map[x][y] = classes.Thing("grass", x, y, 0)

        #Move down
        person.y_coordinate += 1

        #Set new location
        environment.global_map[x][y+1] = person
        
        if person.current_action == "walk_D":
            print("\t" + person.name + " walked downwards")
        else:
            print("\t" + person.name + " ran downwards")
    elif person.current_action == "walk_L" or person.current_action == "run_L":

        if person.energy <= constants.ENERGY_THRESHOLD:
            person.current_action = "walk_L"
    
        #Reset current location to grass
        environment.global_map[x][y] = classes.Thing("grass", x, y, 0)

        #Move left
        person.x_coordinate -= 1

        #Set new location
        environment.global_map[x-1][y] = person
        
        if person.current_action == "walk_L":
            print("\t" + person.name + " walked to the left")
        else:
            print("\t" + person.name + " ran to the left")
    elif person.current_action == "walk_R" or person.current_action == "run_R":

        if person.energy <= constants.ENERGY_THRESHOLD:
            person.current_action = "walk_R"
    
        #Reset current location to grass
        environment.global_map[x][y] = classes.Thing("grass", x, y, 0)

        #Move right
        person.x_coordinate += 1

        #Set new location
        environment.global_map[x+1][y] = person
        
        if person.current_action == "walk_R":
            print("\t" + person.name + " walked to the right")
        else:
            print("\t" + person.name + " ran to the right")
    elif person.current_action == "sleep":
        print("\t" + person.name + " slept")

    elif person.current_action == "eat":
        #Get location of food
        food_loc = find_food(x, y, person, environment)
        if food_loc == "left":
            environment.global_map[x-1][y].resources -= 1
        elif food_loc == "right":
            environment.global_map[x+1][y].resources -= 1
        elif food_loc == "up":
            environment.global_map[x][y+1].resources -= 1
        else:
            environment.global_map[x][y-1].resources -= 1
        print("\t" + person.name + " ate")

    elif person.current_action == "drink":
        print("\t" + person.name + " drank water")
    elif person.current_action == "sleep":
        print("\t" + person.name + " slept")
    elif person.current_action == "dance":
        if person.energy <= constants.ENERGY_THRESHOLD:
            print("\t" + person.name + " is too tired to dance")
            person.current_action = ""
        else:
            print("\t" + person.name + " danced")
    elif person.current_action == "pushup":
        if person.energy <= constants.ENERGY_THRESHOLD:
            print("\t" + person.name + " is too tired to do push-ups")
            person.current_action = ""
        else:
            print("\t" + person.name + " did push-ups")
    elif person.current_action == "pee":
        print("\t" + person.name + " peed on the ground")
    elif person.current_action == "poo":
        print("\t" + person.name + " took a dump")
    