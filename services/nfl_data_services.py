import requests

def get_nfl_live_scores():
    url = "https://www.thesportsdb.com/api/v2/json/60130162/livescore.php?l=4391"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()['events']
    except requests.RequestException as e:
        print(f"Error fetching NFL data: {e}")
        return []
