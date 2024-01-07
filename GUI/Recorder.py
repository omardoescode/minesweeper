class Recorder:
    def __init__(self):
        self.steps = []
        self.undone_steps = []  # Will be reduced to zero once the recording is finished
        self.board = []

    def add_step(self, row, column, action):
        new_step = Step(row, column, action)
        self.steps.append(new_step)
        self.undone_steps.append(new_step)

    def get_steps(self):
        return self.steps

    def set_board(self, board):
        # Unreveal all the cells
        for row in board:
            for cell in row:
                cell.is_covered = True
                cell.is_flagged = False

        # Set the board
        self.board = board

    # () -> Step
    # Return the next step, None when all are shows
    def get_next_step(self):
        if not self.undone_steps:
            return None

        step = self.undone_steps.pop(0)
        return step

    def finishied_replaying(self):
        return not self.undone_steps


class Step:
    # Invariant: action will always either be "click" "flag"
    # "flag" stands for either flagging or unflagged
    # "click" stands for either revealing or chording
    def __init__(self, row, column, action):
        self.row = row
        self.column = column
        self.action = action
        self.shown = False  # True when revealed to the user in the RewatchGame Page

    def __str__(self):
        return f"{self.action} in {self.row}x{self.column}"

    def get_coordinates(self):
        return self.row, self.column
