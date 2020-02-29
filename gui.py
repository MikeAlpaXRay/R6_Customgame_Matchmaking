import tkinter as tk
import functions as fnc

#ToDo: Layout
#ToDo:_changePlayer function
#ToDo: Rewrite?

def gui_handler(player_name_list):
    GUI_MAIN = tk.Tk()
    GUI_MAIN.title("Rainbow 6 Siege: Custom Matchmaking")
    GUI_MAIN.minsize(width=400, height=300)
    player1 = tk.StringVar()
    player2 = tk.StringVar()
    player3 = tk.StringVar()
    player4 = tk.StringVar()
    player5 = tk.StringVar()
    player6 = tk.StringVar()
    player7 = tk.StringVar()
    player8 = tk.StringVar()
    player9 = tk.StringVar()
    player10 = tk.StringVar()

    player1.set("Player 1")
    player2.set("Player 2")
    player3.set("Player 3")
    player4.set("Player 4")
    player5.set("Player 5")
    player6.set("Player 6")
    player7.set("Player 7")
    player8.set("Player 8")
    player9.set("Player 9")
    player10.set("Player 10")

    player1.set("Player 1")
    player2.set("Player 2")
    player3.set("Player 3")
    player4.set("Player 4")
    player5.set("Player 5")
    player6.set("Player 6")
    player7.set("Player 7")
    player8.set("Player 8")
    player9.set("Player 9")
    player10.set("Player 10")

    entry = fnc.AutocompleteEntry(player_name_list, GUI_MAIN)
    text_output = tk.Text(GUI_MAIN, height=14, width=25)
    matchmake = tk.Button(GUI_MAIN, text="Calculate Teams", width=15, height=1,
                          command=lambda: fnc.check_players(text_output))

    butplayer1 = tk.Button(GUI_MAIN, textvariable=player1, width=15, height=1,
                           command=lambda: fnc.changePlayer(entry, player1, 1))
    butplayer2 = tk.Button(GUI_MAIN, textvariable=player2, width=15, height=1,
                           command=lambda: fnc.changePlayer(entry, player2, 2))
    butplayer3 = tk.Button(GUI_MAIN, textvariable=player3, width=15, height=1,
                           command=lambda: fnc.changePlayer(entry, player3, 3))
    butplayer4 = tk.Button(GUI_MAIN, textvariable=player4, width=15, height=1,
                           command=lambda: fnc.changePlayer(entry, player4, 4))
    butplayer5 = tk.Button(GUI_MAIN, textvariable=player5, width=15, height=1,
                           command=lambda: fnc.changePlayer(entry, player5, 5))
    butplayer6 = tk.Button(GUI_MAIN, textvariable=player6, width=15, height=1,
                           command=lambda: fnc.changePlayer(entry, player6, 6))
    butplayer7 = tk.Button(GUI_MAIN, textvariable=player7, width=15, height=1,
                           command=lambda: fnc.changePlayer(entry, player7, 7))
    butplayer8 = tk.Button(GUI_MAIN, textvariable=player8, width=15, height=1,
                           command=lambda: fnc.changePlayer(entry, player8, 8))
    butplayer9 = tk.Button(GUI_MAIN, textvariable=player9, width=15, height=1,
                           command=lambda: fnc.changePlayer(entry, player9, 9))
    butplayer10 = tk.Button(GUI_MAIN, textvariable=player10, width=15, height=1,
                            command=lambda: fnc.changePlayer(entry, player10, 10))

    entry.place(x=5, y=5)
    matchmake.place(x=5, y=32)

    text_output.place(x=5, y=59)

    butplayer1.place(x=250, y=5)
    butplayer2.place(x=250, y=32)
    butplayer3.place(x=250, y=59)
    butplayer4.place(x=250, y=86)
    butplayer5.place(x=250, y=113)
    butplayer6.place(x=250, y=140)
    butplayer7.place(x=250, y=167)
    butplayer8.place(x=250, y=194)
    butplayer9.place(x=250, y=221)
    butplayer10.place(x=250, y=248)

    GUI_MAIN.mainloop()
