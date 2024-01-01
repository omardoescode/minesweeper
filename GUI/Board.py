import pygame
from classes import Game
from GUI.gui_constants import PRIMARY_COLOR, TOP_MARGIN, SECONDARY_COLOR
from GUI.gui_helpers import calculate_cell_size, get_page_coordinates, create_button, started_playing
from GUI.flag_counter import FlagCounter
from timer import Timer
from GUI.MusicPlayer import MusicPlayer
from GUI.scorer import Scorer

class GUICell:
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
        stop_input,
        flag_counter,
        music_player
    ):
        # Initlaize the cell object, saving all given parameters
        self.coordinates = coordinates
        self.cell_size = cell_size
        self.border_size = border_size
        self.value = value
        self.handle_lose = handle_lose
        self.handle_flag = handle_flag
        self.handle_click = handle_click
        self.handle_chord = handle_chord
        self.rectangle = pygame.Rect(
            self.border_size + self.cell_size * self.coordinates[1],
            self.border_size + self.cell_size * self.coordinates[0] + TOP_MARGIN,
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
        self.stop_input = stop_input
        self.flag_counter = flag_counter
        self.music_player = music_player

    # () -> ()
    # Reveal the cell. Start losing animation if it was mine
    def reveal_cell(self):
        self.music_player.play_dig_sound(channel=1)
        self.handle_click(self.coordinates[0], self.coordinates[1])
        
        if self.value == "M":
            self.stop_input()
            pygame.time.set_timer(pygame.USEREVENT + 1, 250)

        self.is_clicked = True

    # () -> ()
    # Toggle the flag state of the cell. Increase the counter of the flag or derease
    def flag_cell(self):
        self.music_player.play_flag_sound(channel=2)
        self.is_flagged = not self.is_flagged

        if self.is_flagged:
            self.flag_counter.place_flag()
        else:
            self.flag_counter.remove_flag()

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

        coords = pygame.mouse.get_pos()
        column, row = coords[0]//self.cell_size, (coords[1]-TOP_MARGIN)//self.cell_size

        is_hovered = self.coordinates[0] == row and self.coordinates[1] == column

        if is_hovered:
            if self.is_flagged == False and self.is_clicked == False:
                screen.blit(self.hover_image, self.rectangle.topleft)


class Board(Game):
    def __init__(self, rows, columns, mines, music_player, board=None, border_size=1):
        # Initilaize the inherited game object
        super().__init__(rows, columns, mines)

        # Initilaize the object
        self.title_text = "board"
        self.rows = rows
        self.columns = columns
        self.cell_size = calculate_cell_size(rows, columns)
        self.border_size = border_size
        self.stop_input = False
        self.music_player = music_player
        self.width = columns * self.cell_size
        self.height = rows * self.cell_size + TOP_MARGIN
        self.cells = ['X']*(self.columns*self.rows)
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Initalize the timer
        self.timer = Timer()
        self.timer.start() # start the timer

        # Initalize the flag counter
        self.flag_counter = FlagCounter(self.mines)

        # Initalize the score
        self.scorer = Scorer()

        # Initlaize the board given
        if board:
            self.start_playing = True
            self.board = board

        # Load the background
        self.background = pygame.image.load('./assets/background.png')

        # Load the images of the cells
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

        # Load the images of the sidebar
        self.TB_flag_image = pygame.transform.scale(
            pygame.image.load("./assets/in_game_icons/board/red-flag.png"),
            (30, 30),
        )

        self.TB_timer_image = pygame.transform.scale(
            pygame.image.load("./assets/in_game_icons/clock.png"),
            (30, 30),
        )

    def handle_stop_input(self):
        self.stop_input = True

    # Draw the board
    def draw_cells(self, screen):
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
                cell = GUICell(
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
                    self.handle_stop_input,
                    self.flag_counter,
                    self.music_player
                )
                self.cells[row_index*self.columns + column_index] = cell
                cell.draw_cell(screen) 
    
    # Draw an item in the siderbar
    def draw_siderbar_item(self, screen, font, text, x, y, icon=None):
        # Assuming screen is the Pygame surface
        screen_width = screen.get_width()

        # Adjust x to be relative to the right of the screen
        x_relative_to_right = screen_width - x

        bg_rect = pygame.Rect(x_relative_to_right, y, 150, 30)
        pygame.draw.rect(screen, SECONDARY_COLOR, bg_rect)

        text_surface = font.render(text, True, (0, 0, 0))
        
        # Adjust text_rect to be relative to the right of bg_rect
        text_rect = text_surface.get_rect(center=bg_rect.center)

        screen.blit(text_surface, text_rect.topleft)

        # Adding the icon
        if icon:
            screen.blit(icon, bg_rect.topleft)

    def draw_topbar(self, screen, fonts):
        # TODO: Change the time and flag text to some icons to be placed with them
        # TODO: change the font from xs to sm after implementing so
        # Timer
        time = f"{self.timer.get_elapsed_time():.0f}s"
        self.draw_siderbar_item(screen, fonts["sm"], time, 150, 40, self.TB_timer_image)

        # Score
        score = f"Score: {self.scorer.calculate_score(self.get_revealed_cells(), self.timer.get_elapsed_time())} XP"
        self.draw_siderbar_item(screen, fonts["xs"], score, 300 + 10, 40)

        # Flag Counter
        flags = f"{self.flag_counter.get_remaining_flags()}"
        self.draw_siderbar_item(screen, fonts["sm"], flags, 450 + 20, 40, self.TB_flag_image)

        self.menu = self.draw_button("Pause", (10, 30), screen, fonts)
        

    def draw_button(self, text, position, screen, fonts, handle_click=lambda: None):
        return create_button(
            position[0],
            position[1],
            120,
            50,
            text,
            (255, 255, 255),
            SECONDARY_COLOR,
            (0, 0, 0),
            screen,
            fonts,
            handle_click,
        )
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT_GAME", None

            # Handle Pause Menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.start_playing:
                    state = "didn't_start"
                elif self.playing:
                    state = "playing"
                else:
                    state = "over"
                if self.menu.collidepoint(event.pos):
                    return "PAUSE_MENU", {"rows": self.rows, "columns": self.columns, "mines": self.mines, "board": self.board, "state": state}

            # Handle clicking on cells
            if event.type == pygame.MOUSEBUTTONDOWN and not self.stop_input:
                coords = pygame.mouse.get_pos()

                # This if statement aims to prevent a bug
                # The bug is that it gives a negative index to the board list, causing it to dig the last row of cells
                if coords[1] >= TOP_MARGIN:
                    column, row = coords[0]//self.cell_size, (coords[1] - TOP_MARGIN)//self.cell_size
                    cell = self.cells[row*self.columns + column]
                    if event.button == 1 and not cell.is_flagged:
                            cell.reveal_cell()
                            cell.handle_chord(cell.coordinates[0], cell.coordinates[1])

                            if (self.start_playing and self.check_win()) or (not self.playing):
                                pygame.time.set_timer(pygame.USEREVENT+1, 250)
                                self.stop_input = True
                                self.timer.end()

                    elif event.button == 3 and not cell.is_clicked:
                        cell.flag_cell()

            if event.type == (pygame.USEREVENT+1):
                uncovered_mines = list(filter(lambda cell: cell.value == "M" and cell.is_clicked == False, self.cells))
                if len(uncovered_mines) > 0:
                    self.music_player.play_beep_sound(channel=len(uncovered_mines)+2)
                    next_mine = uncovered_mines[0]
                    row_index, column_index = next_mine.coordinates[0], next_mine.coordinates[1]
                    self.board[row_index][column_index].is_flagged = False
                    self.board[row_index][column_index].is_covered = False
                    pygame.time.set_timer(pygame.USEREVENT + 1, int(250*(len(uncovered_mines)/self.mines)))
                else:
                    pygame.time.set_timer(pygame.USEREVENT+1, 0)
                    pygame.time.set_timer(pygame.USEREVENT+2, 1500)

            if event.type == pygame.USEREVENT + 2:
                pygame.time.set_timer(pygame.USEREVENT+2, 0)
                if self.start_playing and self.check_win():
                    return "GAME_WIN", {
                        "rows": self.rows,
                        "columns": self.columns,
                        "mines": self.mines,
                        "cell_size": self.cell_size,
                    }

                if not self.playing:
                    return "GAME_LOSE", {
                        "rows": self.rows,
                        "columns": self.columns,
                        "mines": self.mines,
                        "cell_size": self.cell_size,
                    }
            
        return None, None

    def update(self, screen, fonts):
        screen.blit(self.background, (0, 0))
        pygame.display.set_caption("Enjoy!!!")
        self.draw_topbar(screen, fonts)
        self.draw_cells(screen)
