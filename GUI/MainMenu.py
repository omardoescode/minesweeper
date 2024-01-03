import pygame
from .gui_helpers import create_button
from .gui_constants import WIDTH, HEIGHT
from .save_game import check_game, retrieve_game


class MainMenu:
    def __init__(self, username, music_player):
        self.title_text = "Minesweeper Main Menu"
        self.username = username
        self.music_player = music_player

        self.background = pygame.transform.scale(pygame.image.load('./assets/background.png'), (WIDTH, HEIGHT))
        self.navigation_buttons = []  # {obj: button, val: "Navigation Button", kwargs}

        # Loading Images
        self.title_image = pygame.transform.scale(pygame.image.load("./assets/title.png"), (550, 100))

        self.btn_bg = pygame.transform.scale(pygame.image.load("./assets/buttons/menu_butt1.png"), (300, 200))

        self.play_text = pygame.transform.scale(pygame.image.load("./assets/text/play.png"), (100, 50))
        self.continue_text = pygame.transform.scale(pygame.image.load("./assets/text/continue.png"), (200, 50))
        self.stats_text = pygame.transform.scale(pygame.image.load("./assets/text/stats.png"), (150, 50))
        self.quit_text = pygame.transform.scale(pygame.image.load("./assets/text/quit.png"), (150, 50))

        self.unmuted = pygame.transform.scale(pygame.image.load("./assets/icons/music-on-icon.png"), (50, 50))
        self.muted = pygame.transform.scale(pygame.image.load("./assets/icons/music-off-icon.png"), (50, 50))
        self.about = pygame.transform.scale(pygame.image.load("./assets/icons/aboutus-icon.png"), (50, 50))

        self.buttons = [
            {
            "text_image": self.play_text,
            "val": "DIFFICULTY",
            "kwargs": {}
            },
            {
            "text_image": self.stats_text,
            "val": "STATS",
            "kwargs": {}
            },
            {
            "text_image": self.quit_text,
            "val": "QUIT_GAME",
            "kwargs": {}
            },
        ]
        if check_game(self.username):
            self.buttons = [{"text_image": self.continue_text, "val": "BOARD", "kwargs": retrieve_game(self.username)}] + self.buttons


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

    def place_img(self, img, screen, x, y):
        img_rect = img.get_rect(center=(x, y))
        screen.blit(img, img_rect.topleft)

        return img_rect
    
    def place_button(self, bg, text, screen, x, y):
        bg_rect = bg.get_rect(center=(x, y))
        text_rect = text.get_rect(center=(bg_rect.midtop[0], bg_rect.midtop[1] + 85))
        screen.blit(bg, bg_rect.topleft)
        screen.blit(text, text_rect.topleft)

        return text_rect
    
    def update(self, screen, fonts):
        pygame.display.set_caption(self.title_text)
        screen.blit(self.background, (0, 0))


        # Draw Header
        self.draw_title(
            "Welcome to", screen, fonts["sm"], WIDTH / 2, HEIGHT / 5 - 60
        )
        # self.draw_title("Minesweeper", screen, fonts["lg"], WIDTH / 2, HEIGHT / 3)
        self.place_img(self.title_image, screen, WIDTH / 2, HEIGHT / 5)
        self.draw_title(
            f"Dig in, {self.username}", screen, fonts["sm"], WIDTH / 2, HEIGHT / 5 + 60
        )

        

        n = 5
        y = 140
        for btn_data in self.buttons:
            btn = self.place_button(self.btn_bg, btn_data["text_image"], screen, WIDTH // n, HEIGHT // 5 + y)
            self.navigation_buttons.append({"obj": btn, "val": btn_data["val"], "kwargs": btn_data["kwargs"]})
            n -= 1
            y += 120
        
        # Draw About Page
        about_btn = self.place_img(self.about, screen, WIDTH - 50, HEIGHT - 100)
        self.navigation_buttons.append(
            {"obj": about_btn, "val": "ABOUT", "kwargs": {}}
        )
        # Draw Mute/Unmute button
        icon = self.muted if self.music_player.is_muted else self.unmuted
        self.toggle_mute_btn = self.place_img(icon, screen, WIDTH - 50, HEIGHT - 50)