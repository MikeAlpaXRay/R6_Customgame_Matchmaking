import json
import requests

class Player:
    def __init__(self, player_name, player_id, MMR, LastChecked):
        self.player_name = PlayerName
        self.player_id = PlayerID
        self.mmr = MMR
        self.last_checked = LastChecked

def get_json():
    all_players = []
    with open("player_data\\knownPlayers.json", 'r') as json_file:
        all_players = json.load(json_file)
    return all_players


def get_player_id_r6tab(player_name):
    id_url = "https://r6tab.com/api/search.php?platform=uplay&search=" + player_name
    id_request = requests.get(id_url)
    id_request = id_request.json()
    if id_request['totalresults'] != 0:
        id_request = id_request['results']
        player_id = id_request[0]['p_id']
        return player_id
    else:
        player_id = False
        return



if __name__ == "__main__":
    playerid = get_player_id_r6tab("MikeAlpaXRayLFT")
    print(playerid)
