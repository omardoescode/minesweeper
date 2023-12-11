from helpers import validate_coordinates
from constants import BOARD_SIZE,NUMBER_OF_MINES
import random

class Game:
    # difficulty "easy" | "medium" | "hard"
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board = []
        
        rows, columns = BOARD_SIZE[difficulty]
        for row in range(rows):
            self.board.append([])
            for column in range(columns):
                self.board[-1].append(Cell(row, column, False, 0, False))



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
        if self.board[row][column].is_covered == True:
            self.board[row][column].is_flagged = not self.board[row][column].is_flagged

    # (int, int) -> (listof Cell)
    # return a list of the surrounding cells of the given cell
    # use validate_coordinates
    def neighboring_cells(self, row, column):
        neighbors = []

        # Looping through the 8 neighboring cells positions with respect to current cell
        # Format = (row, column)
        for position in [(0,1), (0,-1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]:
            neighbor_row = row + position[0]
            neighbor_column = column + position[1]

            # Checking if the position represents a valid index in the board
            # This check is mainly useful for the cells present on the edges of the board
            if validate_coordinates(neighbor_row, neighbor_column, BOARD_SIZE[self.difficulty]):
                neighbors.append(self.board[neighbor_row][neighbor_column])

        return neighbors
    
    # (int, int) -> int
    # Return the count of neighboring mines
    # Should be used in create_board only    
    def count_neighboring_mines(self, row, column):
        return len(list(filter(lambda cell: cell.val == "M", self.neighboring_cells(row, column))))


    # (int, int) -> void
    # given the coordinates of the cell clicked first, create a board that must have the given cell with a non-mine value, then call click_cell to start the game
    # fill in the mines randomly, then fill in the number depending on the mines
    def generate_board(self, row, column):
        rows, columns = BOARD_SIZE[self.difficulty]
        
        mine_positions = []

        # Generate a number of mines with random positions based on the chosen difficulity
        while len(mine_positions) < NUMBER_OF_MINES[self.difficulty]:
            # Generate a random position for the mine 
            mine_row_index = random.randint(0, rows-1)
            mine_column_index = random.randint(0, columns-1)
            
            # Make sure that the mine position wasn't generated before
            # Also, make sure that the mine position doesn't match the user's first move
            # Assign the value "M" to the cell with this position
            if(mine_row_index, mine_column_index) not in mine_positions and (mine_row_index, mine_column_index) != (row, column):
                self.board[mine_row_index][mine_column_index].val = "M"
                mine_positions.append((mine_row_index, mine_column_index))
        
        # Assign the values of each cell on the board
        # If its not a Mine -> Assign it the number of neighboring mines 
        for row_index in range(len(self.board)):
            for column_index in range(len(self.board[row_index])):
                if (row_index, column_index) not in mine_positions:
                    self.board[row_index][column_index].val = self.count_neighboring_mines(row_index, column_index) 

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
                print(f' {self.board[row][column].val} ', end='')
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


