import pygame
from GUI.gui_helpers import create_button
from GUI.gui_constants import WIDTH, HEIGHT, PRIMARY_COLOR, SECONDARY_COLOR


class MainMenu:
    def __init__(self, username, music_player):
        self.title_text = "Minesweeper Main Menu"
        self.username = username
        self.music_player = music_player

        self.navigation_buttons = []  # {obj: button, val: "Navigation Button", kwargs}
        self.background = pygame.transform.scale(pygame.image.load('./assets/background.png'), (WIDTH, HEIGHT))

    def handle_events(self):
        for event in pygame.event.get():
            # Check for quitting the game
            if event.type == pygame.QUIT:
                return "QUIT_GAME", None
            
            # Check if clicking buttons
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for btn in self.navigation_buttons:
                    if btn["obj"].collidepoint(event.pos):
                        return btn["val"], btn["kwargs"]
                
                # Checking if the button is mute button
                if self.toggle_mute_btn.collidepoint(event.pos):
                    self.music_player.toggle_mute_music()

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
            SECONDARY_COLOR,
            (0, 0, 0),
            screen,
            fonts,
            handle_click,
        )
    
    def draw_small_button(self, text, position, screen, fonts, handle_click=lambda: None):
        return create_button(
            position[0] - 60,
            position[1] + 25,
            120,
            50,
            text,
            (255, 255, 255),
            SECONDARY_COLOR,
            (0, 0, 0),
            screen,
            fonts,
            handle_click,
            text_size="sm"
        )

    def update(self, screen, fonts):
        pygame.display.set_caption(self.title_text)
        screen.blit(self.background, (0, 0))


        # Draw Header
        self.draw_title(
            "Welcome to", screen, fonts["sm"], WIDTH / 2, HEIGHT / 3 - 40
        )
        self.draw_title("Minesweeper", screen, fonts["lg"], WIDTH / 2, HEIGHT / 3)
        self.draw_title(
            f"Hello, {self.username}", screen, fonts["sm"], WIDTH / 2, HEIGHT / 3 + 40
        )

        # Draw Buttons
        game_start = self.draw_button(
            "Game Start", (WIDTH // 2, HEIGHT // 3 + 40), screen, fonts
        )
        self.navigation_buttons.append(
            {"obj": game_start, "val": "DIFFICULTY", "kwargs": None}
        )
        # TODO: Handle the Stats functionailty
        stats_button = self.draw_button("Stats", (WIDTH // 2, HEIGHT // 3 + 160), screen, fonts)
        self.navigation_buttons.append(
            {"obj": stats_button, "val": "STATS", "kwargs": None}
        )

        quit_button = self.draw_button(
            "Quit", (WIDTH // 2, HEIGHT // 3 + 280), screen, fonts
        )
        self.navigation_buttons.append(
            {"obj": quit_button, "val": "QUIT_GAME", "kwargs": {}}
        )
    
        # Draw About Page
        about_btn = self.draw_small_button(
            "About", (WIDTH - 80, HEIGHT - 100), screen, fonts
        )
        self.navigation_buttons.append(
            {"obj": about_btn, "val": "ABOUT", "kwargs": {}}
        )
        
        # Draw Mute/Unmute button
        toggle_mute_text = "Unmute" if self.music_player.is_muted else "Mute"
        self.toggle_mute_btn = self.draw_small_button(
            toggle_mute_text, (WIDTH - 80, HEIGHT - 160), screen, fonts
        )