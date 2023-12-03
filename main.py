from flask import Flask, render_template
from datetime import datetime
from services.game_id_service import get_todays_game_ids, save_game_ids_to_json, load_game_ids_from_json
from services.game_data_service import get_all_games_details, save_game_details_to_json

app = Flask(__name__)

@app.route('/')
def index():
    folder_name_game_ids = 'gameID'
    folder_name_game_data = 'gameData'
    today_date = datetime.now().strftime('%Y-%m-%d')
    json_filename_game_ids = f'game_ids_{today_date}.json'
    json_filename_game_data = f'game_details_{today_date}.json'

    saved_game_ids = load_game_ids_from_json(folder_name_game_ids, json_filename_game_ids)

    if not saved_game_ids:
        todays_game_ids = get_todays_game_ids()
        save_game_ids_to_json(todays_game_ids, folder_name_game_ids, json_filename_game_ids)
        saved_game_ids = todays_game_ids

    game_details = get_all_games_details(saved_game_ids)
    
    # Save game details to JSON in the gameData folder
    save_game_details_to_json(game_details, folder_name_game_data, json_filename_game_data)

    return render_template('index.html', game_details=game_details)

if __name__ == '__main__':
    app.run(debug=True)
