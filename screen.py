import pygame
import sys
from classes import Game
from constants import DIFFICULTIES, NUMBER_OF_MINES, BOARD_SIZE
from gui_helpers import create_button
from gui_constants import HEIGHT, WIDTH, PRIMARY_COLOR


class GUI:
    def __init__(self, rows, columns, mines):
        self.game = Game(rows, columns, mines)
        self.game.generate_board(1, 1)
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
                    current_page = Board(self.screen, self.fonts, self.game, 16, 16)

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


class Cell:
    def __init__(
        self,
        screen,
        coordinates,
        info,
        covered_image,
        uncovered_image,
        hover_image,
        value_image,
        flag_image,
        cell_size,
        border_size,
    ):
        self.coordinates = coordinates
        self.screen = screen
        self.cell_size = cell_size
        self.border_size = border_size
        self.info = info
        self.rectangle = pygame.Rect(
            self.border_size + self.cell_size * self.coordinates[0],
            self.border_size + self.cell_size * self.coordinates[1],
            self.cell_size,
            self.cell_size,
        )
        self.is_hovered = False
        self.covered_image = covered_image
        self.uncovered_image = uncovered_image
        self.hover_image = hover_image
        self.value_image = value_image
        self.flag_image = flag_image

    def reveal_cell(self):
        self.info.is_covered = False

    def flag_cell(self):
        self.info.is_flagged = True

    def draw_cell(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rectangle)
        if not self.info.is_covered:
            self.screen.blit(self.uncovered_image, self.rectangle.topleft)
            self.screen.blit(
                self.value_image,
                self.value_image.get_rect(center=self.rectangle.center),
            )
        elif self.info.is_flagged:
            self.screen.blit(
                self.flag_image, self.flag_image.get_rect(center=self.rectangle.center)
            )
        else:
            self.screen.blit(self.covered_image, self.rectangle.topleft)

        is_hovered = self.rectangle.collidepoint(pygame.mouse.get_pos())

        if is_hovered:
            if pygame.mouse.get_pressed()[0]:
                self.reveal_cell()
            elif pygame.mouse.get_pressed()[2]:
                self.flag_cell()
            else:
                self.screen.blit(self.hover_image, self.rectangle.topleft)


class Board:
    def __init__(self, screen, fonts, game, rows, columns, cell_size=40, border_size=1):
        self.title_text = "game"
        self.screen = screen
        self.fonts = fonts
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.border_size = border_size
        self.width = columns * cell_size
        self.height = rows * cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.game = game
        self.covered_image = pygame.transform.scale(
            pygame.image.load("./assets/in_game_icons/board/covered-cell.png"),
            (self.cell_size - self.border_size, self.cell_size - self.border_size),
        )
        self.uncovered_image = pygame.transform.scale(
            pygame.image.load("./assets/in_game_icons/board/dug-cell.png"),
            (self.cell_size - self.border_size, self.cell_size - self.border_size),
        )
        self.hover_image = pygame.transform.scale(
            pygame.image.load("./assets/in_game_icons/board/hover-cell.png"),
            (self.cell_size - self.border_size, self.cell_size - self.border_size),
        )
        self.flag_image = pygame.transform.scale(
            pygame.image.load("./assets/in_game_icons/board/red-flag.png"),
            (self.cell_size, self.cell_size),
        )
        self.value_images = []

        for i in range(8):
            self.value_images.append(
                pygame.transform.scale(
                    pygame.image.load(
                        f"./assets/in_game_icons/board/dug/{i+1}-icon.png"
                    ),
                    (self.cell_size * 0.5, self.cell_size * 0.5),
                )
            )

    def draw_cells(self):
        for row_index in range(len(self.game.board)):
            for column_index in range(len(self.game.board[row_index])):
                cell = Cell(
                    self.screen,
                    (column_index, row_index),
                    self.game.board[row_index][column_index],
                    self.covered_image,
                    self.uncovered_image,
                    self.hover_image,
                    self.value_images[1 - 1],
                    self.flag_image,
                    self.cell_size,
                    self.border_size,
                )
                cell.draw_cell()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pass
        return None, None

    def update(self):
        self.screen.fill(PRIMARY_COLOR)
        self.draw_cells()
        pygame.display.set_caption("Enjoy!!!")

        # TODO
        # Desing the game.board funcitonality


# TODO
# Create a page to ask for name
