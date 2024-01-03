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
from .AboutPage import AboutPage
from .MusicPlayer import MusicPlayer
from .Stats import Stats

class GUI:
    def __init__(self):
        # Initlizing the game with the defailt settings
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

    # This function handles the game with all the navigation, and playing background music
    def start_game(self):
        self.username = "Omar"
        current_page = MainMenu(self.username, self.music_player)
        self.music_player.play_default_music() # Start the music right away
        while self.running:
            action, kwargs = current_page.handle_events()

            match action:
                case "QUIT_GAME":
                    self.running = False
                    pygame.quit()
                    sys.exit()
                case "MAIN_MENU":
                    # Reset the screen coordinates
                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

                    # Check for username value
                    if kwargs and "name" in kwargs:
                        self.username = kwargs["name"]
                    current_page = MainMenu(self.username, self.music_player)
                    
                    # This code will run when navigating from board to main menu
                    # As the music changes, so cannot continue the music from player page name
                    if not self.music_player.check_default_music():
                        self.music_player.play_default_music() 
                case "PAUSE_MENU":
                    current_page = PauseMenu(**kwargs)

                case "DIFFICULTY":
                    current_page = Difficulty()

                case 'STATS':
                    current_page = Stats(self.username)

                case "CUSTOM_DIFFICULTY":
                    current_page = CustomDifficulty()

                case "BOARD":
                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    board = None
                    
                    # Check if coming from pause menu, where board value exists
                    if kwargs and "board" in kwargs:
                        board = kwargs["board"]

                    current_page = Board(
                        kwargs["rows"],
                        kwargs["columns"],
                        kwargs["mines"],
                        self.music_player,
                        self.username,
                        kwargs.get('difficulty', 'custom'),
                        board=board,
                        initial_time=kwargs.get('initial_time', 0)
                    )

                    # Play the board music
                    self.music_player.play_board_music()

                case "GAME_LOSE":
                    # Reset the coordiantes
                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

                    current_page = GameOver(
                        self.username,
                        **kwargs
                    )
                    self.music_player.play_losing_music()
                case "GAME_WIN":
                    # Reset the coordiantes
                    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

                    current_page = GameWin(
                        self.username,
                        **kwargs
                    )
                    self.music_player.play_winning_music()
                case "ABOUT":
                    current_page = AboutPage()
            current_page.update(self.screen, self.fonts)

            pygame.display.flip()
            self.clock.tick(60)
