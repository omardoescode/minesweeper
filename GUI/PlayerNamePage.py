import pygame
from gui_helpers import create_button
from gui_constants import WIDTH, HEIGHT, PRIMARY_COLOR


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
                return "quit_game", None
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
