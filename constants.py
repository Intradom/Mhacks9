# List of constants used in the simulation

# Colors
C_APPLE = (204, 0, 0)
C_BLACK = (0, 0, 0)
C_GRASS = (178, 255, 102)
C_PLAYER = (102, 0, 204)
C_TREE = (0, 102, 0)
C_WATER = (0, 0, 153)
C_WHITE = (255, 255, 255)

# Grid Info
GRID_WIDTH = 25
GRID_HEIGHT = 25

# Screen Info
SCREEN_WIDTH = 640          # Pixels
SCREEN_HEIGHT = 480         # Pixels
CYCLE_DELAY = 100          # Delay in milliseconds

# draw.py
BOX_WIDTH_SCREEN = SCREEN_WIDTH / GRID_WIDTH
BOX_HEIGHT_SCREEN = SCREEN_HEIGHT / GRID_HEIGHT
HALF_BOX_WIDTH_SCREEN = BOX_WIDTH_SCREEN / 2
HALF_BOX_HEIGHT_SCREEN = BOX_HEIGHT_SCREEN / 2
THIRD_BOX_WIDTH_SCREEN = BOX_WIDTH_SCREEN / 3
THIRD_BOX_HEIGHT_SCREEN = BOX_HEIGHT_SCREEN / 3

# Day Info
CYCLES_IN_DAY = 300

# Player Info, stats defined below
NUM_PLAYERS = 1
NUM_DAYS_WO_WATER = 3
NUM_DAYS_WO_FOOD = 14

# Environment Initial, total can't add up to more than GRID_WIDTH * GRID_HEIGHT - NUM_PLAYERS
E_NUM_REG_TREES = 20
E_NUM_APPLE_TREES = 10
E_NUM_WATER_SPOTS = 10

# Environmental Feature Attributes
E_TREE_APPLE_MIN = 5
E_TREE_APPLE_MAX = 20

# Player Initial Stats
P_HEALTH = 100
P_HUNGER = 0
P_THIRST = 0
P_ENERGY = 100
P_FITNESS = 50 
P_ANGER = 50
P_FEAR = 50
P_GRIEF = 50
P_JOY = 50
P_INTELLIGENCE = 50
P_SOBRIETY = 100
P_BLADDER = 0
P_DUMP = 0

# Time to perform actions in cycles
ACTION_TIME = {}
ACTION_TIME["walk_U"] = 5
ACTION_TIME["walk_D"] = 5
ACTION_TIME["walk_L"] = 5
ACTION_TIME["walk_R"] = 5
ACTION_TIME["run_U"] = 1
ACTION_TIME["run_D"] = 1
ACTION_TIME["run_L"] = 1
ACTION_TIME["run_R"] = 1

ACTION_TIME["eat"] = 10
ACTION_TIME["drink"] = 5
ACTION_TIME["sleep"] = CYCLES_IN_DAY / 2
ACTION_TIME["dance"] = 5
ACTION_TIME["pushup"] = 20
ACTION_TIME["pee"] = 5
ACTION_TIME["poo"] = 10
ACTION_TIME[""] = 5

# Action threshold, outdated using probabilistic methods now
HUNGER_THRESHOLD = 60
THIRST_THRESHOLD = 60
ENERGY_THRESHOLD = 20 

# Field Of View Range
FOV_RADIUS = 3







