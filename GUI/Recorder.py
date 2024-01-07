class Recorder:
    def __init__(self):
        self.steps = []
        self.board = []

    def add_step(self, row, column, action):
        new_step = Step(row, column, action)
        print(new_step)  # Display the steps info in the console
        self.steps.append(new_step)

    def get_steps(self):
        return self.steps

    def set_board(self, board):
        self.board = board


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
