'''
Cell:
    val: [0:8] or F or M (1 through 8 for number or f for flagged or m for mines)
    is_flagged: boolean
    is_covered: boolean

Board: (listof Cell)

GameSavedObject: 
    rows: int
    columns: int
    mines: int
    baord: Board
'''

# string, int, int, int, Board -> ()
# create a new file in folder games called <username>.json
# This file has a GameSavedObject
def store_game(username, rows, columns, mines, board):
    pass

# string -> (listof GameSavedObject)
# Retrieves the GameSavedObject of the given username
# the file should be in <username>.json
# Return an empty object if there's none
def retrieve_game(username):
    pass

# string -> boolean
# delete the json file named <username>.json in games folder
# Return true if the file has been deleted, or false if the file doesn't exist (OPTIONAL)
def delete_game(username):
    pass

# string -> boolean
# Check if the player has a previous game uncontinued
# Check if the player has a file named after him in the games folder
# Return true if the player has a file named <username>, otherwise false

def check_game(username):
    pass