from helpers import validate_input
from classes import Game
from constants import say_welcome, DIFFICULTIES, NUMBER_OF_MINES, BOARD_SIZE
def main():
    name = validate_input(str, "Enter your name: ", lambda val: val != "")
    say_welcome(name)

    print("Choose the difficulty\n1. Easy\n2. Medium\n3. Hard\n4. Custom")
    difficulty = validate_input(int , "Input: ", lambda val: val in [1,2,3,4])
    
    if difficulty == 4:
        rows = validate_input(int, "Enter the number of rows: ", lambda val: val > 2)
        columns = validate_input(int, "Enter the number of columns: ", lambda val: val > 2)
        mines = validate_input(int, "Enter the number of the mines: ", lambda val: val > 0 and val < rows * columns / 2) 
    else:
        rows, columns = BOARD_SIZE[DIFFICULTIES[difficulty]]
        mines = NUMBER_OF_MINES[DIFFICULTIES[difficulty]]
        
    
    game = Game(rows, columns, mines)
    game.start_game()

if __name__ == '__main__':
    main()
