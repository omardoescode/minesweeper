from helpers import validate_input
from classes import Game
from constants import WELCOME_MESSAGE, DIFFICULTIES

def main():
    print(WELCOME_MESSAGE)

    print("Choose the difficulty\n1. Easy\n2. Medium\n3. Hard")
    difficulty = validate_input(int , "")
    while difficulty not in [1,2,3]:
        difficulty = validate_input(int, "Enter a difficulty level from 1 to 3")
    
    game = Game(DIFFICULTIES[difficulty])
    game.start_game()

if __name__ == '__main__':
    main()
