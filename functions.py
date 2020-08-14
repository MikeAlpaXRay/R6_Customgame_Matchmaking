import requests
import datetime
import json
import re
import clipboard
import tkinter as tk
from operator import itemgetter
import gui_support
import calendar

DEFAULT_MMR = 2000
chosen_players = [None] * 10
added_no_player = []


class Player:
    def __init__(self, player_name, player_id, last_checked=True, mmr=True):
        self.player_name = player_name
        if type(last_checked) and type(mmr) == bool:
            if player_id:
                self.player_id = player_id
            else:
                raise ValueError
            self.last_checked = False
            self.mmr = self.update_player()
            print(str(self.player_name) + "    " + str(self.mmr))
            clipboard.copy(str(self.player_name) + "    " + str(self.mmr))
        else:
            self.player_id = player_id
            self.last_checked = last_checked
            self.mmr = mmr

    def check_id(self):
        dt = datetime.datetime.utcnow()
        unix = calendar.timegm(dt.utctimetuple())
        id_url = " https://r6.apitab.com/search/uplay/" + self.player_name + "?u=" + str(unix)
        id_request = requests.get(id_url)
        id_request = id_request.json()
        if id_request['foundmatch'] == True:
            player_id = id_request['players'].keys()
        else:
            player_id = False
        return player_id

    def update_name(self, new_player_name):
        self.player_name = new_player_name

    def update_player(self):
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
            dt = datetime.datetime.utcnow()
            unix = calendar.timegm(dt.utctimetuple())
            player_stats_url = "https://r6.apitab.com/player/" + self.player_id + "?u=" + str(unix)
            player_stats = requests.get(player_stats_url).json()
            self.player_name = player_stats["player"]["p_name"]
            player_stats_seasons = player_stats["seasons"]
            season_nr = 6
            player_mmr = 0
            count = 0
            season = str(season_nr)
            while season in player_stats_seasons.keys():
                if player_stats_seasons[season]["maxmmr"] != "":
                    player_mmr += player_stats_seasons[season]["maxmmr"]
                    count += 1
                season_nr += 1
                season = str(season_nr)
            if player_stats["ranked"]['actualmmr'] != "":
                player_mmr += player_stats["ranked"]['actualmmr']
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
        player_list.append(Player(player_name=player['player_name'],
                                  player_id=player['player_id'],
                                  last_checked=player['last_checked'],
                                  mmr=player['mmr']))
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


# ToDo bei change in playernameliste none back to name
def add_player(gui, no):
    player_added = False
    new_player_name = gui.Player_Entry.get()
    if new_player_name in player_name_list:
        index = player_name_list.index(new_player_name)
        player_object = player_list[index]
        player_object.update_player()
        player_name_list[index] = ""
        player_added = True
        chosen_players[no] = player_object
        # print("update Spieler")
    else:
        new_player_id = check_id(new_player_name)
        if new_player_id:
            if new_player_id in player_id_list:
                index = player_id_list.index(new_player_id)
                player_object = player_list[index]
                player_object.update_name(new_player_name)
                player_name_list[index] = ""
                player_object.update_player()
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
    gui_support.match_make.set("Matchmake")
    player_added = add_player(gui, no - 1)
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
    dt = datetime.datetime.utcnow()
    unix = calendar.timegm(dt.utctimetuple())
    id_url = " https://r6.apitab.com/search/uplay/" + player_name + "?u=" + str(unix)
    id_request = requests.get(id_url)
    id_request = id_request.json()
    if id_request['foundmatch']:
        player_id = list(id_request['players'].keys())[0]
    else:
        player_id = False
    return player_id


def matchmake():
    if len(added_no_player) == 10:
        chosen_players.sort(key=lambda player: player.mmr, reverse=True)
        mmrDeltaList = []
        Team1List = []
        Team2List = []

        team1 = []
        team2 = []

        for player in chosen_players:
            print(str(player.player_name) + "\t" + str(player.mmr))
            if calcteam_mmr(team1) <= calcteam_mmr(team2):
                team1.append(player)
            else:
                team2.append(player)
        print("MMR Delta: " + str(abs(calcmmr_delta(team1, team2))))
        showteam(team1)
        showteam(team2)

        mmrDeltaList.append(calcmmr_delta(team1, team2))
        Team1List.append(team1)
        Team2List.append(team2)

        i = 0
        while True:
            team1, team2 = correct(team1, team2)
            if calcmmr_delta(team1, team2) in mmrDeltaList:
                break
            print("#############################################################\n" +
                  "\t\t\tIteration " + str(i) + "\n" +
                  "#############################################################\n")
            mmrDeltaList.append(calcmmr_delta(team1, team2))
            Team1List.append(team1)
            Team2List.append(team2)
            print("\n\n")
            print("MMR Delta: " + str(abs(calcmmr_delta(team1, team2))))
            showteam(team1)
            showteam(team2)
            i += 1

        # use best teamcomposition
        solutionIndex = mmrDeltaList.index(min(mmrDeltaList, key=abs))
        print("\n\n\n")
        print("#############################################################\n" +
              "\t\t\tTeams\n" +
              "#############################################################\n")
        print("MMR Delta: " + str(abs(mmrDeltaList[solutionIndex])))
        showteam(Team1List[solutionIndex])
        showteam(Team2List[solutionIndex])

        text = to_clipbord(team1, team2)
    else:
        gui_support.match_make.set("Add 10 Player")


def correct(team1, team2):
    'Corrects both Teams according to the last MMR Delta'
    newTeam1 = team1
    newTeam2 = team2
    pairs = []
    error = calcteam_mmr(team1) - calcteam_mmr(team2)
    i = 0
    for playeri in newTeam1:
        j = 0
        for playerj in newTeam2:
            playerdiff = (playeri.mmr - playerj.mmr) * 2
            pairs.append([playerdiff, newTeam1[i], newTeam2[j]])
            j += 1
        i += 1

    pairs = sorted(pairs, key=itemgetter(0), reverse=False)
    changingPair = min(pairs, key=lambda x: abs(x[0] - error))
    newTeam1.remove(changingPair[1])
    newTeam1.append(changingPair[2])
    newTeam2.remove(changingPair[2])
    newTeam2.append(changingPair[1])
    if abs(calcmmr_delta(team1, team2)) > abs(calcmmr_delta(newTeam1, newTeam2)):
        team1 = newTeam1
        team2 = newTeam2
    return team1, team2


def calcteam_mmr(team):
    'Get Teamcombinedmmr'
    teamMMR = 0
    for player in team:
        teamMMR += player.mmr
    return teamMMR


def calcmmr_delta(team1, team2):
    'MMR Delta between Teams'
    delta = calcteam_mmr(team1) - calcteam_mmr(team2)
    return delta


def showteam(team):
    'prints the Teamcomposition'
    print("\nTeam:\n\tMMR:" + str(calcteam_mmr(team)))
    for player in team:
        print(player.player_name)


def to_clipbord(team1, team2):
    'copy result to clipbord'
    text = ""
    text += "Team1:\n"
    for player in team1:
        text += "\t" + player.player_name + "\n"
    text += "\nTeam2:\n"
    for player in team2:
        text += "\t" + player.player_name + "\n"
    clipboard.copy("\n" + text)
    gui_support.match_make_text.set(text)
    return text


if __name__ == "__main__":
    print()
