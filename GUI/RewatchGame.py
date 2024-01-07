from .Board import Board
import pygame


class RewatchGame(Board):
    def __init__(
        self, rows, columns, mines, music_player, username, difficulty, recorder
    ):
        super().__init__(
            rows=rows,
            columns=columns,
            mines=mines,
            music_player=music_player,
            difficulty=difficulty,
            username=username,
            board=recorder.board,
        )
        self.recorder = recorder
        self.start_time = pygame.time.get_ticks()

    # We will modify this handle_events function to allow only for quitting the game and cliking the pause game
    # TODO: Pass the recorder to pause menu to continue later
    def handle_events(self):
        for event in pygame.event.get():
            # Quitting the game
            if event.type == pygame.QUIT:
                return "QUIT_GAME", None

            # Clicking teh menu button
            if event.type == pygame.MOUSEBUTTONDOWN and self.menu.collidepoint(
                event.pos
            ):
                # Handle the stat variable
                if not self.start_playing:
                    state = "didn't_start"
                elif self.playing:
                    state = "playing"
                else:
                    state = "over"
                return "PAUSE_MENU", {
                    "rows": self.rows,
                    "columns": self.columns,
                    "mines": self.mines,
                    "board": self.board,
                    "state": state,
                    "difficulty": self.difficulty,
                    "initial_time": self.timer.get_elapsed_time(),
                }

        # Redirect to the same game when finishing the recording after a 500s
        current_time = pygame.time.get_ticks()
        end_time = self.start_time + 1000
        if self.recorder.finishied_replaying() and current_time >= end_time:
            if self.check_win():
                return "GAME_WIN", {
                    "rows": self.rows,
                    "columns": self.columns,
                    "mines": self.mines,
                    "difficulty": self.difficulty,
                    "recorder": self.recorder,
                }
            else:  # We pass a finished game, so if check_win returns false, he lost, not pause
                return "GAME_LOSE", {
                    "rows": self.rows,
                    "columns": self.columns,
                    "mines": self.mines,
                    "difficulty": self.difficulty,
                    "recorder": self.recorder,
                }

        return None, None

    # Make the recorder works
    def run_record(self):
        step = self.recorder.get_next_step()
        if step is not None:
            row, column = step.get_coordinates()
            cell = self.cells[row * self.columns + column]
            if step.action == "click":
                cell.reveal_cell()

            elif step.action == "flag":
                cell.flag_cell()

    # () -> Boolean
    # return true if the difference between current time and start time is 1000 ms (1s)
    def do_next_step(self):
        current_time = pygame.time.get_ticks()
        end_time = self.start_time + 500
        if current_time >= end_time:
            self.start_time = current_time
            return True

        return False

    # Inherit the update function alongside running the record
    def update(self, screen, fonts):
        super().update(screen, fonts)

        if not self.recorder.finishied_replaying() and self.do_next_step():
            self.run_record()
