import pygame
from .gui_helpers import create_button
from .gui_constants import WIDTH, HEIGHT, SECONDARY_COLOR
from constants import CREDITS
# Dictionary to hold the credits of each creator



class AboutPage:
    def __init__(self):
        self.title_text = "Minesweeper Main Menu"
        self.background = pygame.transform.scale(pygame.image.load('./assets/background.png'), (WIDTH, HEIGHT))
        self.navigation_buttons = []  # {obj: button, val: "Navigation Button", kwargs}

    def handle_events(self):
        for event in pygame.event.get():
            # Check for quitting the game
            if event.type == pygame.QUIT:
                return "QUIT_GAME", None
            
            # Check if clicking buttons
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for btn in self.navigation_buttons:
                    if btn["obj"].collidepoint(event.pos):
                        return btn["val"], btn["kwargs"]

        return None, None


    def draw_title(self, text, screen, font, x, y):
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(
            center=(
                x,
                y,
            )
        )
        screen.blit(text_surface, text_rect.topleft)

    def draw_small_button(self, text, position, screen, fonts, handle_click=lambda: None):
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
            text_size="sm"
        )

    def draw_item(self, name, id, y, screen, font):
        text = f"{name}: {id}"
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
        screen.blit(text_surface, text_rect.topleft)

    def update(self, screen, fonts):
        pygame.display.set_caption(self.title_text)
        screen.blit(self.background, (0, 0))

        # Draw Header
        self.draw_title("Credits", screen, fonts["lg"], WIDTH / 2, HEIGHT / 3)

        # Draw Names
        y = HEIGHT // 2
        for person, id in CREDITS.items():
            self.draw_item(person, id, y, screen, fonts["md"])
            y += 50


        # Draw About Page
        about_btn = self.draw_small_button(
            "Back", (10, 10), screen, fonts
        )
        self.navigation_buttons.append(
            {"obj": about_btn, "val": "MAIN_MENU", "kwargs": {}}
        )
        