import sys

import constants

class Thing(object):

    def __init__(self, n, x, y, r):
        self.name = n
        self.x_coordinate = x
        self.y_coordinate = y
        self.resources = r
        
        def __str__(self):
            return self.name + " " + self.x_coordinate + " " + self.y_coordinate + " " + self.resources

class LivingThings(Thing):

    def __init__(self, n, x, y, he):
        super(LivingThings, self).__init__(n, x, y, 0)
        self.health = he

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
                print("\t" + cognitive_map[i])
        return "**********Player**********"

class Animal(LivingThings):

    def __init__(self, n, x, y, a):
        super(Animal, self).__init__(n, x, y, 0)
        self.aggression = a

class Environment(object):

    def __init__(self):
        w, h = constants.GRID_WIDTH, constants.GRID_HEIGHT;
        self.global_map = [[0 for x in range(w)] for y in range(h)] 
        self.uses = []
        self.weather = "normal"
        self.day = 1
        
        # Initialize environment to be all grass tiles
        for i in range(constants.GRID_WIDTH):
            for j in range(constants.GRID_HEIGHT):
                self.global_map[i][j] = Thing("grass", i, j,0)
                
    def __str__(self):
        print("**********GRID**********\n")
        for row in range(constants.GRID_HEIGHT):
                for col in range(constants.GRID_WIDTH):
                    sys.stdout.write(self.global_map[col][row].name + " ")
                print("\n")
        return "**********GRID**********"
        
    def change_tile(self, x, y, new_name):
        if new_name == "apple_tree":
            self.global_map[x][y] = Thing(new_name, x, y, 10)
        else:
            self.global_map[x][y] = Thing(new_name, x, y, 0)
