import pygame
import sys
from GUI.gui_constants import WIDTH, HEIGHT
from .Board import Board
from .PlayerNamePage import PlayerNamePage
from .Difficulty import Difficulty
from .MainMenu import MainMenu
from .GameOver import GameOver
from .GameWin import GameWin
from .CustomDifficulty import CustomDifficulty
from .pause_menu import PauseMenu

class GUI:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Minesweeper")
        pygame.font.init()
        self.fonts = {
            "lg": pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 40),
            "md": pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 20),
            "sm": pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 15),
            "xs": pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 10),
        }
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    if kwargs and "name" in kwargs:
                        self.username = kwargs["name"]
                    current_page = MainMenu(self.username)
                case "pause_menu":
                    current_page = PauseMenu(
                        kwargs["rows"],
                        kwargs["columns"],
                        kwargs["mines"],
                        kwargs["board"]
                    )

                case "difficulty":
                    current_page = Difficulty()

                case "custom_difficulty":
                    current_page = CustomDifficulty()

                case "board":
                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    board = None
                    if kwargs and "board" in kwargs:
                        board = kwargs["board"]
                    current_page = Board(
                        kwargs["rows"],
                        kwargs["columns"],
                        kwargs["mines"],
                        board=board
                    )

                case "game_lose":
                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    current_page = GameOver(
                        self.username,
                        kwargs["rows"],
                        kwargs["columns"],
                        kwargs["mines"],
                    )
                case "game_win":
                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    current_page = GameWin(
                        self.username,
                        kwargs["rows"],
                        kwargs["columns"],
                        kwargs["mines"],
                    )
            current_page.update(self.screen, self.fonts)

            pygame.display.flip()
            self.clock.tick(60)
