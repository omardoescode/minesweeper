import pygame

class PauseMenu:
    def __init__(self, rows, columns, mines, board, state):
        if state == "over":
            self.buttons = [
                {"text": "Restart", "action": "board", "kwargs": {"rows": rows, "columns": columns, "mines": mines}}
            ]
        elif state == "didn't_start":
            self.buttons = [
                {"text": "Continue", "action": "board", "kwargs": {"rows": rows, "columns": columns, "mines": mines}}
            ]
        else:
            self.buttons = [
                {"text": "Continue", "action": "board", "kwargs": {"rows": rows, "columns": columns, "mines": mines, "board": board}}
            ]
        self.buttons +=[
            {"text": "Main Menu", "action": "main_menu", "kwargs": None},
            {"text": "Quit", "action": "quit_game", "kwargs": None},
        ]
        self.selected_button = 0

    def draw_menu(self, screen, fonts):
        screen.fill((0, 0, 0))  # Background color

        # Display buttons
        button_spacing = 40
        y = screen.get_height() // 3
        for idx, button in enumerate(self.buttons):
            text = fonts["md"].render(button["text"], True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() // 2, y))
            screen.blit(text, text_rect)
            y += button_spacing

            # Highlight selected button
            if idx == self.selected_button:
                pygame.draw.rect(
                    screen, (255, 255, 255), text_rect, 3
                )  # Draw rectangle around the selected button

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit_game", None
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
                    selected_button = self.buttons[self.selected_button]
                    return selected_button["action"], selected_button["kwargs"]

        return None, None
    

    def update(self, screen, fonts):
        screen.fill((0, 0, 0))

        self.draw_menu(screen, fonts)


