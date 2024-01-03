import json
from json.decoder import JSONDecodeError

# username = ""
# wins = 0
# loses = 0 
# games_played = wins+loses
# highscore = 0
# game_won = None


## Class for saving player info (will use later)
# class Player:
#      def __init__(self,username, wins,loses,highscore):
#           self.username = username
#           self.wins = wins
#           self.loses = loses
#           self.highscore = highscore
#           self.games_played = self.loses + self.wins
# playerinfo_JSON = '{"username":username, "wins":wins, "loses":loses, "games_played":games_played, "score":score}'

# If a save_games.json file exists, load the data in it and return it. Otherwise, return an empty list
def load_games():
     games = []
     try:
          with open(rf"save_games.json","r") as file:
               games = json.load(file)
     except JSONDecodeError:
          games = []
     except FileNotFoundError:
          games = []
     
     return games

# If a save_games.json file exist, load the data in it and concatenate it to the new data. Then write all the data to save_games.json
def save_game(username,difficulty,winning,score,time_elapsed):
     games_data = load_games()
     with open(rf"save_games.json","w") as file:
          game_data = {"username":username,"difficulty":difficulty,"game state":winning,"score":score,"time elapsed":time_elapsed}
          json.dump([*games_data, game_data], file)

