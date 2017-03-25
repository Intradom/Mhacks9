import constants
import pygame


# REQUIRES: x_coordinate_grid, y_coordinate grid are valid grid coordinates
# MODIFIES: screen
# EFFECTS:  converts a grid coordinate to a screen coordinate (upper left hand
#           corner)
def grid_to_screen((x_coordinate_grid, y_coordinate_grid)):
    x_coordinate_screen = (constants.BOX_WIDTH_SCREEN * x_coordinate_grid)
    y_coordinate_screen = (constants.BOX_HEIGHT_SCREEN) * y_coordinate_grid
    return (x_coordinate_screen, y_coordinate_screen)


# REQUIRES: x_coordinate_grid, y_coordinate grid are valid grid coordinates
# MODIFIES: screen
# EFFECTS:  draws a tree at (x_coordinate_grid, y_coordinate_grid)
def draw_tree(screen, (x_coordinate_grid, y_coordinate_grid)):

    # convert grid coordinates to screen coordinates
    coordinate_screen = grid_to_screen((x_coordinate_grid, y_coordinate_grid))

    # calculate coordinates for triangle
    top_coordinate_screen = (coordinate_screen[0] +
                             constants.HALF_BOX_WIDTH_SCREEN,
                             coordinate_screen[1])
    left_coordinate_screen = (coordinate_screen[0], coordinate_screen[1] +
                              constants.BOX_HEIGHT_SCREEN)
    right_coordinate_screen = (coordinate_screen[0] +
                               constants.BOX_WIDTH_SCREEN,
                               coordinate_screen[1] +
                               constants.BOX_HEIGHT_SCREEN)

    # pygame.draw.polygon(Surface, color, pointlist, width=0)
    pygame.draw.polygon(screen, constants.C_DARK_GREEN, (top_coordinate_screen,
                        left_coordinate_screen, right_coordinate_screen), 0)


def draw_water(screen, (x_coordinate_grid, y_coordinate_grid)):


    # pygame.draw.rect(Surface, color, Rect, width=0)
    #pygame.draw.rect(screen, constants.C_DARK_BLUE, (constants.BOX_HEIGHT_SCREEN * constants.BOX_WIDTH_SCREEN), 0)
    pass


def draw_environment(screen, x):
    # circle(Surface, color, pos, radius, width=0)
    #pygame.draw.circle(screen, constants.C_BLACK, (x, constants.SCREEN_HEIGHT / 2), 100, 1)
    for i in range(9):
        for j in range(9):
            draw_tree(screen, (i, j))

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
