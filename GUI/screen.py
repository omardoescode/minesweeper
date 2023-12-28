import pygame
import sys
from gui_constants import WIDTH, HEIGHT
from GUI.Board import Board
from GUI.PlayerNamePage import PlayerNamePage
from GUI.Difficulty import Difficulty
from GUI.MainMenu import MainMenu
from GUI.GameOver import GameOver
from GUI.GameWin import GameWin
from GUI.CustomDifficulty import CustomDifficulty


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
                    if kwargs and "name" in kwargs:
                        self.username = kwargs["name"]
                    current_page = MainMenu(self.username)
                case "difficulty":
                    current_page = Difficulty()
                case "custom_difficulty":
                    current_page = CustomDifficulty()
                case "board":
                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    current_page = Board(
                        kwargs["rows"],
                        kwargs["columns"],
                        kwargs["mines"],
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
