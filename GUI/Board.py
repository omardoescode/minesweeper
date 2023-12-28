import pygame
from classes import Game
from gui_constants import PRIMARY_COLOR
from gui_helpers import calculate_cell_size


class Cell:
    def __init__(
        self,
        handle_lose,
        handle_flag,
        handle_click,
        handle_chord,
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
        self.handle_chord = handle_chord
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
        self.handle_click(self.coordinates[0], self.coordinates[1])

        if self.value == "M":
            self.handle_lose()

        self.is_clicked = True

    def flag_cell(self):
        self.is_flagged = True

        self.handle_flag(self.coordinates[0], self.coordinates[1])

    def draw_cell(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rectangle)
        if self.is_clicked:
            screen.blit(self.uncovered_image, self.rectangle.topleft)
            if self.value != 0:
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

        if is_hovered:
            if self.is_flagged == False and self.is_clicked == False:
                screen.blit(self.hover_image, self.rectangle.topleft)


class Board(Game):
    def __init__(self, rows, columns, mines, border_size=1):
        super().__init__(rows, columns, mines)
        self.title_text = "board"
        self.rows = rows
        self.columns = columns
        self.cell_size = calculate_cell_size(rows, columns)
        self.border_size = border_size
        self.width = columns * self.cell_size
        self.height = rows * self.cell_size
        self.cells = []
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
        self.draw_title("Hello", screen, fonts)
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
                        self.chord,
                        (row_index, column_index),
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
                    self.cells.append(cell)
                    cell.draw_cell(screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit_game", None
            if event.type == pygame.MOUSEBUTTONDOWN:
                coords = pygame.mouse.get_pos()
                row, column = coords[0] // self.cell_size, coords[1] // self.cell_size
                cell = self.cells[row * self.rows + column]
                if event.button == 1:
                    cell.reveal_cell()
                    cell.handle_chord(cell.coordinates[0], cell.coordinates[1])
                elif event.button == 3 and not cell.is_clicked:
                    cell.flag_cell()

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
        pygame.display.set_caption("Enjoy!!!")
        self.draw_cells(screen, fonts)
