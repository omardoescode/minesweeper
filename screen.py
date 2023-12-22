import pygame
import sys
from classes import Game
from constants import DIFFICULTIES, NUMBER_OF_MINES, BOARD_SIZE
from gui_helpers import create_button
from gui_constants import HEIGHT, WIDTH, PRIMARY_COLOR, DIFFICULTIES_CELLS_SIZES


class GUI:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Minesweeper")
        pygame.font.init()
        self.fonts = {
            "lg": pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 40),
            "md": pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 20),
            "sm": pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 15),
        }
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.username = None

    def start_game(self):
        current_page = PlayerNamePage()

        while True:
            action, kwargs = current_page.handle_events()

            match action:
                case "quit_game":
                    pygame.quit()
                    sys.exit()
                case "main_menu":
                    if kwargs and "name" in kwargs:
                        self.username = kwargs["name"]
                    current_page = MainMenu(self.username)
                case "difficulty":
                    current_page = Difficulty()
                case "board":
                    current_page = Board(
                        kwargs["rows"],
                        kwargs["columns"],
                        kwargs["mines"],
                        cell_size=kwargs["cell_size"],
                    )
                case "game_lose":
                    current_page = GameLose(
                        self.username,
                        kwargs["rows"],
                        kwargs["columns"],
                        kwargs["mines"],
                        cell_size=kwargs["cell_size"],
                    )
                case "game_win":
                    current_page = GameWin(
                        self.username,
                        kwargs["rows"],
                        kwargs["columns"],
                        kwargs["mines"],
                        cell_size=kwargs["cell_size"],
                    )
            current_page.update(self.screen, self.fonts)

            pygame.display.flip()
            self.clock.tick(60)


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
        # TODO: Handle the options functionailty
        self.draw_button("Stats", (WIDTH // 2, HEIGHT // 3 + 160), screen, fonts)
        quit_button = self.draw_button(
            "Quit", (WIDTH // 2, HEIGHT // 3 + 280), screen, fonts
        )
        self.navigation_buttons.append(
            {"obj": quit_button, "val": "quit_game", "kwargs": {}}
        )


class Difficulty:
    def __init__(self):
        self.title_text = "Minesweeper: Choose the difficulty"
        self.navigation_buttons = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for btn in self.navigation_buttons:
                    if btn["obj"].collidepoint(event.pos):
                        return btn["val"], btn["kwargs"]
        return None, None

    def draw_button(self, text, position, screen, fonts, handle_click=lambda: None):
        return create_button(
            position[0] - 150,
            position[1] + 40,
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

        y = HEIGHT // 5
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
                        "cell_size": DIFFICULTIES_CELLS_SIZES[dif],
                    },
                }
            )
            y += 120
        go_back_button = self.draw_button("Back", (WIDTH // 2, y), screen, fonts)
        self.navigation_buttons.append(
            {"obj": go_back_button, "val": "main_menu", "kwargs": {}}
        )


class Cell:
    def __init__(
        self,
        handle_lose,
        handle_flag,
        handle_click,
        coordinates,
        is_clicked,
        is_flagged,
        value,
        covered_image,
        uncovered_image,
        hover_image,
        value_image,
        flag_image,
        cell_size,
        border_size,
    ):
        self.coordinates = coordinates
        self.cell_size = cell_size
        self.border_size = border_size
        self.value = value
        self.handle_lose = handle_lose
        self.handle_flag = handle_flag
        self.handle_click = handle_click
        self.rectangle = pygame.Rect(
            self.border_size + self.cell_size * self.coordinates[0],
            self.border_size + self.cell_size * self.coordinates[1],
            self.cell_size,
            self.cell_size,
        )
        self.is_hovered = False
        self.is_clicked = is_clicked
        self.is_flagged = is_flagged
        self.covered_image = covered_image
        self.uncovered_image = uncovered_image
        self.hover_image = hover_image
        self.value_image = value_image
        self.flag_image = flag_image

    def reveal_cell(self):
        self.handle_click(self.coordinates[1], self.coordinates[0])

        if self.value == "M":
            self.handle_lose()

        self.is_clicked = True

    def flag_cell(self):
        self.is_flagged = True

        self.handle_flag(self.coordinates[1], self.coordinates[0])

    def draw_cell(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rectangle)
        if self.is_clicked:
            screen.blit(self.uncovered_image, self.rectangle.topleft)
            screen.blit(
                self.value_image,
                self.value_image.get_rect(center=self.rectangle.center),
            )
        elif self.is_flagged:
            screen.blit(self.covered_image, self.rectangle.topleft)
            screen.blit(
                self.flag_image, self.flag_image.get_rect(center=self.rectangle.center)
            )
        else:
            screen.blit(self.covered_image, self.rectangle.topleft)

        is_hovered = self.rectangle.collidepoint(pygame.mouse.get_pos())

        if is_hovered and self.is_clicked == False:
            if pygame.mouse.get_pressed()[0]:
                self.reveal_cell()
            elif pygame.mouse.get_pressed()[2]:
                self.flag_cell()
            elif self.is_flagged == False:
                screen.blit(self.hover_image, self.rectangle.topleft)


class Board(Game):
    def __init__(self, rows, columns, mines, cell_size=40, border_size=1):
        super().__init__(rows, columns, mines)
        self.title_text = "board"
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.border_size = border_size
        self.width = columns * cell_size
        self.height = rows * cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
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
        self.mine_image = pygame.transform.scale(
            pygame.image.load("./assets/in_game_icons/board/mine.png"),
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

    def draw_title(self, text, screen, fonts):
        text_surface = fonts["lg"].render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(
            center=(
                self.width / 2,
                self.height / 3,
            )
        )
        screen.blit(text_surface, text_rect.topleft)

    def draw_cells(self, screen, fonts):
        if self.playing:
            for row_index in range(len(self.board)):
                for column_index in range(len(self.board[row_index])):
                    cell_data = self.board[row_index][column_index]
                    if cell_data.val != None:
                        if cell_data.val == "M":
                            image = self.mine_image
                        elif cell_data.val == 0:
                            image = self.uncovered_image
                        else:
                            image = self.value_images[cell_data.val - 1]
                    else:
                        image = self.uncovered_image
                    cell = Cell(
                        self.game_lose,
                        self.flag_cell,
                        self.click_cell,
                        (column_index, row_index),
                        not cell_data.is_covered,
                        cell_data.is_flagged,
                        cell_data.val,
                        self.covered_image,
                        self.uncovered_image,
                        self.hover_image,
                        image,
                        self.flag_image,
                        self.cell_size,
                        self.border_size,
                    )
                    cell.draw_cell(screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if self.start_playing and self.check_win():
            return "game_win", {
                "rows": self.rows,
                "columns": self.columns,
                "mines": self.mines,
                "cell_size": self.cell_size,
            }
        if not self.playing:
            return "game_lose", {
                "rows": self.rows,
                "columns": self.columns,
                "mines": self.mines,
                "cell_size": self.cell_size,
            }
        return None, None

    def update(self, screen, fonts):
        screen.fill(PRIMARY_COLOR)
        self.draw_cells(screen, fonts)
        pygame.display.set_caption("Enjoy!!!")


class PlayerNamePage:
    def __init__(self):
        self.title_text = "Enter Your Name"
        self.submit_button = pygame.Rect(0, 0, 0, 0)
        self.text_input = ""
        self.input_rect = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2, 400, 50)
        self.active = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.submit_button.collidepoint(event.pos):
                    if self.text_input:
                        return "main_menu", {
                            "name": self.text_input
                        }  # Proceed to the main menu
                if self.input_rect.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
                self.text_input = ""

            elif event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        if self.text_input:
                            return (
                                "main_menu",
                                {"name": self.text_input},
                            )  # Proceed to the game board
                    elif event.key == pygame.K_BACKSPACE:
                        self.text_input = self.text_input[:-1]
                    elif (event.unicode.isalnum() or event.unicode.isspace()) and len(
                        self.text_input
                    ) < 18:
                        self.text_input += event.unicode
        return None, None

    def draw_input_box(self, screen, fonts):
        pygame.draw.rect(screen, (255, 255, 255), self.input_rect)
        text_surface = fonts["md"].render(self.text_input, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.input_rect.center)
        screen.blit(text_surface, text_rect.topleft)

    def draw_submit_button(self, screen, fonts):
        self.submit_button = create_button(
            WIDTH // 2,
            HEIGHT // 2 + 60,
            200,
            50,
            "Submit",
            (255, 255, 255),
            PRIMARY_COLOR,
            (0, 0, 0),
            screen,
            fonts,
        )

    def update(self, screen, fonts):
        pygame.display.set_caption(self.title_text)
        screen.fill(PRIMARY_COLOR)

        text_surface = fonts["lg"].render("Enter Your Name", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(text_surface, text_rect.topleft)

        self.draw_input_box(screen, fonts)
        self.draw_submit_button(screen, fonts)


class GameLose:
    def __init__(self, username, rows, columns, mines, cell_size):
        self.title_text = "You Lost!!!"
        self.navigation_buttons = []  # {obj: button, val: "Navigation Button", kwargs}
        self.username = username
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.cell_size = cell_size

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
        screen.fill((255, 255, 255))

        self.draw_title("You Lost!", screen, fonts["lg"], WIDTH / 2, HEIGHT / 3)
        self.draw_title(
            f"Don't sadden, {self.username}",
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
                    "cell_size": self.cell_size,
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


class GameWin:
    def __init__(self, username, rows, columns, mines, cell_size):
        self.title_text = "You WON!!!"
        self.navigation_buttons = []  # {obj: button, val: "Navigation Button", kwargs}
        self.username = username
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.cell_size = cell_size

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
                    "cell_size": self.cell_size,
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
