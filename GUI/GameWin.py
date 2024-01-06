import pygame
from .Page import Page
from GUI.gui_constants import WIDTH, HEIGHT


class GameWin(Page):
    def __init__(self, username, rows, columns, mines, difficulty):
        self.title_text = "You WON!!!"
        self.navigation_buttons = []  # {obj: button, val: "Navigation Button", kwargs}
        self.username = username
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.difficulty = difficulty

        # Load the images
        self.button_coordinates = (300, 200)
        self.background = pygame.transform.scale(
            pygame.image.load("./assets/background.png"), (WIDTH, HEIGHT)
        )
        self.title_image = pygame.transform.scale(
            pygame.image.load("./assets/text/you-won.png"), (350, 100)
        )
        self.btn_bg = pygame.transform.scale(
            pygame.image.load("./assets/buttons/menu_butt1.png"),
            self.button_coordinates,
        )
        self.btn_bg_hover = pygame.transform.scale(
            pygame.image.load("./assets/buttons/menu_butt1.png"),
            self.button_coordinates,
        )

        self.restart_text = pygame.transform.scale(
            pygame.image.load("./assets/text/play-again.png"), (200, 50)
        )
        self.back_text = pygame.transform.scale(
            pygame.image.load("./assets/text/back.png"), (100, 50)
        )
        self.quit_text = pygame.transform.scale(
            pygame.image.load("./assets/text/quit.png"), (150, 50)
        )

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT_GAME", None
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for btn in self.navigation_buttons:
                    if self.check_button_hover(event.pos, btn):
                        return btn["val"], btn["kwargs"]
        return None, None

    def update(self, screen, fonts):
        pygame.display.set_caption(self.title_text)
        screen.blit(self.background, (0, 0))

        # self.draw_title("You Won!", screen, fonts["lg"], WIDTH / 2, HEIGHT / 3)
        self.place_img(self.title_image, screen, WIDTH // 2, HEIGHT / 5)
        self.draw_title(
            f"Congratulations, {self.username}",
            screen,
            fonts["sm"],
            WIDTH / 2,
            HEIGHT / 5 + 70,
        )

        game_start = self.place_button(
            self.btn_bg,
            self.btn_bg_hover,
            self.restart_text,
            screen,
            WIDTH // 2,
            HEIGHT // 5 + 180,
        )
        self.navigation_buttons.append(
            {
                "obj": game_start,
                "val": "BOARD",
                "kwargs": {
                    "rows": self.rows,
                    "columns": self.columns,
                    "mines": self.mines,
                    "difficulty": self.difficulty,
                },
                "x": WIDTH // 2,
                "y": HEIGHT // 5 + 180,
            }
        )
        back_main_menu = self.place_button(
            self.btn_bg,
            self.btn_bg_hover,
            self.back_text,
            screen,
            WIDTH // 2,
            HEIGHT // 5 + 300,
        )
        self.navigation_buttons.append(
            {
                "obj": back_main_menu,
                "val": "MAIN_MENU",
                "kwargs": {},
                "x": WIDTH // 2,
                "y": HEIGHT // 5 + 300,
            }
        )
        quit_button = self.place_button(
            self.btn_bg,
            self.btn_bg_hover,
            self.quit_text,
            screen,
            WIDTH // 2,
            HEIGHT // 5 + 420,
        )
        self.navigation_buttons.append(
            {
                "obj": quit_button,
                "val": "QUIT_GAME",
                "kwargs": {},
                "x": WIDTH // 2,
                "y": HEIGHT // 5 + 420,
            }
        )
