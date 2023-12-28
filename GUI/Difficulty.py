import pygame
from GUI.gui_helpers import create_button
from GUI.gui_constants import PRIMARY_COLOR, WIDTH, HEIGHT, SECONDARY_COLOR
from constants import DIFFICULTIES, BOARD_SIZE, NUMBER_OF_MINES


class Difficulty:
    def __init__(self):
        self.title_text = "Minesweeper: Choose the difficulty"
        self.navigation_buttons = []
        self.vertical_placement = HEIGHT // 5

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit_game", None
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for btn in self.navigation_buttons:
                    if btn["obj"].collidepoint(event.pos):
                        return btn["val"], btn["kwargs"]
        return None, None

    def draw_button(self, text, position, screen, fonts, handle_click=lambda: None):
        return create_button(
            position[0] - 150,
            position[1],
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
        screen.fill(PRIMARY_COLOR)

        y = 100
        for dif in DIFFICULTIES.values():
            btn = self.draw_button(dif.capitalize(), (WIDTH // 2, y), screen, fonts)
            self.navigation_buttons.append(
                {
                    "obj": btn,
                    "val": "board",
                    "kwargs": {
                        "rows": BOARD_SIZE[dif][0],
                        "columns": BOARD_SIZE[dif][1],
                        "mines": NUMBER_OF_MINES[dif],
                    },
                }
            )
            y += 120
        custom_difficulty_button = self.draw_button(
            "Custom", (WIDTH // 2, y), screen, fonts
        )
        self.navigation_buttons.append(
            {"obj": custom_difficulty_button, "val": "custom_difficulty", "kwargs": {}}
        )
        go_back_button = self.draw_button("Back", (WIDTH // 2, y + 120), screen, fonts)
        self.navigation_buttons.append(
            {"obj": go_back_button, "val": "main_menu", "kwargs": {}}
        )
