import pygame
from pygame.locals import QUIT


class PauseMenu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.buttons = [
            {"text": "Continue", "action": "continue"},
            {"text": "Main Menu", "action": "main_menu"},
            {"text": "Quit", "action": "quit"},
        ]
        self.selected_button = 0

    def draw_menu(self):
        self.screen.fill((0, 0, 0))  # Background color

        # Display buttons
        button_spacing = 40
        y = 200
        for idx, button in enumerate(self.buttons):
            text = self.font.render(button["text"], True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.screen.get_width() // 2, y))
            self.screen.blit(text, text_rect)
            y += button_spacing

            # Highlight selected button
            if idx == self.selected_button:
                pygame.draw.rect(
                    self.screen, (255, 255, 255), text_rect, 3
                )  # Draw rectangle around the selected button

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_button = (self.selected_button - 1) % len(
                        self.buttons
                    )
                elif event.key == pygame.K_DOWN:
                    self.selected_button = (self.selected_button + 1) % len(
                        self.buttons
                    )
                elif event.key == pygame.K_RETURN:
                    return self.buttons[self.selected_button]["action"]

        return None
