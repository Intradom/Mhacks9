class Player: Living

    hunger
    thirst
    energy
    fitness
    anger
    fear
    grief
    joy
    intelligence
    sobriety

    bladder
    dump

    cognitive_map[]

class Thing:
    name
    x_coordinate
    y_coordinate

class Environment:
    global_map[Thing] #no live things
    living_things[]
    weather
    day/night

    uses[] # tree -> food, shelter

class LivingThings
    health
    x_coordinate
    y_coordinate