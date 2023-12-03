from datetime import datetime
from nba_api.stats.endpoints import scoreboard
import json
import os

def get_todays_game_ids():
    today = datetime.now().strftime('%Y-%m-%d')
    scoreboard_data = scoreboard.Scoreboard(game_date=today)
    game_ids = scoreboard_data.get_normalized_dict()['GameHeader']
    return [game['GAME_ID'] for game in game_ids]

def save_game_ids_to_json(game_ids, folder, filename):
    os.makedirs(folder, exist_ok=True)
    json_file_path = os.path.join(folder, filename)
    with open(json_file_path, 'w') as json_file:
        json.dump(game_ids, json_file)

def load_game_ids_from_json(folder, filename):
    json_file_path = os.path.join(folder, filename)
    try:
        with open(json_file_path, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []
