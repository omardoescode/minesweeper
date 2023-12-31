import json
import os
from typing import List, Optional, Dict, Any

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
class Cell:
    def __init__(self, val: str, is_flagged: bool, is_covered: bool):
        self.val = val
        self.is_flagged = is_flagged
        self.is_covered = is_covered

class GameSavedObject:
    def __init__(self, rows: int, columns: int, mines: int, board: List[Cell]):
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.board = board
        
# string, int, int, int, Board -> ()
# create a new file in folder games called <username>.json
# This file has a GameSavedObject
def store_game(username: str, rows: int, columns: int, mines: int, board: List[Cell]):
    game_data = {
        "rows": rows,
        "columns": columns,
        "mines": mines,
        "board": [vars(cell) for cell in board]

# string -> (listof GameSavedObject)
# Retrieves the GameSavedObject of the given username
# the file should be in <username>.json
# Return an empty object if there's none
def retrieve_game(username: str) -> Optional[GameSavedObject]:
    try:
        with open(f'games/{username}.json', 'r') as file:
            data = json.load(file)
            board = [Cell(**cell) for cell in data["board"]]
            return GameSavedObject(data["rows"], data["columns"], data["mines"], board)
    except FileNotFoundError:
        return None
        
# string -> boolean
# delete the json file named <username>.json in games folder
# Return true if the file has been deleted, or false if the file doesn't exist (OPTIONAL)
def delete_game(username: str) -> bool:
    try:
        file_path = f'games/{username}.json'
        os.remove(file_path)
        return True
    except FileNotFoundError:
        return False
        
# string -> boolean
# Check if the player has a previous game uncontinued
# Check if the player has a file named after him in the games folder
# Return true if the player has a file named <username>, otherwise false

def check_game(username: str) -> bool:
    file_path = f'games/{username}.json'
    return os.path.exists(file_path)
