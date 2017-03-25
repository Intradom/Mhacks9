# List of constants used in the simulation

# Colors
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_DARK_GREEN = (0, 102, 0)
C_DARK_BLUE = (0, 0, 153)

# Grid Info
GRID_WIDTH = 99
GRID_HEIGHT = 99

# Screen Info
SCREEN_WIDTH = 640          # Pixels
SCREEN_HEIGHT = 480         # Pixels
CYCLE_DELAY = 1000          # Delay in milliseconds

# draw.py
BOX_WIDTH_SCREEN = SCREEN_WIDTH / GRID_WIDTH
BOX_HEIGHT_SCREEN = SCREEN_HEIGHT / GRID_HEIGHT
HALF_BOX_WIDTH_SCREEN = BOX_WIDTH_SCREEN / 2
HALF_BOX_HEIGHT_SCREEN = BOX_HEIGHT_SCREEN / 2

# Day Info
CYCLES_IN_DAY = 1000

# Player Info, stats defined below
NUM_PLAYERS = 1
NUM_DAYS_WO_WATER = 3
NUM_DAYS_WO_FOOD = 14

# Environment Initial, total can't add up to more than GRID_WIDTH * GRID_HEIGHT - NUM_PLAYERS
E_NUM_REG_TREES = 5
E_NUM_APPLE_TREES = 1
E_NUM_WATER_SPOTS = 1

# Player Initial Stats
P_HEALTH = 100
P_HUNGER = 1
P_THIRST = 1
P_ENERGY = 100
P_FITNESS = 50 
P_ANGER = 50
P_FEAR = 50
P_GRIEF = 50
P_JOY = 50
P_INTELLIGENCE = 50
P_SOBRIETY = 100
P_BLADDER = 1
P_DUMP = 1 

# Time to perform actions
ACTION_TIME = {}
ACTION_TIME[walk_U] = 1
ACTION_TIME[walk_D] = 1
ACTION_TIME[walk_L] = 1
ACTION_TIME[walk_R] = 1

ACTION_TIME[eat] = 3
ACTION_TIME[drink] = 3
ACTION_TIME[sleep] = 25









