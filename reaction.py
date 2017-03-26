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

def process_reactions(person):
    # Constant hunger
    if person.current_action != "eat":
        if person.hunger > 95:
            person.hunger = 100
            print(person.name + " is very hungry")
        else:
            person.hunger += 5
            if person.hunger >= 50:
                print(person.name + " is hungry")
        
    # Constant thirst
    if person.current_action != "drink":
        if person.thirst > 95:
            person.thirst = 100
            print(person.name + " is very thirsty")
        else:
            person.thirst += 5
            if person.thirst >= 50:
                print(person.name + " is thirsty")

    if person.current_action == "walk_U" or person.current_action=="walk_D" or person.current_action == "walk_L" or person.current_action=="walk_R":
    	#Energy decreases
    	if person.energy < 1:
    		person.energy = 0
    	else:
    		person.energy -= 1

    elif person.current_action == "sleep":
        #Energy increases
        if person.energy > 95:
        	person.energy = 100
        else:
        	person.energy += 5

    elif person.current_action == "eat":
        #Hunger decreases
        if person.hunger < 10:
        	person.hunger = 0
        else:
        	person.hunger -= 10 

        #Desire to take a dump increases
        if person.dump > 90:
        	person.dump = 100
        else:
        	person.dump += 10

    elif person.current_action == "drink":
        #Thirst decreases
        if person.thirst < 10:
        	person.thirst = 0
        else:
        	person.thirst -= 10

        #Bladder contents increase
        if person.bladder > 90:
        	person.bladder = 100
        else:
        	person.bladder += 10