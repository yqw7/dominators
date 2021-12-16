import random

from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

games = []
games_list = [
    "https://upload.wikimedia.org/wikipedia/en/5/51/Minecraft_cover.png",
    "https://www.stronggamers.com/wp-content/uploads/2019/03/fortnite.png",
    "https://upload.wikimedia.org/wikipedia/en/a/a5/Grand_Theft_Auto_V.png",
    "https://images-na.ssl-images-amazon.com/images/I/61Wvdn29vZL.png",
    "https://wallpapercave.com/wp/wp4251249.jpg",
    "https://cdn1.dotesports.com/wp-content/uploads/2019/09/12195522/league-of-legends.jpg",
    "https://upload.wikimedia.org/wikipedia/en/5/51/Overwatch_cover_art.jpg",
    "https://cdn1.epicgames.com/epic/offer/RDR2PC1227_Epic%20Games_860x1148-860x1148-b4c2210ee0c3c3b843a8de399bfe7f5c.jpg",
    "https://upload.wikimedia.org/wikipedia/en/thumb/e/e9/CallofDutyModernWarfare%282019%29.jpg/220px-CallofDutyModernWarfare%282019%29.jpg",
    "https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/Wii_Sports_Europe.jpg/220px-Wii_Sports_Europe.jpg",
    "https://upload.wikimedia.org/wikipedia/en/thumb/a/a7/God_of_War_4_cover.jpg/220px-God_of_War_4_cover.jpg",
    "https://activeplayer.io/wp-content/uploads/2020/11/Rocket-League-live-player-count.jpg",
    "https://wallpapercave.com/wp/wp7007822.jpg",
    "https://wallpapercave.com/wp/wp4400693.jpg",
    "https://wallpapercave.com/dwp2x/wp7048888.png"

]

def _find_next_id():
    return max(games["id"] for game in games) + 1


def _init_games():
    id = 1
    for game in games_list:
        games.append({"id": id, "game": game})
        id += 1

@api_bp.route('/game')
def get_game():
    if len(games) == 0:
        _init_games()
    return jsonify(random.choice(games))

if __name__ == "__main__":
    print(random.choice(games_list))