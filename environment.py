import classes


def process_environment(environment):
    for x in range(len(environment.global_map)):
        for y in range(len(environment.global_map[0])):
            name = environment.global_map[x][y]
            num_resources = environment.global_map[x][y].resources
            if name == "apple_tree" and num_resources == 0:
                classes.environment.change_tile("reg_tree", 0, x, y)
