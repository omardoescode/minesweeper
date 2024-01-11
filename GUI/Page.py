import pygame
from .gui_helpers import create_button
from .gui_constants import WIDTH, HEIGHT, SECONDARY_COLOR


class Page:
    def __init__(self):
        self.background = pygame.transform.scale(
            pygame.image.load("./assets/background.png"), (WIDTH, HEIGHT)
        )
        self.button_coordinates = (300, 100)
        self.btn_bg = pygame.transform.scale(
            pygame.image.load("./assets/buttons/menu_butt1.png"),
            self.button_coordinates,
        )
        self.btn_bg_hover = pygame.transform.scale(
            pygame.image.load("./assets/buttons/menu_butt1_hover.png"),
            self.button_coordinates,
        )

    def check_button_hover(self, click_coords, btn_data):
        x, y = click_coords
        btn_x = btn_data["x"]
        btn_y = btn_data["y"]
        width, height = self.button_coordinates
        return (
            btn_x - width / 2 <= x <= btn_x + width / 2
            and btn_y - height / 2 <= y <= btn_y + height / 2
        )

    def draw_title(self, text, screen, font, x, y):
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(
            center=(
                x,
                y,
            )
        )
        screen.blit(text_surface, text_rect.topleft)

    def place_img(self, img, screen, x, y):
        img_rect = img.get_rect(center=(x, y))
        screen.blit(img, img_rect.topleft)

        return img_rect

    def place_button(self, bg, bg_hover, text, screen, x, y):
        bg_rect = bg.get_rect(center=(x, y))
        text_rect = text.get_rect(center=(bg_rect.midtop[0], bg_rect.midtop[1] + 30))
        is_hovered = self.check_button_hover(pygame.mouse.get_pos(), {"x": x, "y": y})
        img = bg_hover if is_hovered else bg
        screen.blit(img, bg_rect.topleft)
        screen.blit(text, text_rect.topleft)

        return text_rect

    def draw_small_button(
        self, text, position, screen, fonts, handle_click=lambda: None
    ):
        return create_button(
            position[0],
            position[1],
            120,
            50,
            text,
            (255, 255, 255),
            SECONDARY_COLOR,
            (0, 0, 0),
            screen,
            fonts,
            handle_click,
            text_size="sm",
        )
