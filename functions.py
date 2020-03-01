import requests
import datetime
import json
import re
import tkinter as tk
import gui
import gui_support

# ToDo: matchmaking
DEFAULT_MMR = 2000
chosen_players = [None] * 10
added_no_player = []


class Player:
    def __init__(self, player_name, player_id, last_checked=True, mmr=True):
        self.player_name = player_name
        if last_checked and mmr:
            if player_id:
                self.player_id = player_id
            else:
                raise ValueError
            self.last_checked = False
            self.mmr = self.update_mmr()
        else:
            self.player_id = player_id
            self.last_checked = last_checked
            self.mmr = mmr

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
        diff = today - today
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


class AutocompleteEntry(tk.Entry):
    def __init__(self, player_name_list, *args, **kwargs):

        tk.Entry.__init__(self, *args, **kwargs)
        self.player_name_list = player_name_list
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = tk.StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.new_name)
        self.bind("<Return>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)

        self.lb_up = False

    def changed(self, name, index, mode):

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:
                if not self.lb_up:
                    self.lb = tk.Listbox()
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Return>", self.selection)
                    self.lb.bind("<Right>", self.new_name)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
                    self.lb_up = True

                self.lb.delete(0, tk.END)
                for w in words:
                    self.lb.insert(tk.END, w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False

    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(tk.ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(tk.END)

    def new_name(self, event):

        if self.lb_up:
            self.var.set(self.var.get())
            self.lb.destroy()
            self.lb_up = False
            self.icursor(tk.END)

    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':
                self.lb.selection_clear(first=index)
                index = str(int(index) - 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != tk.END:
                self.lb.selection_clear(first=index)
                index = str(int(index) + 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)

    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*')
        return [w for w in self.player_name_list if re.match(pattern, w)]


def load_json():
    players = []
    with open("player_data\\player_data.json", 'r') as json_file:
        json_data = json.load(json_file)
        for entry in json_data:
            players.append(entry)

    global player_list
    player_list = []
    for player in players:
        player_list.append(Player(player['player_name'],
                                  player['player_id'],
                                  player['last_checked'],
                                  player['mmr']))
    global player_name_list
    player_name_list = []
    global player_id_list
    player_id_list = []
    for player in player_list:
        player_name_list.append(player.player_name)
        player_id_list.append(player.player_id)
    return player_name_list


def save_json():
    str_json = json.dumps(player_list, default=lambda o: o.__dict__, indent=4)
    json_file = open("player_data\\player_data.json", "w+")
    json_file.write(str_json)
    json_file.close()


def addPlayer(gui, no):
    player_added = False
    new_player_name = gui.Player_Entry.get()
    if new_player_name in player_name_list:
        player_object = player_list[player_name_list.index(new_player_name)]
        player_object.update_mmr()
        player_name_list.remove(new_player_name)
        player_added = True
        chosen_players[no] = player_object
        # print("update Spieler")
    else:
        new_player_id = check_id(new_player_name)
        if new_player_id:
            if new_player_id in player_id_list:
                player_object = player_list[player_id_list.index(new_player_id)]
                player_object.update_name(new_player_name)
                player_name_list.remove(player_object.player_name)
                player_object.update_mmr()
                # print("neuer Spielername")
            else:
                player_object = Player(new_player_name, new_player_id)
                player_list.append(player_object)
                player_name_list.append(new_player_name)
            player_added = True
            chosen_players[no] = player_object

        # else:
        #     print("Spieler unbekannt")
    return player_added


def handle_add_player(gui, no):
    player_added = addPlayer(gui, no - 1)
    if player_added:
        if no == 1:
            if no in added_no_player:
                player_name_list.append(gui_support.player1.get())
                gui_support.player1.set(gui.Player_Entry.get())
            else:
                added_no_player.append(no)
                gui_support.player1.set(gui.Player_Entry.get())
        elif no == 2:
            if no in added_no_player:
                player_name_list.append(gui_support.player2.get())
                gui_support.player2.set(gui.Player_Entry.get())
            else:
                added_no_player.append(no)
                gui_support.player2.set(gui.Player_Entry.get())
        elif no == 3:
            if no in added_no_player:
                player_name_list.append(gui_support.player3.get())
                gui_support.player3.set(gui.Player_Entry.get())
            else:
                added_no_player.append(no)
                gui_support.player3.set(gui.Player_Entry.get())
        elif no == 4:
            if no in added_no_player:
                player_name_list.append(gui_support.player4.get())
                gui_support.player4.set(gui.Player_Entry.get())
            else:
                added_no_player.append(no)
                gui_support.player4.set(gui.Player_Entry.get())
        elif no == 5:
            if no in added_no_player:
                player_name_list.append(gui_support.player5.get())
                gui_support.player5.set(gui.Player_Entry.get())
            else:
                added_no_player.append(no)
                gui_support.player5.set(gui.Player_Entry.get())
        elif no == 6:
            if no in added_no_player:
                player_name_list.append(gui_support.player5.get())
                gui_support.player6.set(gui.Player_Entry.get())
            else:
                added_no_player.append(no)
                gui_support.player6.set(gui.Player_Entry.get())
        elif no == 7:
            if no in added_no_player:
                player_name_list.append(gui_support.player7.get())
                gui_support.player7.set(gui.Player_Entry.get())
            else:
                added_no_player.append(no)
                gui_support.player7.set(gui.Player_Entry.get())
        elif no == 8:
            if no in added_no_player:
                player_name_list.append(gui_support.player8.get())
                gui_support.player8.set(gui.Player_Entry.get())
            else:
                added_no_player.append(no)
                gui_support.player8.set(gui.Player_Entry.get())
        elif no == 9:
            if no in added_no_player:
                player_name_list.append(gui_support.player9.get())
                gui_support.player9.set(gui.Player_Entry.get())
            else:
                added_no_player.append(no)
                gui_support.player9.set(gui.Player_Entry.get())
        elif no == 10:
            if no in added_no_player:
                player_name_list.append(gui_support.player10.get())
                gui_support.player10.set(gui.Player_Entry.get())
            else:
                added_no_player.append(no)
                gui_support.player10.set(gui.Player_Entry.get())


def handle_remove_player(gui, no):
    if no == 1:
        if no in added_no_player:
            added_no_player.remove(no)
            player_name_list.append(gui_support.player1.get())
            gui_support.player1.set("Player " + str(no))
    elif no == 2:
        if no in added_no_player:
            added_no_player.remove(no)
            player_name_list.append(gui_support.player2.get())
            gui_support.player2.set("Player " + str(no))
    elif no == 3:
        if no in added_no_player:
            added_no_player.remove(no)
            player_name_list.append(gui_support.player3.get())
            gui_support.player3.set("Player " + str(no))
    elif no == 4:
        if no in added_no_player:
            added_no_player.remove(no)
            player_name_list.append(gui_support.player4.get())
            gui_support.player4.set("Player " + str(no))
    elif no == 5:
        if no in added_no_player:
            added_no_player.remove(no)
            player_name_list.append(gui_support.player5.get())
            gui_support.player5.set("Player " + str(no))
    elif no == 6:
        if no in added_no_player:
            added_no_player.remove(no)
            player_name_list.append(gui_support.player6.get())
            gui_support.player6.set("Player " + str(no))
    elif no == 7:
        if no in added_no_player:
            added_no_player.remove(no)
            player_name_list.append(gui_support.player7.get())
            gui_support.player7.set("Player " + str(no))
    elif no == 8:
        if no in added_no_player:
            added_no_player.remove(no)
            player_name_list.append(gui_support.player8.get())
            gui_support.player8.set("Player " + str(no))
    elif no == 9:
        if no in added_no_player:
            added_no_player.remove(no)
            player_name_list.append(gui_support.player9.get())
            gui_support.player9.set("Player " + str(no))
    elif no == 10:
        if no in added_no_player:
            added_no_player.remove(no)
            player_name_list.append(gui_support.player10.get())
            gui_support.player10.set("Player " + str(no))


def check_id(player_name):
    id_url = "https://r6tab.com/api/search.php?platform=uplay&search=" + player_name
    id_request = requests.get(id_url)
    id_request = id_request.json()
    if id_request['totalresults'] != 0:
        id_request = id_request['results']
        player_id = id_request[0]['p_id']
    else:
        player_id = False
    return player_id


if __name__ == "__main__":
    print()
