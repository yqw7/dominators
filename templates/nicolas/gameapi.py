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
    "https://st4.depositphotos.com/16775192/24052/v/600/depositphotos_240520392-stock-illustration-poster-and-phrase-from-the.jpg",
    "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Legend_of_Zelda_Breath_of_the_Wild.jpg",
    "https://cdn1.dotesports.com/wp-content/uploads/2019/09/12195522/league-of-legends.jpg",
    "https://upload.wikimedia.org/wikipedia/en/1/15/The_Elder_Scrolls_V_Skyrim_cover.png",
    "https://upload.wikimedia.org/wikipedia/en/9/91/WoW_Box_Art1.jpg",
    "https://upload.wikimedia.org/wikipedia/en/5/51/Overwatch_cover_art.jpg",
    "https://www.nintendo.com//content/dam/noa/en_US/games/switch/m/mario-kart-8-deluxe-switch/mario-kart-8-deluxe-switch-hero.jpg",
    "https://upload.wikimedia.org/wikipedia/en/1/1f/Animal_Crossing_New_Horizons.jpg",
    "https://cdn1.epicgames.com/epic/offer/RDR2PC1227_Epic%20Games_860x1148-860x1148-b4c2210ee0c3c3b843a8de399bfe7f5c.jpg",
    "https://upload.wikimedia.org/wikipedia/en/thumb/e/e9/CallofDutyModernWarfare%282019%29.jpg/220px-CallofDutyModernWarfare%282019%29.jpg",
    "https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/Wii_Sports_Europe.jpg/220px-Wii_Sports_Europe.jpg",
    "https://upload.wikimedia.org/wikipedia/en/thumb/a/a7/God_of_War_4_cover.jpg/220px-God_of_War_4_cover.jpg",
    "https://activeplayer.io/wp-content/uploads/2020/11/Rocket-League-live-player-count.jpg",
    "data:image/jpeg;base64,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",
    "https://photos5.appleinsider.com/gallery/40883-79111-B3840B94-33C9-4304-96D9-2BEBF83ECBAD-xl.jpg"
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