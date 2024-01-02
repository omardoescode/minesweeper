import json

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

def save_game(username,difficulty,winning,score,time_elapsed):
     with open("save_games.txt","a") as file:
          game_data = {'username':username,'difficulty':difficulty,'game state':winning,'score':score,'time elapsed':time_elapsed}
          file.write(f"{game_data}\n")

def load_games():
     games = []
     with open("save_games.txt","r") as file:
          for line in file:
               games.append(json.loads(line.rstrip().replace("'", '"')))
     return games


