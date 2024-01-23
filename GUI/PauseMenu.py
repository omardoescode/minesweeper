import pygame


class PauseMenu:
    def __init__(
        self,
        rows,
        columns,
        mines,
        board,
        difficulty,
        state,
        initial_time,
    ):
        page_back = "BOARD"
        if state == "over":
            self.buttons = []
        elif state == "didn't_start":
            self.buttons = [
                {
                    "text": "Continue",
                    "action": page_back,
                    "kwargs": {
                        "difficulty": difficulty,
                        "rows": rows,
                        "columns": columns,
                        "mines": mines,
                        "initial_time": initial_time,
                    },
                }
            ]
        else:
            self.buttons = [
                {
                    "text": "Continue",
                    "action": page_back,
                    "kwargs": {
                        "difficulty": difficulty,
                        "rows": rows,
                        "columns": columns,
                        "mines": mines,
                        "board": board,
                        "initial_time": initial_time,
                    },
                }
            ]

        # Common buttons on all cases
        self.buttons += [
            {
                "text": "Restart",
                "action": "BOARD",  # Restart button will play a new game, whether you are in RewatchGame or in Board Page
                "kwargs": {
                    "difficulty": difficulty,
                    "rows": rows,
                    "columns": columns,
                    "mines": mines,
                },
            },
            {"text": "Main Menu", "action": "MAIN_MENU", "kwargs": None},
            {"text": "Quit", "action": "QUIT_GAME", "kwargs": None},
        ]
        self.selected_button = 0

    def draw_menu(self, screen, fonts):
        screen.fill((0, 0, 0))  # Background color

        # Display buttons
        button_spacing = 40
        y = screen.get_height() // 3  # First Button Y coordinate
        for idx, button in enumerate(self.buttons):
            text = fonts["md"].render(button["text"], True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() // 2, y))
            screen.blit(text, text_rect)
            y += button_spacing  # Add the y coordinate for the next one

            # Add the text_rectangle to the buttons, for handling clicking later
            button["obj"] = text_rect

            # Highlight selected button
            if idx == self.selected_button:
                pygame.draw.rect(
                    screen, (255, 255, 255), text_rect, 3
                )  # Draw rectangle around the selected button

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT_GAME", None
            # Handle Pressing the keyboard
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

            # Handle Mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button["obj"].collidepoint(event.pos):
                        return button["action"], button["kwargs"]

        return None, None

    def update(self, screen, fonts):
        screen.fill((0, 0, 0))

        self.draw_menu(screen, fonts)
