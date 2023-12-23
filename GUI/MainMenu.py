import pygame
from gui_helpers import create_button
from gui_constants import WIDTH, HEIGHT, PRIMARY_COLOR


class MainMenu:
    def __init__(self, username):
        self.title_text = "Minesweeper Main Menu"
        self.navigation_buttons = []  # {obj: button, val: "Navigation Button", kwargs}
        self.username = username

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit_game", None
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

    def draw_button(self, text, position, screen, fonts, handle_click=lambda: None):
        return create_button(
            position[0] - 150,
            position[1] + 50,
            300,
            100,
            text,
            (255, 255, 255),
            PRIMARY_COLOR,
            (0, 0, 0),
            screen,
            fonts,
            handle_click,
        )

    def update(self, screen, fonts):
        pygame.display.set_caption(self.title_text)
        screen.fill(PRIMARY_COLOR)

        self.draw_title("Minesweeper", screen, fonts["lg"], WIDTH / 2, HEIGHT / 3)
        self.draw_title(
            f"Hello, {self.username}", screen, fonts["sm"], WIDTH / 2, HEIGHT / 3 + 40
        )

        game_start = self.draw_button(
            "Game Start", (WIDTH // 2, HEIGHT // 3 + 40), screen, fonts
        )
        self.navigation_buttons.append(
            {"obj": game_start, "val": "difficulty", "kwargs": None}
        )
        # TODO: Handle the Stats functionailty
        self.draw_button("Stats", (WIDTH // 2, HEIGHT // 3 + 160), screen, fonts)
        quit_button = self.draw_button(
            "Quit", (WIDTH // 2, HEIGHT // 3 + 280), screen, fonts
        )
        self.navigation_buttons.append(
            {"obj": quit_button, "val": "quit_game", "kwargs": {}}
        )
