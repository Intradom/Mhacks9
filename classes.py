import sys

import constants

class Thing(object):

    def __init__(self, n, x, y):
        self.name = n
        self.x_coordinate = x
        self.y_coordinate = y

class LivingThings(Thing):

    def __init__(self, n, x, y, he):
        super(LivingThings, self).__init__(n, x, y)
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

class Animal(LivingThings):

    def __init__(self, n, x, y, a):
        super(Animal, self).__init__(n, x, y)
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
                self.global_map[i][j] = Thing("grass", i, j)
                
    def __str__(self):
        print("**********GRID**********\n")
        for i in range(constants.GRID_WIDTH):
                for j in range(constants.GRID_HEIGHT):
                    sys.stdout.write(self.global_map[i][j].name + " ")
                print("\n")
        return "**********GRID**********"
        
    def change_tile(self, x, y, new_name):
        self.global_map[x][y] = Thing(new_name, x, y)
