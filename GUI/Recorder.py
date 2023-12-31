class Recorder:
    def __init__(self):
        self.steps = []
        self.undone_steps = []  # Will be reduced to zero once the recording is finished
        self.board = []

    def add_step(self, row, column, action):
        # Check Action value
        if action not in ["click", "flag"]:
            raise Exception("A step can either be a click or a flag")

        # Adding a new step
        new_step = Step(row, column, action)
        self.steps.append(new_step)
        self.undone_steps.append(new_step)

    # () -> (listof Step)
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

    # () -> Recorder
    # Return a new recorder in which it has the same steps and the same board but has all cells covered and unflagged
    def restart(self):
        steps = self.steps

        # Initiate the new recorder and set the board
        new_recorder = Recorder()
        new_recorder.set_board(self.board.copy())  # Unflag and cover all cells
        new_recorder.steps = steps.copy()
        new_recorder.undone_steps = steps.copy()  # Restart the steps
        # ! If we don't assign it as a copy, we won't be allowed for more than one replay, since they will have the same address, and get_next_step will erase all steps in the first replay
        # ? Mutation?
        # Return the new recorder
        return new_recorder

    # () -> ()
    # a helper function for debugging the recorder functionality
    def print_steps(self):
        print(", ".join(self.steps))


class Step:
    # Invariant: action will always either be "click" "flag"
    # "flag" stands for either flagging or unflagged
    # "click" stands for either revealing or chording
    def __init__(self, row, column, action):
        self.row = row
        self.column = column
        self.action = action

    def __str__(self):
        return f"{self.action} in {self.row}x{self.column}"

    def get_coordinates(self):
        return self.row, self.column
