from nba_api.stats.endpoints import boxscoretraditionalv2
import json
import os

def get_game_details(game_id):
    game_data = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=game_id)
    return game_data.get_normalized_dict()

def get_all_games_details(game_ids):
    all_game_details = {}
    for game_id in game_ids:
        all_game_details[game_id] = get_game_details(game_id)
    return all_game_details

def save_game_details_to_json(game_details, folder, filename):
    os.makedirs(folder, exist_ok=True)
    json_file_path = os.path.join(folder, filename)
    with open(json_file_path, 'w') as json_file:
        json.dump(game_details, json_file)