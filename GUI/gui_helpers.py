import pygame
from helpers import every, flat

def create_button(
    x,
    y,
    width,
    height,
    text,
    normal_color,
    hover_color,
    text_color,
    screen,
    fonts,
    handle_click=lambda: None,
    text_size="md"
):
    button_rect = pygame.Rect(x, y, width, height)

    is_hovered = button_rect.collidepoint(pygame.mouse.get_pos())

    button_color = hover_color if is_hovered else normal_color

    pygame.draw.rect(screen, button_color, button_rect)
    text_surface = fonts[text_size].render(text, True, text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)

    screen.blit(text_surface, text_rect.topleft)

    if is_hovered and pygame.mouse.get_pressed()[0]:
        handle_click()

    return button_rect


def calc_initial_mine_reveal_time(num_mines):
    pass

def calculate_cell_size(rows, columns):
    width, height = get_page_coordinates()

    # formula for cell_size
    return min(width // columns, height // rows)

def get_page_coordinates():

    # Get the display information
    display_info = pygame.display.Info()

    # Get the screen width and height
    screen_width = display_info.current_w
    screen_height = display_info.current_h

    return screen_width, screen_height

# (listof Cell) -> bool
# return false, if at least one of the cells is uncovered
def started_playing(board):
    return not every(lambda cell: cell.is_covered, flat(board))