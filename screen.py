import pygame
import sys
from classes import Game
from constants import DIFFICULTIES, NUMBER_OF_MINES, BOARD_SIZE
from gui_helpers import create_button
from gui_constants import HEIGHT, WIDTH, PRIMARY_COLOR


class GUI(Game):
    def __init__(self, rows, columns, mines):
        super().__init__(rows, columns, mines)
        pygame.init()
        pygame.display.set_caption("Minesweeper")
        pygame.font.init()
        self.fonts = {
            "xl": pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 60),
            "lg": pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 40),
            "md": pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 20),
            "sm": pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 10),
        }
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def start_game(self):
        current_page = MainMenu(self.screen, self.fonts)

        while True:
            action, kwargs = current_page.handle_events()

            match action:
                case "quit_game":
                    pygame.quit()
                    sys.exit()
                case "main_menu":
                    current_page = MainMenu(self.screen, self.fonts)
                case "difficulty":
                    current_page = Difficulty(self.screen, self.fonts)
                case "board":
                    current_page = Board(
                        self.screen,
                        self.fonts,
                        kwargs["rows"],
                        kwargs["columns"],
                        kwargs["mines"],
                    )

            current_page.update()

            pygame.display.flip()
            self.clock.tick(60)


class MainMenu:
    def __init__(self, screen, fonts):
        self.title_text = "Minesweeper Main Menu"
        self.screen = screen
        self.fonts = fonts
        self.navigation_buttons = []
        # {obj: button, val: "Navigation Button", kwargs}

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit_game", None
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for btn in self.navigation_buttons:
                    if btn["obj"].collidepoint(event.pos):
                        return btn["val"], btn["kwargs"]
        return None, None

    def draw_title(self):
        text_surface = self.fonts["lg"].render("Minesweeper", True, (0, 0, 0))
        text_rect = text_surface.get_rect(
            center=(
                WIDTH / 2,
                HEIGHT / 3,
            )
        )
        self.screen.blit(text_surface, text_rect.topleft)

    def draw_button(self, text, position, handle_click=lambda: None):
        return create_button(
            position[0] - 150,
            position[1] + 40,
            300,
            100,
            text,
            (255, 255, 255),
            PRIMARY_COLOR,
            (0, 0, 0),
            self.screen,
            self.fonts,
            handle_click,
        )

    def update(self):
        pygame.display.set_caption(self.title_text)
        self.screen.fill(PRIMARY_COLOR)

        self.draw_title()

        game_start = self.draw_button("Game Start", (WIDTH // 2, HEIGHT // 3 + 40))
        self.navigation_buttons.append(
            {"obj": game_start, "val": "difficulty", "kwargs": None}
        )
        # TODO: Handle the options functionailty
        self.draw_button("Options", (WIDTH // 2, HEIGHT // 3 + 160))
        quit_button = self.draw_button("Quit", (WIDTH // 2, HEIGHT // 3 + 280))
        self.navigation_buttons.append(
            {"obj": quit_button, "val": "quit_game", "kwargs": {}}
        )


class Difficulty:
    def __init__(self, screen, fonts):
        self.title_text = "Minesweeper: Choose the difficulty"
        self.screen = screen
        self.fonts = fonts
        self.navigation_buttons = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for btn in self.navigation_buttons:
                    if btn["obj"].collidepoint(event.pos):
                        print("Hello")
                        return btn["val"], btn["kwargs"]
        return None, None

    def draw_title(self):
        text_surface = self.fonts["lg"].render("Choose the Difficulty", True, (0, 0, 0))
        text_rect = text_surface.get_rect(
            center=(
                WIDTH / 2,
                HEIGHT / 3 - 40,
            )
        )
        self.screen.blit(text_surface, text_rect.topleft)

    def draw_button(self, text, position, handle_click=lambda: None):
        return create_button(
            position[0] - 150,
            position[1] + 40,
            300,
            100,
            text,
            (255, 255, 255),
            PRIMARY_COLOR,
            (0, 0, 0),
            self.screen,
            self.fonts,
            handle_click,
        )

    def update(self):
        pygame.display.set_caption(self.title_text)
        self.screen.fill(PRIMARY_COLOR)

        y = HEIGHT // 5
        for dif in DIFFICULTIES.values():
            btn = self.draw_button(dif.capitalize(), (WIDTH // 2, y))
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
        go_back_button = self.draw_button("Back", (WIDTH // 2, y))
        self.navigation_buttons.append(
            {"obj": go_back_button, "val": "main_menu", "kwargs": {}}
        )


class Board:
    def __init__(self, screen, fonts):
        self.title_text = "board"
        self.screen = screen
        self.fonts = fonts

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pass
        return None, None

    def update(self):
        pygame.display.set_caption("Enjoy!!!")
        self.screen.fill(PRIMARY_COLOR)

        # TODO
        # Desing the board funcitonality


# TODO
# Create a page to ask for name
