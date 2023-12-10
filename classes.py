from helpers import validate_coordinates
from constants import BOARD_SIZE,NUMBER_OF_MINES

class Game:
    # difficulty "easy" | "medium" | "hard"
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board = []
        
        rows, columns = BOARD_SIZE[difficulty]
        for row in range(rows):
            self.board.append([])
            for column in range(columns):
                self.board[-1].append(Cell(row, column, False))



    def start_game(self):
        pass

    # (int, int) -> void
    # click the current cell with the given row, and conlumn coordinates. 
    # if covered, if not mine, just reveal it with the surrounding. If mine, declare game_lose, if  
    # if not convered, if the surrounding flags number matches with the number, click the rest cells
    def click_cell(self, row, column):
        pass

    # (int, int) -> void
    # The cell must be covered, toggle the flag on the cell
    def flag_cell(self, row, column):
        pass

    # (int, int) -> (listof int)
    # return the values of the surrounding cells of the given cell
    # use validate_coordinates
    def neighboring_cells(self, row, column):
        pass

    # (int, int) -> void
    # given the coordinates of the cell clicked first, create a board that must have the given cell with a non-mine value, then call click_cell to start the game
    # fill in the mines randomly, then fill in the number depending on the mines
    def create_board(self, row, column):
        pass

    # void -> void
    # create a grid-looking board of the current board
    # (0-8) -> the number, X for not opened cells, F for flagged cells, B for mines when losing the game
    def draw_board(self):
        rows, columns = BOARD_SIZE[self.difficulty]
            
        # Print First Row
        print('     ', end="")
        for column in range(columns):
            print(f'{(column + 1):^4}', end='')
        print()
        # print each row
        for row in range(rows):
            # Print Upper Border
            print('----' * (columns + 1))

            print(f'{(row + 1):^4}', end='')

            # Print The Row
            for column in range(columns):
                # Print the horizontal border for the first column
                if column == 0:
                    print('|', end='')


                # Print the value of the cell
                print(f' {self.board[row][column]} ', end='')
                # Print Horizontal Border
                print('|', end='')
            print()
        
        # Print Bottom Border
        print('----' * (columns + 1))


class Cell:
    def __init__(self, row, column, is_flagged, val=None, is_covered=True):
        self.row = row
        self.column = column
        self.is_flagged = is_flagged
        self.is_covered = is_covered
        self.val = val # None when game not started, "M" for mine , (0-8) for the number value

    def __str__(self):
        if self.val is not None or not self.is_covered: # return X for the uncalculated values (game not started) or when the cell is still covered
            return self.val
        return "X"


