import sys
import random

import constants

###############################################################################
class Thing(object):
    def __init__(self, name_in, resrouces_in, x_in, y_in):
        self.name = name_in
        self.resources = resrouces_in
        self.x_coordinate = x_in
        self.y_coordinate = y_in

    def __str__(self):
        return self.name + " " + str(self.resources) + " " + \
            str(self.x_coordinate) + " " + str(self.y_coordinate)


class LivingThings(Thing):
    def __init__(self, name_in, x_in, y_in, health_in):
        super(LivingThings, self).__init__(name_in, x_in, y_in, 0)
        self.health = health_in


class Animal(LivingThings):
    def __init__(self, name_in, x_in, y_in, agression_in):
        super(Animal, self).__init__(name_in, x_in, y_in, 0)
        self.aggression = agression_in
###############################################################################


class Player(LivingThings):

    def __init__(self, n, x, y, he, hu, t, e, fi, a, fe, g, j, i, s, b, d):
        super(Player, self).__init__(n, x, y, he)
        self.cognitive_map = []
        self.hunger = hu
        self.thirst = t
        self.energy = e
        self.fitness = fi
        self.anger = a
        self.fear = fe
        self.grief = g
        self.joy = j
        self.intelligence = i
        self.sobriety = s
        self.bladder = b
        self.dump = d

        self.last_thought = ""
        self.current_action = ""
        self.action_counter = 0

    def __str__(self):
        print("**********Player**********")
        print("Name: " + str(self.name))
        print("X: " + str(self.x_coordinate))
        print("Y: " + str(self.y_coordinate))
        print("Health: " + str(self.health))
        print("Hunger: " + str(self.hunger))
        print("Thirst: " + str(self.thirst))
        print("Energy: " + str(self.energy))
        print("Fitness: " + str(self.fitness))
        print("Anger: " + str(self.anger))
        print("Fear: " + str(self.fear))
        print("Grief: " + str(self.grief))
        print("Joy: " + str(self.joy))
        print("Intelligence: " + str(self.intelligence))
        print("Sobriety: " + str(self.sobriety))
        print("Bladder: " + str(self.bladder))
        print("Dump: " + str(self.dump))
        print("Last thought: " + self.last_thought)
        print("Current action: " + self.current_action)
        print("Action counter: " + str(self.action_counter))
        print("Cognitive Map: ")
        if len(self.cognitive_map) == 0:
            print("\tCognitive map empty")
        else:
            for i in range(len(self.cognitive_map)):
                print("\t" + self.cognitive_map[i])
        return "**********Player**********"


###############################################################################
class Environment(object):

    def __init__(self):
        width, height = constants.GRID_WIDTH, constants.GRID_HEIGHT

        self.global_map = [[0 for x in range(width)] for y in range(height)]
        self.uses = []
        self.weather = "normal"
        self.day = 1

        # initialize environment to be all grass tiles
        for i in range(constants.GRID_WIDTH):
            for j in range(constants.GRID_HEIGHT):
                self.global_map[i][j] = Thing("grass", 0, i, j)

    def __str__(self):
        print("**********GRID**********\n")
        for i in range(constants.GRID_HEIGHT):
            for j in range(constants.GRID_WIDTH):
                sys.stdout.write(self.global_map[i][j].name + " ")
                print("\n")
        return "**********GRID**********"

    def change_tile(self, name_in, resources_in, x_in, y_in):
        if name_in == "apple_tree":
            resources_in = random.randint(constants.E_TREE_APPLE_MIN, constants.E_TREE_APPLE_MAX)
        self.global_map[x_in][y_in] = Thing(name_in, resources_in, x_in, y_in)
###############################################################################
