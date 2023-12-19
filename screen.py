import pygame
import sys
from classes import Game, Cell
from gui_helpers import create_button
from gui_constants import HEIGHT, WIDTH, PRIMARY_COLOR


class GUI(Game):
    def __init__(self, rows, columns, mines):
        super().__init__(rows, columns, mines)
        pygame.init()
        pygame.display.set_caption("Minesweeper")
        pygame.font.init()
        self.fonts = {
            "xl": pygame.font.Font("assets/PressStart2P-Regular.ttf", 60),
            "lg": pygame.font.Font("assets/PressStart2P-Regular.ttf", 40),
            "md": pygame.font.Font("assets/PressStart2P-Regular.ttf", 20),
            "sm": pygame.font.Font("assets/PressStart2P-Regular.ttf", 10),
        }
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def start_game(self):
        current_page = HomePage(self.screen, self.fonts)

        while True:
            action = current_page.handle_events()

            # Handle Navigation Functionality
            if action == "Board":
                current_page = Board(self.screen, self.fonts)
            elif action == "HomePage":
                current_page = HomePage(self.screen, self.fonts)

            current_page.update()

            pygame.display.flip()
            self.clock.tick(60)


class HomePage:
    def __init__(self, screen, fonts):
        self.title_text = "Minesweeper Homepage"
        self.screen = screen
        self.fonts = fonts
        self.start_game_button = pygame.Rect(0, 0, 0, 0)

    def quit(self):
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.start_game_button.collidepoint(event.pos):
                    return "Board"

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
        # TODO: Handle the options functionailty
        self.draw_button("Option", (WIDTH // 2, HEIGHT // 3 + 160))
        self.draw_button("Quit", (WIDTH // 2, HEIGHT // 3 + 280), self.quit)

        self.start_game_button = game_start


class Board:
    def __init__(self, screen, fonts):
        self.title_text = "Board"
        self.screen = screen
        self.fonts = fonts
        self.homepage_button = pygame.Rect(0, 0, 0, 0)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.homepage_button.collidepoint(event.pos):
                    return "HomePage"  # Telling where this is heading later

    # Display the grid
    def update(self):
        pygame.display.set_caption("Enjoy!!!")
        self.screen.fill(PRIMARY_COLOR)

        # TODO
        # Desing the board funcitonality


# TODO
# Create a page to ask for name
