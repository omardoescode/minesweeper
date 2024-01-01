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
from .PauseMenu import PauseMenu
from .CreditsPage import CreditsPage
from .MusicPlayer import MusicPlayer

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
        self.music_player = MusicPlayer()

    def start_game(self):
        current_page = PlayerNamePage()
        self.music_player.play_default_music()
        while True:
            action, kwargs = current_page.handle_events()

            match action:
                case "QUIT_GAME":
                    pygame.quit()
                    sys.exit()
                case "MAIN_MENU":
                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    if kwargs and "name" in kwargs:
                        self.username = kwargs["name"]
                    current_page = MainMenu(self.username)
                case "PAUSE_MENU":
                    current_page = PauseMenu(
                        kwargs["rows"],
                        kwargs["columns"],
                        kwargs["mines"],
                        kwargs["board"],
                        kwargs["state"]
                    )

                case "DIFFICULTY":
                    current_page = Difficulty()

                case "CUSTOM_DIFFICULTY":
                    current_page = CustomDifficulty()

                case "BOARD":
                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    board = None
                    if kwargs and "board" in kwargs:
                        board = kwargs["board"]
                    current_page = Board(
                        kwargs["rows"],
                        kwargs["columns"],
                        kwargs["mines"],
                        self.music_player,
                        board=board
                    )
                    self.music_player.play_board_music()

                case "GAME_LOSE":
                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    current_page = GameOver(
                        self.username,
                        kwargs["rows"],
                        kwargs["columns"],
                        kwargs["mines"],
                    )
                    self.music_player.play_losing_music()
                case "GAME_WIN":
                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    current_page = GameWin(
                        self.username,
                        kwargs["rows"],
                        kwargs["columns"],
                        kwargs["mines"],
                    )
                    self.music_player.play_winning_music()
                case "CREDITS":
                    current_page = CreditsPage()
            current_page.update(self.screen, self.fonts)

            pygame.display.flip()
            self.clock.tick(60)
