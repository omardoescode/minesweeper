import json
import os
from typing import List, Optional, Dict, Any
from classes import Cell
'''
Cell: [Previously defined in classes.py]

Board: (listof Cell)

GameSavedObject: 
    rows: int
    columns: int
    mines: int
    initial_time
    baord: Board
'''
# string, int, int, int, Board -> ()
# create a new file in folder games called <username>.json
# This file has a GameSavedObject
def store_game(username: str, rows: int, columns: int, mines: int, board: List[Cell], initial_time):
    game_data = {
        "rows": rows,
        "columns": columns,
        "mines": mines,
        "initial_time": initial_time,
        "board": [[cell.__dict__() for cell in row] for row in board]
    }

    # Create the games folder if it doesn't exist
    if not os.path.exists('games'):
        os.makedirs('games')

    path = fr'games/{username}.json'
    with open(path, 'w') as file:
        json.dump(game_data, file, indent=2)

# string -> (listof GameSavedObject)
# Retrieves the GameSavedObject of the given username
# the file should be in <username>.json
# Return an empty object if there's none
def retrieve_game(username: str) -> Optional[Dict]:
    # If the file doesn't exist, return an empty object
    if not check_game(username): return {}

    # If it's not, return the object
    with open(fr'games/{username}.json', 'r') as file:
        data = json.load(file)
        board = [[Cell(**cell) for cell in row] for row in data["board"]]
        return {**data, "board": board}
        
# string -> boolean
# delete the json file named <username>.json in games folder
# Return true if the file has been deleted, or false if the file doesn't exist (OPTIONAL)
def delete_game(username: str) -> bool:
    if check_game(username):
        file_path = fr'games/{username}.json'
        os.remove(file_path)
        return True
    return False
        
# string -> boolean
# Check if the player has a previous game uncontinued
# Check if the player has a file named after him in the games folder
# Return true if the player has a file named <username>, otherwise false

def check_game(username: str) -> bool:
    file_path = f'games/{username}.json'
    return os.path.exists(file_path)
