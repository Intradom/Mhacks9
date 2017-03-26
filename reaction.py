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
        if person.hunger > 99:
            person.hunger = 100
            person.health -= 5
            print(person.name + " is very hungry")
        else:
            person.hunger += 1
            if person.hunger >= 50:
                print(person.name + " is hungry")
                
        if person.hunger >= constants.HUNGER_THRESHOLD:
            if person.joy < 1:
                person.joy = 0
            else:
                person.joy -= 1
                if person.fitness == 25:
                    print(person.name + " is not happy")
        
    # Constant thirst
    if person.current_action != "drink":
        if person.thirst > 98:
            person.thirst = 100
            person.health -= 5
            print(person.name + " is very thirsty")
        else:
            person.thirst += 2
            if person.thirst >= 50:
                print(person.name + " is thirsty")
                
        if person.hunger < constants.HUNGER_THRESHOLD and person.thirst >= constants.THIRST_THRESHOLD:
            if person.joy < 1:
                person.joy = 0
            else:
                person.joy -= 1
                if person.fitness == 25:
                    print(person.name + " is not happy")

    if person.current_action == "walk_U" or person.current_action=="walk_D" or person.current_action == "walk_L" or person.current_action=="walk_R":
    	#Energy decreases
    	if person.energy < 1:
    		person.energy = 0
    	else:
    		person.energy -= 1
            
    if person.current_action == "run_U" or person.current_action=="run_D" or person.current_action == "run_L" or person.current_action=="run_R":
    	#Energy decreases  
        decrement = 250 / person.fitness
    	if person.energy < decrement:
    		person.energy = 0
    	else:
    		person.energy -= decrement

        if person.fitness > 99:
    		person.fitness = 100
    	else:
            person.fitness += 1
            if person.fitness == 75:
                print(person.name + " is very fit")
            
    elif person.current_action == "sleep":
        #Energy goes to max
        person.energy = 100

    elif person.current_action == "eat":
        #Hunger decreases
        if person.hunger < 30:
        	person.hunger = 0
        else:
        	person.hunger -= 30 

        #Desire to take a dump increases
        if person.dump > 90:
    		person.dump = 100
    	else:
            person.dump += 10
            if person.dump == 50:
                print(person.name + " needs to take a dump")

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
            if person.bladder == 50:
                print(person.name + " needs to pee")
                
    elif person.current_action == "dance":
    
        if person.energy < 10:
        	person.energy = 0
        else:
        	person.energy -= 10
    
        if person.joy > 90:
    		person.joy = 100
    	else:
            person.joy += 10
            if person.joy == 80:
                print(person.name + " is very happy")
                
    elif person.current_action == "pushup":
    
        if person.energy < 10:
        	person.energy = 0
        else:
        	person.energy -= 10
    
        if person.fitness > 90:
    		person.fitness = 100
    	else:
            person.fitness += 10
            if person.fitness == 75:
                print(person.name + " is very fit")
                
    elif person.current_action == "pee":
        person.bladder = 0
                
    elif person.current_action == "poo":
        person.dump = 0