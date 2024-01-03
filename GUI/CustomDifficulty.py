import pygame
from GUI.gui_helpers import create_button
from GUI.gui_constants import WIDTH, HEIGHT, PRIMARY_COLOR, SECONDARY_COLOR


class CustomDifficulty:
    def __init__(self):
        self.title_text = "Enter Difficulty"
        self.submit_button = pygame.Rect(0, 0, 0, 0)
        self.inputs = []
        self.submit_button = pygame.Rect(0, 0, 0, 0)
        self.header = "Enter the rows, columns, and mines"
        self.bacground = pygame.transform.scale(pygame.image.load('./assets/background.png'), (WIDTH, HEIGHT))

        # Gathering info about buttons
        info = ["rows", "columns", "mines"]

        self.y = HEIGHT // 2
        for input in info:
            self.inputs.append(
                {
                    "obj": pygame.Rect(WIDTH // 2 - 200, self.y, 400, 50),
                    "label": input,
                    "is_active": False,
                    "val": "",
                }
            )
            self.y += 80
        # {obj: rect, val: rows | columns | mines}

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit_game", None
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Handle Submit Click
                if self.submit_button.collidepoint(event.pos):
                    values = {"rows": 0, "columns": 0, "mines": 0}
                    # Validate values
                    for input in self.inputs:
                        # Hanlde rows, and columns
                        if input["label"] != "mines":
                            value = input["val"]
                            if value == "" or int(value) > 30 or int(value) < 3:
                                self.header = "Rows, and columsn values have to be between 3 and 30"
                                break
                            values[input["label"]] = int(value)
                        # Handle mins
                        else:
                            value = input["val"]
                            max_value = values["rows"] * values["columns"] // 2
                            if value == "" or int(value) < 3:
                                self.header = (
                                    f"Mines value has to be between 3 and {max_value}"
                                )
                                break
                            values[input["label"]] = int(value)
                    else:
                        return "BOARD", values

                for input in self.inputs:
                    # Make it active
                    if input["obj"].collidepoint(event.pos):
                        input["is_active"] = True
                    # make the rest unactive
                    else:
                        input["is_active"] = False
            elif event.type == pygame.KEYDOWN:
                for input in self.inputs:
                    if input["is_active"]:
                        # Handle backspace
                        if event.key == pygame.K_BACKSPACE and input["val"] != "":
                            input["val"] = input["val"][:-1]
                        # Handle numbers
                        elif event.unicode.isnumeric():
                            # Handle Min and Max Values
                            # The minimum values must be 3, 3 for rows, columns, max are 30, 30
                            # and mines have to be 3 < mines <= rows * columns // 2
                            new_value = int(input["val"] + event.unicode)
                            label = input["label"]
                            if label != "mines":  # Handle rows, and columns
                                if new_value > 30:
                                    new_value = 30
                            else:  # Handle mines
                                # Retireve the current rows, and columsn values
                                rows, columns = 0, 0
                                for input in self.inputs:
                                    if input["label"] == "rows":
                                        rows = (
                                            0
                                            if input["val"] == ""
                                            else int(input["val"])
                                        )
                                    if input["label"] == "columns":
                                        columns = (
                                            0
                                            if input["val"] == ""
                                            else int(input["val"])
                                        )

                                if new_value > rows * columns // 2:
                                    new_value = rows * columns // 2

                            input["val"] = str(new_value)

        return None, None

    def draw_inputs_boxes(self, screen, fonts, label):
        for input in self.inputs:
            obj, label, is_active, val = input.values()
            # Draw the input
            pygame.draw.rect(screen, (255, 255, 255), obj)

            # Determining the value
            if str(val) != "":
                value = str(val)
            elif is_active:
                value = val
            else:
                value = label 

            # Draw the text
            text_surface = fonts["md"].render(value, False, (0, 0, 0))
            text_rect = text_surface.get_rect(center=obj.center)
            screen.blit(text_surface, text_rect.topleft)

    def draw_submit_button(self, screen, fonts):
        self.submit_button = create_button(
            WIDTH // 2,
            self.y,
            200,
            50,
            "Submit",
            (255, 255, 255),
            SECONDARY_COLOR,
            (0, 0, 0),
            screen,
            fonts,
        )

    def update(self, screen, fonts):
        pygame.display.set_caption(self.title_text)
        screen.blit(self.bacground, (0, 0))

        text_surface = fonts["md"].render(self.header, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(text_surface, text_rect.topleft)

        self.draw_inputs_boxes(screen, fonts, input)
        self.draw_submit_button(screen, fonts)
