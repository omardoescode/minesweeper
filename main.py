from helpers import validate_input
from classes import Game
from constants import say_welcome, DIFFICULTIES, NUMBER_OF_MINES, BOARD_SIZE
from timer import Timer
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

def start_game():
    # Initialize the Timer
    timer = Timer()
    timer.start_timer()

    # ... (rest of your game setup and logic)
    print("Game started!")

    # Example loop to simulate gameplay (replace this with your actual game logic)
    try:
        while True:
            # Perform game actions here

            # For instance, check the elapsed time
            elapsed_time = timer.get_elapsed_time()
            print(f"Elapsed Time: {elapsed_time} seconds")

            # Check for game-over conditions based on elapsed time or other game events
            if elapsed_time >= 300:  # Check if 5 minutes (300 seconds) elapsed
                print("Game over due to time limit!")
                break  # End the game or perform game-over actions

            # Simulate gameplay delay
            # Replace this with your actual game mechanics that would occur over time
            # For demonstration purposes, this sleeps for 1 second in each loop iteration
            time.sleep(1)

    except KeyboardInterrupt:
        timer.stop_timer()
        print("Game stopped. Elapsed Time:", timer.get_elapsed_time(), "seconds")


if __name__ == '__main__':
    main()
    start_game()
