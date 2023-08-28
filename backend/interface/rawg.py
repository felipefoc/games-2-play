import requests
import os
from dotenv import load_dotenv

load_dotenv()
class Rawg(object):
    list_url = "https://api.rawg.io/api/games?"
    get_url = "https://api.rawg.io/api/games"

    def get_games(self, game_name):
        key = os.getenv('KEY')
        r = requests.get(f"{self.list_url}&search_exact=true&search={game_name}", params={"key": key})
        result = r.json()["results"]
        games = []
        for game in result:
            if not len(game["short_screenshots"]):
                continue
            
            games.append(
                {
                    "id": game["id"],
                    "title": game["name"],
                    "photo": game["short_screenshots"][0]["image"],
                    "metacritic": game["metacritic"],   
                }
            )
        return games
    
    def get_game(self, game_id):
        key = os.getenv('KEY')
        r = requests.get(f"{self.get_url}/{game_id}", params={"key": key})
        game = r.json()
        return (
                {
                    "id": game["id"],
                    "title": game["name"],
                    "description": game["description"],
                    "released": game["released"],
                    "photo": game["background_image"],
                    "metacritic": game["metacritic"],   
                }
            )
                

