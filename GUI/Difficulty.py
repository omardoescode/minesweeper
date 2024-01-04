import pygame
from GUI.gui_constants import WIDTH, HEIGHT
from constants import DIFFICULTIES, BOARD_SIZE, NUMBER_OF_MINES


class Difficulty:
    def __init__(self):
        self.title_text = "Minesweeper: Choose the difficulty"
        self.navigation_buttons = []
        self.vertical_placement = HEIGHT // 5
        self.bacground = pygame.transform.scale(
            pygame.image.load("./assets/background.png"), (WIDTH, HEIGHT)
        )

        # Load the images
        self.button_coordinates = (300, 200)
        self.btn_bg = pygame.transform.scale(
            pygame.image.load("./assets/buttons/menu_butt1.png"),
            self.button_coordinates,
        )
        # self.btn_bg_hovered = pygame.transform.scale(pygame.image.load("./assets/buttons/menu_butt1_hover.png"), (200, 100))

        self.texts = {
            "easy": pygame.transform.scale(
                pygame.image.load("./assets/text/easy.png"), (100, 50)
            ),
            "medium": pygame.transform.scale(
                pygame.image.load("./assets/text/medium.png"), (150, 50)
            ),
            "hard": pygame.transform.scale(
                pygame.image.load("./assets/text/hard.png"), (100, 50)
            ),
        }
        self.custom_text = pygame.transform.scale(
            pygame.image.load("./assets/text/custom.png"), (150, 50)
        )
        self.back_text = pygame.transform.scale(
            pygame.image.load("./assets/text/back.png"), (100, 50)
        )

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT_GAME", None
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for btn in self.navigation_buttons:
                    if self.check_button_click(event.pos, btn):
                        return btn["val"], btn["kwargs"]
        return None, None

    def place_button(self, bg, text, screen, x, y):
        bg_rect = bg.get_rect(center=(x, y))
        text_rect = text.get_rect(center=(bg_rect.midtop[0], bg_rect.midtop[1] + 85))
        screen.blit(bg, bg_rect.topleft)
        screen.blit(text, text_rect.topleft)

        return bg_rect

    def check_button_click(self, click_coords, btn_data):
        x, y = click_coords
        btn_x = btn_data["x"]
        btn_y = btn_data["y"]
        width, height = self.button_coordinates
        return (
            btn_x - width / 2 <= x <= btn_x + width / 2
            and btn_y - height / 4 <= y <= btn_y + height / 4
        )

    def update(self, screen, fonts):
        pygame.display.set_caption(self.title_text)
        screen.blit(self.bacground, (0, 0))

        y = 120
        for dif in DIFFICULTIES.values():
            btn = self.place_button(self.btn_bg, self.texts[dif], screen, WIDTH // 2, y)
            self.navigation_buttons.append(
                {
                    "obj": btn,
                    "val": "BOARD",
                    "kwargs": {
                        "rows": BOARD_SIZE[dif][0],
                        "columns": BOARD_SIZE[dif][1],
                        "mines": NUMBER_OF_MINES[dif],
                        "difficulty": dif,
                    },
                    "x": WIDTH // 2,
                    "y": y,
                }
            )
            y += 120
        custom_difficulty_button = self.place_button(
            self.btn_bg, self.custom_text, screen, WIDTH // 2, y
        )
        self.navigation_buttons.append(
            {
                "obj": custom_difficulty_button,
                "val": "CUSTOM_DIFFICULTY",
                "kwargs": {},
                "x": WIDTH // 2,
                "y": y,
            }
        )
        go_back_button = self.place_button(
            self.btn_bg, self.back_text, screen, WIDTH // 2, y + 120
        )
        self.navigation_buttons.append(
            {
                "obj": go_back_button,
                "val": "MAIN_MENU",
                "kwargs": {},
                "x": WIDTH // 2,
                "y": y,
            }
        )
