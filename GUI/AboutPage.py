import pygame
from .gui_helpers import create_button
from .gui_constants import WIDTH, HEIGHT
from .Page import Page
from constants import CREDITS


class AboutPage(Page):
    def __init__(self):
        super().__init__()
        self.title_text = "Minesweeper Main Menu"

        self.navigation_buttons = []  # {obj: button, val: "Navigation Button", kwargs}

        self.eui_logo = pygame.transform.scale(
            pygame.image.load("./assets/eui.png"), (300, 300)
        )

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

    def draw_item(self, name, id, y, screen, font):
        text = f"{name}: {id}"
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH * 5 // 12, y))
        screen.blit(text_surface, text_rect.topleft)

    def update(self, screen, fonts):
        pygame.display.set_caption(self.title_text)
        screen.blit(self.background, (0, 0))

        # Draw Header
        self.draw_title(
            "Who are we? EUIians", screen, fonts["lg"], WIDTH / 2, HEIGHT / 4
        )

        # Draw Names
        y = HEIGHT // 2
        for person, id in CREDITS.items():
            self.draw_item(person, id, y, screen, fonts["md"])
            y += 50

        # Draw EUI logo
        screen.blit(self.eui_logo, (WIDTH * 2 // 3, HEIGHT // 3))

        # Draw Back Button
        about_btn = self.draw_small_button("Back", (10, 10), screen, fonts)
        self.navigation_buttons.append(
            {"obj": about_btn, "val": "MAIN_MENU", "kwargs": {}}
        )
