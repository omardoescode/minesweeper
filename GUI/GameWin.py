import pygame
from gui_constants import SECONDARY_COLOR, WIDTH, HEIGHT
from gui_helpers import create_button


class GameWin:
    def __init__(self, username, rows, columns, mines):
        self.title_text = "You WON!!!"
        self.navigation_buttons = []  # {obj: button, val: "Navigation Button", kwargs}
        self.username = username
        self.rows = rows
        self.columns = columns
        self.mines = mines

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
            SECONDARY_COLOR,
            (0, 0, 0),
            screen,
            fonts,
            handle_click,
        )

    def update(self, screen, fonts):
        pygame.display.set_caption(self.title_text)
        screen.fill((255, 255, 255))

        self.draw_title("You Won!", screen, fonts["lg"], WIDTH / 2, HEIGHT / 3)
        self.draw_title(
            f"Congratulations, {self.username}",
            screen,
            fonts["sm"],
            WIDTH / 2,
            HEIGHT / 3 + 40,
        )

        game_start = self.draw_button(
            "Restart", (WIDTH // 2, HEIGHT // 3 + 40), screen, fonts
        )
        self.navigation_buttons.append(
            {
                "obj": game_start,
                "val": "board",
                "kwargs": {
                    "rows": self.rows,
                    "columns": self.columns,
                    "mines": self.mines,
                },
            }
        )
        back_main_menu = self.draw_button(
            "Main Menu", (WIDTH // 2, HEIGHT // 3 + 160), screen, fonts
        )
        self.navigation_buttons.append(
            {"obj": back_main_menu, "val": "main_menu", "kwargs": {}}
        )
        quit_button = self.draw_button(
            "Quit", (WIDTH // 2, HEIGHT // 3 + 280), screen, fonts
        )
        self.navigation_buttons.append(
            {"obj": quit_button, "val": "quit_game", "kwargs": {}}
        )
