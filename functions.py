import requests
import datetime
import json

DEFAULT_MMR = 2000


class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_id = self.check_id()
        if not self.player_id:
            raise ValueError
        self.last_checked = False
        self.mmr = self.update_mmr()

    def check_id(self):
        id_url = "https://r6tab.com/api/search.php?platform=uplay&search=" + self.player_name
        id_request = requests.get(id_url)
        id_request = id_request.json()
        if id_request['totalresults'] != 0:
            id_request = id_request['results']
            player_id = id_request[0]['p_id']
        else:
            player_id = False
        return player_id

    def update_name(self, new_player_name):
        self.player_name = new_player_name

    def update_mmr(self):
        today = datetime.date.today()
        if self.last_checked:
            last_checked = self.last_checked.split('-')
            last_checked_year = int(last_checked[0])
            last_checked_month = int(last_checked[1])
            last_checked_day = int(last_checked[2])
            last_checked = datetime.date(last_checked_year,
                                         last_checked_month,
                                         last_checked_day)
            diff = today - last_checked
        if not self.last_checked or diff.days >= 5:
            player_stats_url = "https://r6tab.com/api/player.php?p_id=" + self.player_id
            player_stats = requests.get(player_stats_url).json()
            season_nr = 6
            player_mmr = 0
            count = 0
            season = "season" + str(season_nr)
            while season in player_stats.keys():
                if player_stats[season] != 0:
                    player_mmr += player_stats[season]
                    count += 1
                season_nr += 1
                season = "season" + str(season_nr)
            if player_stats["p_EU_currentmmr"] != 0:
                player_mmr += player_stats["p_EU_currentmmr"]
                count += 1

            self.last_checked = str(today)
            if player_mmr == 0:
                return DEFAULT_MMR
            else:
                return int(player_mmr / count)


def load_json():
    players = []
    with open("player_data\\player_data.json", 'r') as json_file:
        json_data = json.load(json_file)
        for entry in json_data:
            players.append(entry)
    return players


def save_json(player_list):
    str_json = json.dumps(player_list, default=lambda o: o.__dict__, indent=4)
    json_file = open("player_data\\player_data.json", "w+")
    json_file.write(str_json)
    json_file.close()


if __name__ == "__main__":
# try:
#     player_list = load_json()
#     player_list.append(Player("TheBiche."))
#     save_json(player_list)
#
# except ValueError:
#     print()
