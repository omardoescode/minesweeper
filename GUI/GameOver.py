import pygame
from GUI.gui_constants import WIDTH, HEIGHT
from .Page import Page


class GameOver(Page):
    def __init__(self, username, rows, columns, mines, difficulty, recorder):
        super().__init__()
        self.title_text = "You Lost!!!"
        self.navigation_buttons = []  # {obj: button, val: "Navigation Button", kwargs}
        self.username = username
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.difficulty = difficulty
        self.recorder = recorder

        # Load the images
        self.button_coordinates = (300, 200)

        self.title_image = pygame.transform.scale(
            pygame.image.load("./assets/text/game-over.png"), (400, 100)
        )

        self.restart_text = pygame.transform.scale(
            pygame.image.load("./assets/text/play-again.png"), (200, 50)
        )
        self.rewatch_game = pygame.transform.scale(
            pygame.image.load("./assets/text/rewatch-game.png"), (200, 50)
        )
        self.back_text = pygame.transform.scale(
            pygame.image.load("./assets/text/back.png"), (100, 50)
        )
        self.quit_text = pygame.transform.scale(
            pygame.image.load("./assets/text/quit.png"), (150, 50)
        )

    def add_button(self, screen, text_img, x, y, val, kwargs={}):
        btn = self.place_button(
            self.btn_bg,
            self.btn_bg_hover,
            text_img,
            screen,
            x,
            y,
        )
        self.navigation_buttons.append(
            {
                "obj": btn,
                "val": val,
                "kwargs": kwargs,
                "x": x,
                "y": y,
            }
        )

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT_GAME", None

            # Check Buttons Click
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for btn in self.navigation_buttons:
                    if self.check_button_hover(event.pos, btn):
                        return btn["val"], btn["kwargs"]
        return None, None

    def update(self, screen, fonts):
        pygame.display.set_caption(self.title_text)
        screen.blit(self.background, (0, 0))

        self.place_img(self.title_image, screen, WIDTH // 2, HEIGHT / 5)
        self.draw_title(
            f"Don't Sadden, {self.username}",
            screen,
            fonts["sm"],
            WIDTH / 2,
            HEIGHT / 5 + 70,
        )

        self.add_button(
            screen,
            self.restart_text,
            WIDTH // 2,
            HEIGHT // 5 + 140,
            "REWATCH",
            kwargs={
                "rows": self.rows,
                "columns": self.columns,
                "mines": self.mines,
                "difficulty": self.difficulty,
                "recorder": self.recorder.restart(),
            },
        )
        self.add_button(
            screen,
            self.restart_text,
            WIDTH // 2,
            HEIGHT // 5 + 260,
            "BOARD",
            kwargs={
                "rows": self.rows,
                "columns": self.columns,
                "mines": self.mines,
                "difficulty": self.difficulty,
            },
        )
        self.add_button(
            screen, self.back_text, WIDTH // 2, HEIGHT // 5 + 380, "MAIN_MENU"
        )
        self.add_button(
            screen, self.quit_text, WIDTH // 2, HEIGHT // 5 + 500, "QUIT_GAME"
        )
