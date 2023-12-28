import pygame


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
):
    button_rect = pygame.Rect(x, y, width, height)

    is_hovered = button_rect.collidepoint(pygame.mouse.get_pos())

    button_color = hover_color if is_hovered else normal_color

    pygame.draw.rect(screen, button_color, button_rect)
    text_surface = fonts["md"].render(text, True, text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)

    screen.blit(text_surface, text_rect.topleft)

    if is_hovered and pygame.mouse.get_pressed()[0]:
        handle_click()

    return button_rect


def calc_initial_mine_reveal_time(num_mines):
    pass