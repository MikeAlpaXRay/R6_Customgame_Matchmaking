import clipboard
import tkinter as tk
from operator import itemgetter
import re
import functions as fnc
import gui


if __name__ == "__main__":
    json_player_list = fnc.load_json()
    player_list = []
    for player in json_player_list:
        player_list.append(fnc.Player(player['player_name'],
                                      player['player_id'],
                                      player['last_checked'],
                                      player['mmr']))
    player_name_list = []
    player_id_list = []
    for player in player_list:
        player_name_list.append(player.player_name)
        player_id_list.append(player.player_id)
    gui.vp_start_gui(player_name_list)