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
def draw_tree(screen, (x_coordinate_grid, y_coordinate_grid), apple):

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

    # make it a fruit tree if needed
    if (apple):

        # left apple
        apple_1 = (coordinate_screen[0] + constants.THIRD_BOX_WIDTH_SCREEN,
                   coordinate_screen[1] + constants.HALF_BOX_HEIGHT_SCREEN +
                   constants.THIRD_BOX_HEIGHT_SCREEN)

        # middle apple
        apple_2 = (coordinate_screen[0] + constants.HALF_BOX_WIDTH_SCREEN,
                   coordinate_screen[1] + constants.THIRD_BOX_HEIGHT_SCREEN)

        # right apple
        apple_3 = (coordinate_screen[0] + constants.BOX_WIDTH_SCREEN -
                   constants.THIRD_BOX_WIDTH_SCREEN,
                   coordinate_screen[1] + constants.HALF_BOX_HEIGHT_SCREEN +
                   constants.THIRD_BOX_HEIGHT_SCREEN)

        radius = (constants.BOX_WIDTH_SCREEN * constants.BOX_HEIGHT_SCREEN) / \
            500
        pygame.draw.circle(screen, constants.C_APPLE, apple_1, radius, 0)
        pygame.draw.circle(screen, constants.C_APPLE, apple_2, radius, 0)
        pygame.draw.circle(screen, constants.C_APPLE, apple_3, radius, 0)


def draw_water(screen, (x_coordinate_grid, y_coordinate_grid)):

    coordinate_screen = grid_to_screen((x_coordinate_grid, y_coordinate_grid))
    Rect = list(coordinate_screen)
    Rect.append(constants.BOX_WIDTH_SCREEN)
    Rect.append(constants.BOX_HEIGHT_SCREEN)

    pygame.draw.rect(screen, constants.C_DARK_BLUE, tuple(Rect), 0)


def draw_player(screen, (x_coordinate_grid, y_coordinate_grid)):
    # convert grid coordinates to screen coordinates
    coordinate_screen = grid_to_screen((x_coordinate_grid, y_coordinate_grid))

    player = (coordinate_screen[0] + constants.HALF_BOX_WIDTH_SCREEN,
              constants.HALF_BOX_HEIGHT_SCREEN)

    pygame.draw.circle(screen, constants.C_PLAYER, player,
                       constants.HALF_BOX_HEIGHT_SCREEN, 0)



def draw_environment(screen, x):
    # circle(Surface, color, pos, radius, width=0)
    #pygame.draw.circle(screen, constants.C_BLACK, (x, constants.SCREEN_HEIGHT / 2), 100, 1)

    draw_water(screen, (0, 0))
    draw_water(screen, (0, 1))
    draw_water(screen, (1, 0))
    draw_water(screen, (1, 1))
    draw_tree(screen, (2, 0), False)
    draw_tree(screen, (2, 1), False)
    draw_tree(screen, (2, 2), True)
    draw_tree(screen, (0, 2), False)
    draw_tree(screen, (1, 2), False)
    draw_player(screen, (3, 3))


def draw_person():
    pass


def draw_players(screen):
    pass


def draw_tools(screen):
    pass


def process_draws(screen, x):
    # Clear screen
    screen.fill(constants.C_MEADOW_GREEN)

    draw_environment(screen, x)
    draw_players(screen)
    draw_tools(screen)

    pygame.display.update()
