import constants
import pygame


# REQUIRES: x_coordinate_grid, y_coordinate grid are valid grid coordinates
# MODIFIES: screen
# EFFECTS:  converts a grid coordinate to a screen coordinate
def grid_to_screen((x_coordinate_grid, y_coordinate_grid)):
    x_coordinate_screen = (x_coordinate_grid / constants.GRID_WIDTH) * \
        constants.SCREEN_WIDTH
    y_coordinate_screen = (y_coordinate_grid / constants.GRID_HEIGHT) * \
        constants.SCREEN_HEIGHT
    return (x_coordinate_screen, y_coordinate_screen)


# REQUIRES: x_coordinate_grid, y_coordinate grid are valid grid coordinates
# MODIFIES: screen
# EFFECTS:  draws a tree at (x_coordinate_grid, y_coordinate_grid)
def draw_tree(screen, (x_coordinate_grid, y_coordinate_grid)):

    box_width = constants.SCREEN_WIDTH / constants.GRID_WIDTH
    box_height = constants.SCREEN_HEIGHT / constants.GRID_HEIGHT

    half_box_width = box_width / 2
    half_box_height = box_height / 2

    top_coordinate_grid = (x_coordinate_grid, y_coordinate_grid -
                           half_box_height)
    left_coordinate_grid = (x_coordinate_grid - half_box_width,
                            y_coordinate_grid + half_box_height)
    right_coordinate_grid = (x_coordinate_grid + half_box_width,
                             y_coordinate_grid + half_box_height)

    top_coordinate_screen = grid_to_screen(top_coordinate_grid)
    left_coordinate_screen = grid_to_screen(left_coordinate_grid)
    right_coordinate_screen = grid_to_screen(right_coordinate_grid)

    # pygame.draw.polygon(Surface, color, pointlist, width=0)
    pygame.draw.polygon(screen, constants.C_DARK_GREEN, (top_coordinate_screen,
                        left_coordinate_screen, right_coordinate_screen),
                        width=0)


def draw_water():
    pass


def draw_environment(screen, x):
    # circle(Surface, color, pos, radius, width=0)
    pygame.draw.circle(screen, constants.C_BLACK, (x, constants.SCREEN_HEIGHT / 2), 100, 1)


def draw_person():
    pass


def draw_players(screen):
    pass


def draw_tools(screen):
    pass


def process_draws(screen, x):
    # Clear screen
    screen.fill(constants.C_WHITE)

    draw_environment(screen, x)
    draw_players(screen)
    draw_tools(screen)

    pygame.display.update()
