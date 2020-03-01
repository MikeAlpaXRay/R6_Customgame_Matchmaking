import tkinter as tk
import tkinter.ttk as ttk
from time import time, localtime, strftime
import functions as fnc
import gui_support

# ToDo:_changePlayer function

py3 = True


def vp_start_gui(player_name_list):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    gui_support.set_Tk_var()
    global top
    top = Toplevel(root, player_name_list)
    gui_support.init(root, top)
    root.mainloop()


w = None


def create_toplevel(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    gui_support.set_Tk_var()
    top = Toplevel(w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_toplevel():
    global w
    w.destroy()
    w = None


class Toplevel:
    def __init__(self, top=None, player_name_list=[]):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("640x480+1152+156")
        top.minsize(500, 360)
        top.maxsize(854, 480)
        top.resizable(0, 0)
        top.title("R6 Custom Matchmaking")
        top.configure(background="#d9d9d9")

        self.Player_Entry = fnc.AutocompleteEntry(player_name_list, top)
        self.Player_Entry.place(relx=0.047, rely=0.083, height=20, width=150)
        self.Player_Entry.configure(background="white")
        self.Player_Entry.configure(disabledforeground="#a3a3a3")
        self.Player_Entry.configure(font="TkFixedFont")
        self.Player_Entry.configure(foreground="#000000")
        self.Player_Entry.configure(insertbackground="black")
        tooltip_font = "TkDefaultFont"
        ToolTip(self.Player_Entry, tooltip_font, '''Enter Playername''', delay=0.5)

        self.Player_Canvas = tk.Canvas(top)
        self.Player_Canvas.place(relx=0.047, rely=0.146, relheight=0.667, relwidth=0.344)
        self.Player_Canvas.configure(background="#d9d9d9")
        self.Player_Canvas.configure(borderwidth="2")
        self.Player_Canvas.configure(cursor="arrow")
        self.Player_Canvas.configure(insertbackground="black")
        self.Player_Canvas.configure(relief="ridge")
        self.Player_Canvas.configure(selectbackground="#c4c4c4")
        self.Player_Canvas.configure(selectforeground="black")

        self.PlayerCanvas_Label = tk.Label(self.Player_Canvas)
        self.PlayerCanvas_Label.place(relx=0.091, rely=0.063, height=20, width=50)
        self.PlayerCanvas_Label.configure(background="#d9d9d9")
        self.PlayerCanvas_Label.configure(disabledforeground="#a3a3a3")
        self.PlayerCanvas_Label.configure(foreground="#000000")
        self.PlayerCanvas_Label.configure(text='''Players:''')

        self.removePlayer1_Button = tk.Button(self.Player_Canvas)
        self.removePlayer1_Button.place(relx=0.045, rely=0.156, height=20, width=20)
        self.removePlayer1_Button.configure(activebackground="#ececec")
        self.removePlayer1_Button.configure(activeforeground="#000000")
        self.removePlayer1_Button.configure(background="#d9d9d9")
        self.removePlayer1_Button.configure(cursor="arrow")
        self.removePlayer1_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer1_Button.configure(foreground="#000000")
        self.removePlayer1_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer1_Button.configure(highlightcolor="black")
        self.removePlayer1_Button.configure(pady="0")
        self.removePlayer1_Button.configure(text='''<''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.removePlayer1_Button, tooltip_font, '''Remove Player''', delay=0.5)
        self.removePlayer1_Button.configure(command=lambda: fnc.handle_remove_player(self, 1))

        self.addPlayer1_Button = tk.Button(self.Player_Canvas)
        self.addPlayer1_Button.place(relx=0.136, rely=0.156, height=20, width=20)
        self.addPlayer1_Button.configure(activebackground="#ececec")
        self.addPlayer1_Button.configure(activeforeground="#000000")
        self.addPlayer1_Button.configure(background="#d9d9d9")
        self.addPlayer1_Button.configure(cursor="arrow")
        self.addPlayer1_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer1_Button.configure(foreground="#000000")
        self.addPlayer1_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer1_Button.configure(highlightcolor="black")
        self.addPlayer1_Button.configure(pady="0")
        self.addPlayer1_Button.configure(text='''>''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.addPlayer1_Button, tooltip_font, '''Add/Change Player''', delay=0.5)
        self.addPlayer1_Button.configure(command=lambda: fnc.handle_add_player(self, 1))

        self.Player1_Label = tk.Label(self.Player_Canvas)
        self.Player1_Label.place(relx=0.273, rely=0.156, height=20, width=120)
        self.Player1_Label.configure(background="#d9d9d9")
        self.Player1_Label.configure(disabledforeground="#a3a3a3")
        self.Player1_Label.configure(foreground="#000000")
        self.Player1_Label.configure(text='''Player 1''')
        self.Player1_Label.configure(textvariable=gui_support.player1)

        self.removePlayer2_Button = tk.Button(self.Player_Canvas)
        self.removePlayer2_Button.place(relx=0.045, rely=0.234, height=20, width=20)
        self.removePlayer2_Button.configure(activebackground="#ececec")
        self.removePlayer2_Button.configure(activeforeground="#000000")
        self.removePlayer2_Button.configure(background="#d9d9d9")
        self.removePlayer2_Button.configure(cursor="arrow")
        self.removePlayer2_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer2_Button.configure(foreground="#000000")
        self.removePlayer2_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer2_Button.configure(highlightcolor="black")
        self.removePlayer2_Button.configure(pady="0")
        self.removePlayer2_Button.configure(text='''<''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.removePlayer2_Button, tooltip_font, '''Remove Player''', delay=0.5)
        self.removePlayer2_Button.configure(command=lambda: fnc.handle_remove_player(self, 2))

        self.addPlayer2_Button = tk.Button(self.Player_Canvas)
        self.addPlayer2_Button.place(relx=0.136, rely=0.234, height=20, width=20)
        self.addPlayer2_Button.configure(activebackground="#ececec")
        self.addPlayer2_Button.configure(activeforeground="#000000")
        self.addPlayer2_Button.configure(background="#d9d9d9")
        self.addPlayer2_Button.configure(cursor="arrow")
        self.addPlayer2_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer2_Button.configure(foreground="#000000")
        self.addPlayer2_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer2_Button.configure(highlightcolor="black")
        self.addPlayer2_Button.configure(pady="0")
        self.addPlayer2_Button.configure(text='''>''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.addPlayer2_Button, tooltip_font, '''Add/Change Player''', delay=0.5)
        self.addPlayer2_Button.configure(command=lambda: fnc.handle_add_player(self, 2))

        self.Player2_Label = tk.Label(self.Player_Canvas)
        self.Player2_Label.place(relx=0.273, rely=0.234, height=20, width=120)
        self.Player2_Label.configure(background="#d9d9d9")
        self.Player2_Label.configure(cursor="arrow")
        self.Player2_Label.configure(disabledforeground="#a3a3a3")
        self.Player2_Label.configure(foreground="#000000")
        self.Player2_Label.configure(text='''Player 2''')
        self.Player2_Label.configure(textvariable=gui_support.player2)

        self.removePlayer3_Button = tk.Button(self.Player_Canvas)
        self.removePlayer3_Button.place(relx=0.045, rely=0.313, height=20, width=20)
        self.removePlayer3_Button.configure(activebackground="#ececec")
        self.removePlayer3_Button.configure(activeforeground="#000000")
        self.removePlayer3_Button.configure(background="#d9d9d9")
        self.removePlayer3_Button.configure(cursor="arrow")
        self.removePlayer3_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer3_Button.configure(foreground="#000000")
        self.removePlayer3_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer3_Button.configure(highlightcolor="black")
        self.removePlayer3_Button.configure(pady="0")
        self.removePlayer3_Button.configure(text='''<''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.removePlayer3_Button, tooltip_font, '''Remove Player''', delay=0.5)
        self.removePlayer3_Button.configure(command=lambda: fnc.handle_remove_player(self, 3))

        self.addPlayer3_Button = tk.Button(self.Player_Canvas)
        self.addPlayer3_Button.place(relx=0.136, rely=0.313, height=20, width=20)
        self.addPlayer3_Button.configure(activebackground="#ececec")
        self.addPlayer3_Button.configure(activeforeground="#000000")
        self.addPlayer3_Button.configure(background="#d9d9d9")
        self.addPlayer3_Button.configure(cursor="arrow")
        self.addPlayer3_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer3_Button.configure(foreground="#000000")
        self.addPlayer3_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer3_Button.configure(highlightcolor="black")
        self.addPlayer3_Button.configure(pady="0")
        self.addPlayer3_Button.configure(text='''>''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.addPlayer3_Button, tooltip_font, '''Add/Change Player''', delay=0.5)
        self.addPlayer3_Button.configure(command=lambda: fnc.handle_add_player(self, 3))

        self.Player3_Label = tk.Label(self.Player_Canvas)
        self.Player3_Label.place(relx=0.273, rely=0.313, height=20, width=120)
        self.Player3_Label.configure(background="#d9d9d9")
        self.Player3_Label.configure(disabledforeground="#a3a3a3")
        self.Player3_Label.configure(foreground="#000000")
        self.Player3_Label.configure(text='''Player 3''')
        self.Player3_Label.configure(textvariable=gui_support.player3)

        self.removePlayer4_Button = tk.Button(self.Player_Canvas)
        self.removePlayer4_Button.place(relx=0.045, rely=0.391, height=20, width=20)
        self.removePlayer4_Button.configure(activebackground="#ececec")
        self.removePlayer4_Button.configure(activeforeground="#000000")
        self.removePlayer4_Button.configure(background="#d9d9d9")
        self.removePlayer4_Button.configure(cursor="arrow")
        self.removePlayer4_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer4_Button.configure(foreground="#000000")
        self.removePlayer4_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer4_Button.configure(highlightcolor="black")
        self.removePlayer4_Button.configure(pady="0")
        self.removePlayer4_Button.configure(text='''<''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.removePlayer4_Button, tooltip_font, '''Remove Player''', delay=0.5)
        self.removePlayer4_Button.configure(command=lambda: fnc.handle_remove_player(self, 4))

        self.addPlayer4_Button = tk.Button(self.Player_Canvas)
        self.addPlayer4_Button.place(relx=0.136, rely=0.391, height=20, width=20)
        self.addPlayer4_Button.configure(activebackground="#ececec")
        self.addPlayer4_Button.configure(activeforeground="#000000")
        self.addPlayer4_Button.configure(background="#d9d9d9")
        self.addPlayer4_Button.configure(cursor="arrow")
        self.addPlayer4_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer4_Button.configure(foreground="#000000")
        self.addPlayer4_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer4_Button.configure(highlightcolor="black")
        self.addPlayer4_Button.configure(pady="0")
        self.addPlayer4_Button.configure(text='''>''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.addPlayer4_Button, tooltip_font, '''Add/Change Player''', delay=0.5)
        self.addPlayer4_Button.configure(command=lambda: fnc.handle_add_player(self, 4))

        self.Player4_Label = tk.Label(self.Player_Canvas)
        self.Player4_Label.place(relx=0.273, rely=0.391, height=20, width=120)
        self.Player4_Label.configure(background="#d9d9d9")
        self.Player4_Label.configure(cursor="arrow")
        self.Player4_Label.configure(disabledforeground="#a3a3a3")
        self.Player4_Label.configure(foreground="#000000")
        self.Player4_Label.configure(text='''Player 4''')
        self.Player4_Label.configure(textvariable=gui_support.player4)

        self.removePlayer5_Button = tk.Button(self.Player_Canvas)
        self.removePlayer5_Button.place(relx=0.045, rely=0.469, height=20, width=20)
        self.removePlayer5_Button.configure(activebackground="#ececec")
        self.removePlayer5_Button.configure(activeforeground="#000000")
        self.removePlayer5_Button.configure(background="#d9d9d9")
        self.removePlayer5_Button.configure(cursor="arrow")
        self.removePlayer5_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer5_Button.configure(foreground="#000000")
        self.removePlayer5_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer5_Button.configure(highlightcolor="black")
        self.removePlayer5_Button.configure(pady="0")
        self.removePlayer5_Button.configure(text='''<''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.removePlayer5_Button, tooltip_font, '''Remove Player''', delay=0.5)
        self.removePlayer5_Button.configure(command=lambda: fnc.handle_remove_player(self, 5))

        self.addPlayer5_Button = tk.Button(self.Player_Canvas)
        self.addPlayer5_Button.place(relx=0.136, rely=0.469, height=20, width=20)
        self.addPlayer5_Button.configure(activebackground="#ececec")
        self.addPlayer5_Button.configure(activeforeground="#000000")
        self.addPlayer5_Button.configure(background="#d9d9d9")
        self.addPlayer5_Button.configure(cursor="arrow")
        self.addPlayer5_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer5_Button.configure(foreground="#000000")
        self.addPlayer5_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer5_Button.configure(highlightcolor="black")
        self.addPlayer5_Button.configure(pady="0")
        self.addPlayer5_Button.configure(text='''>''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.addPlayer5_Button, tooltip_font, '''Add/Change Player''', delay=0.5)
        self.addPlayer5_Button.configure(command=lambda: fnc.handle_add_player(self, 5))

        self.Player5_Label = tk.Label(self.Player_Canvas)
        self.Player5_Label.place(relx=0.273, rely=0.469, height=20, width=120)
        self.Player5_Label.configure(background="#d9d9d9")
        self.Player5_Label.configure(disabledforeground="#a3a3a3")
        self.Player5_Label.configure(foreground="#000000")
        self.Player5_Label.configure(text='''Player 5''')
        self.Player5_Label.configure(textvariable=gui_support.player5)

        self.removePlayer6_Button = tk.Button(self.Player_Canvas)
        self.removePlayer6_Button.place(relx=0.045, rely=0.547, height=20, width=20)
        self.removePlayer6_Button.configure(activebackground="#ececec")
        self.removePlayer6_Button.configure(activeforeground="#000000")
        self.removePlayer6_Button.configure(background="#d9d9d9")
        self.removePlayer6_Button.configure(cursor="arrow")
        self.removePlayer6_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer6_Button.configure(foreground="#000000")
        self.removePlayer6_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer6_Button.configure(highlightcolor="black")
        self.removePlayer6_Button.configure(pady="0")
        self.removePlayer6_Button.configure(text='''<''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.removePlayer6_Button, tooltip_font, '''Remove Player''', delay=0.5)
        self.removePlayer6_Button.configure(command=lambda: fnc.handle_remove_player(self, 6))

        self.addPlayer6_Button = tk.Button(self.Player_Canvas)
        self.addPlayer6_Button.place(relx=0.136, rely=0.547, height=20, width=20)
        self.addPlayer6_Button.configure(activebackground="#ececec")
        self.addPlayer6_Button.configure(activeforeground="#000000")
        self.addPlayer6_Button.configure(background="#d9d9d9")
        self.addPlayer6_Button.configure(cursor="arrow")
        self.addPlayer6_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer6_Button.configure(foreground="#000000")
        self.addPlayer6_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer6_Button.configure(highlightcolor="black")
        self.addPlayer6_Button.configure(pady="0")
        self.addPlayer6_Button.configure(text='''>''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.addPlayer6_Button, tooltip_font, '''Add/Change Player''', delay=0.5)
        self.addPlayer6_Button.configure(command=lambda: fnc.handle_add_player(self, 6))

        self.Player6_Label = tk.Label(self.Player_Canvas)
        self.Player6_Label.place(relx=0.273, rely=0.547, height=20, width=120)
        self.Player6_Label.configure(background="#d9d9d9")
        self.Player6_Label.configure(disabledforeground="#a3a3a3")
        self.Player6_Label.configure(foreground="#000000")
        self.Player6_Label.configure(text='''Player 6''')
        self.Player6_Label.configure(textvariable=gui_support.player6)

        self.removePlayer7_Button = tk.Button(self.Player_Canvas)
        self.removePlayer7_Button.place(relx=0.045, rely=0.625, height=20, width=20)
        self.removePlayer7_Button.configure(activebackground="#ececec")
        self.removePlayer7_Button.configure(activeforeground="#000000")
        self.removePlayer7_Button.configure(background="#d9d9d9")
        self.removePlayer7_Button.configure(cursor="arrow")
        self.removePlayer7_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer7_Button.configure(foreground="#000000")
        self.removePlayer7_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer7_Button.configure(highlightcolor="black")
        self.removePlayer7_Button.configure(pady="0")
        self.removePlayer7_Button.configure(text='''<''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.removePlayer7_Button, tooltip_font, '''Remove Player''', delay=0.5)
        self.removePlayer7_Button.configure(command=lambda: fnc.handle_remove_player(self, 7))

        self.addPlayer7_Button = tk.Button(self.Player_Canvas)
        self.addPlayer7_Button.place(relx=0.136, rely=0.625, height=20, width=20)
        self.addPlayer7_Button.configure(activebackground="#ececec")
        self.addPlayer7_Button.configure(activeforeground="#000000")
        self.addPlayer7_Button.configure(background="#d9d9d9")
        self.addPlayer7_Button.configure(cursor="arrow")
        self.addPlayer7_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer7_Button.configure(foreground="#000000")
        self.addPlayer7_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer7_Button.configure(highlightcolor="black")
        self.addPlayer7_Button.configure(pady="0")
        self.addPlayer7_Button.configure(text='''>''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.addPlayer7_Button, tooltip_font, '''Add/Change Player''', delay=0.5)
        self.addPlayer7_Button.configure(command=lambda: fnc.handle_add_player(self, 7))

        self.Player7_Label = tk.Label(self.Player_Canvas)
        self.Player7_Label.place(relx=0.273, rely=0.625, height=20, width=120)
        self.Player7_Label.configure(background="#d9d9d9")
        self.Player7_Label.configure(disabledforeground="#a3a3a3")
        self.Player7_Label.configure(foreground="#000000")
        self.Player7_Label.configure(text='''Player 7''')
        self.Player7_Label.configure(textvariable=gui_support.player7)

        self.removePlayer8_Button = tk.Button(self.Player_Canvas)
        self.removePlayer8_Button.place(relx=0.045, rely=0.703, height=20, width=20)
        self.removePlayer8_Button.configure(activebackground="#ececec")
        self.removePlayer8_Button.configure(activeforeground="#000000")
        self.removePlayer8_Button.configure(background="#d9d9d9")
        self.removePlayer8_Button.configure(cursor="arrow")
        self.removePlayer8_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer8_Button.configure(foreground="#000000")
        self.removePlayer8_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer8_Button.configure(highlightcolor="black")
        self.removePlayer8_Button.configure(pady="0")
        self.removePlayer8_Button.configure(text='''<''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.removePlayer8_Button, tooltip_font, '''Remove Player''', delay=0.5)
        self.removePlayer8_Button.configure(command=lambda: fnc.handle_remove_player(self, 8))

        self.addPlayer8_Button = tk.Button(self.Player_Canvas)
        self.addPlayer8_Button.place(relx=0.136, rely=0.703, height=20, width=20)
        self.addPlayer8_Button.configure(activebackground="#ececec")
        self.addPlayer8_Button.configure(activeforeground="#000000")
        self.addPlayer8_Button.configure(background="#d9d9d9")
        self.addPlayer8_Button.configure(cursor="arrow")
        self.addPlayer8_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer8_Button.configure(foreground="#000000")
        self.addPlayer8_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer8_Button.configure(highlightcolor="black")
        self.addPlayer8_Button.configure(pady="0")
        self.addPlayer8_Button.configure(text='''>''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.addPlayer8_Button, tooltip_font, '''Add/Change Player''', delay=0.5)
        self.addPlayer8_Button.configure(command=lambda: fnc.handle_add_player(self, 8))

        self.Player8_Label = tk.Label(self.Player_Canvas)
        self.Player8_Label.place(relx=0.273, rely=0.703, height=20, width=120)
        self.Player8_Label.configure(background="#d9d9d9")
        self.Player8_Label.configure(disabledforeground="#a3a3a3")
        self.Player8_Label.configure(foreground="#000000")
        self.Player8_Label.configure(text='''Player 8''')
        self.Player8_Label.configure(textvariable=gui_support.player8)

        self.removePlayer9_Button = tk.Button(self.Player_Canvas)
        self.removePlayer9_Button.place(relx=0.045, rely=0.781, height=20, width=20)
        self.removePlayer9_Button.configure(activebackground="#ececec")
        self.removePlayer9_Button.configure(activeforeground="#000000")
        self.removePlayer9_Button.configure(background="#d9d9d9")
        self.removePlayer9_Button.configure(cursor="arrow")
        self.removePlayer9_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer9_Button.configure(foreground="#000000")
        self.removePlayer9_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer9_Button.configure(highlightcolor="black")
        self.removePlayer9_Button.configure(pady="0")
        self.removePlayer9_Button.configure(text='''<''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.removePlayer9_Button, tooltip_font, '''Remove Player''', delay=0.5)
        self.removePlayer9_Button.configure(command=lambda: fnc.handle_remove_player(self, 9))

        self.addPlayer9_Button = tk.Button(self.Player_Canvas)
        self.addPlayer9_Button.place(relx=0.136, rely=0.781, height=20, width=20)
        self.addPlayer9_Button.configure(activebackground="#ececec")
        self.addPlayer9_Button.configure(activeforeground="#000000")
        self.addPlayer9_Button.configure(background="#d9d9d9")
        self.addPlayer9_Button.configure(cursor="arrow")
        self.addPlayer9_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer9_Button.configure(foreground="#000000")
        self.addPlayer9_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer9_Button.configure(highlightcolor="black")
        self.addPlayer9_Button.configure(pady="0")
        self.addPlayer9_Button.configure(text='''>''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.addPlayer9_Button, tooltip_font, '''Add/Change Player''', delay=0.5)
        self.addPlayer9_Button.configure(command=lambda: fnc.handle_add_player(self, 9))

        self.Player9_Label = tk.Label(self.Player_Canvas)
        self.Player9_Label.place(relx=0.273, rely=0.781, height=20, width=120)
        self.Player9_Label.configure(background="#d9d9d9")
        self.Player9_Label.configure(disabledforeground="#a3a3a3")
        self.Player9_Label.configure(foreground="#000000")
        self.Player9_Label.configure(text='''Player 9''')
        self.Player9_Label.configure(textvariable=gui_support.player9)

        self.removePlayer10_Button = tk.Button(self.Player_Canvas)
        self.removePlayer10_Button.place(relx=0.045, rely=0.859, height=20, width=20)
        self.removePlayer10_Button.configure(activebackground="#ececec")
        self.removePlayer10_Button.configure(activeforeground="#000000")
        self.removePlayer10_Button.configure(background="#d9d9d9")
        self.removePlayer10_Button.configure(cursor="arrow")
        self.removePlayer10_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer10_Button.configure(foreground="#000000")
        self.removePlayer10_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer10_Button.configure(highlightcolor="black")
        self.removePlayer10_Button.configure(pady="0")
        self.removePlayer10_Button.configure(text='''<''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.removePlayer10_Button, tooltip_font, '''Remove Player''', delay=0.5)
        self.removePlayer10_Button.configure(command=lambda: fnc.handle_remove_player(self, 10))

        self.addPlayer10_Button = tk.Button(self.Player_Canvas)
        self.addPlayer10_Button.place(relx=0.136, rely=0.859, height=20, width=20)
        self.addPlayer10_Button.configure(activebackground="#ececec")
        self.addPlayer10_Button.configure(activeforeground="#000000")
        self.addPlayer10_Button.configure(background="#d9d9d9")
        self.addPlayer10_Button.configure(cursor="arrow")
        self.addPlayer10_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer10_Button.configure(foreground="#000000")
        self.addPlayer10_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer10_Button.configure(highlightcolor="black")
        self.addPlayer10_Button.configure(pady="0")
        self.addPlayer10_Button.configure(text='''>''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.addPlayer10_Button, tooltip_font, '''Add/Change Player''', delay=0.5)
        self.addPlayer10_Button.configure(command=lambda: fnc.handle_add_player(self, 10))

        self.Player10_Label = tk.Label(self.Player_Canvas)
        self.Player10_Label.place(relx=0.273, rely=0.859, height=20, width=120)
        self.Player10_Label.configure(background="#d9d9d9")
        self.Player10_Label.configure(disabledforeground="#a3a3a3")
        self.Player10_Label.configure(foreground="#000000")
        self.Player10_Label.configure(text='''Player 10''')
        self.Player10_Label.configure(textvariable=gui_support.player10)

        self.PlayerEntry_Label = tk.Label(top)
        self.PlayerEntry_Label.place(relx=0.039, rely=0.042, height=20, width=60)
        self.PlayerEntry_Label.configure(background="#d9d9d9")
        self.PlayerEntry_Label.configure(cursor="arrow")
        self.PlayerEntry_Label.configure(disabledforeground="#a3a3a3")
        self.PlayerEntry_Label.configure(foreground="#000000")
        self.PlayerEntry_Label.configure(text='''Player:''')

        self.Matchmaking_Text = tk.Text(top)
        self.Matchmaking_Text.place(relx=0.422, rely=0.146, relheight=0.667, relwidth=0.531)
        self.Matchmaking_Text.configure(background="white")
        self.Matchmaking_Text.configure(cursor="arrow")
        self.Matchmaking_Text.configure(font="TkTextFont")
        self.Matchmaking_Text.configure(foreground="black")
        self.Matchmaking_Text.configure(highlightbackground="#d9d9d9")
        self.Matchmaking_Text.configure(highlightcolor="black")
        self.Matchmaking_Text.configure(insertbackground="black")
        self.Matchmaking_Text.configure(selectbackground="#c4c4c4")
        self.Matchmaking_Text.configure(selectforeground="black")
        self.Matchmaking_Text.configure(wrap="word")


# ======================================================
# Modified by Rozen to remove Tkinter import statements and to receive
# the font as an argument.
# ======================================================
# Found the original code at:
# http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
# ======================================================


class ToolTip(tk.Toplevel):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    """

    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=0.25, follow=True):
        """
        Initialize the ToolTip

        Arguments:
          wdgt: The widget this ToolTip is assigned to
          tooltip_font: Font to be used
          msg:  A static string message assigned to the ToolTip
          msgFunc: A function that retrieves a string to use as the ToolTip text
          delay:   The delay in seconds before the ToolTip appears(may be float)
          follow:  If True, the ToolTip follows motion, otherwise hides
        """
        self.wdgt = wdgt
        # The parent of the ToolTip is the parent of the ToolTips widget
        self.parent = self.wdgt.master
        # Initalise the Toplevel
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        # Hide initially
        self.withdraw()
        # The ToolTip Toplevel should have no frame or title bar
        self.overrideredirect(True)

        # The msgVar will contain the text displayed by the ToolTip
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        # The text of the ToolTip is displayed in a Message widget
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                   font=tooltip_font,
                   aspect=1000).grid()

        # Add bindings to the widget.  This will NOT override
        # bindings that the widget already has
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')

    def spawn(self, event=None):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget

        Arguments:
          event: The event that called this funciton
        """
        self.visible = 1
        # The after function takes a time argument in miliseconds
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        """
        Processes motion within the widget.
        Arguments:
          event: The event that called this function
        """
        self.lastMotion = time()
        # If the follow flag is not set, motion within the
        # widget will make the ToolTip disappear
        #
        if self.follow is False:
            self.withdraw()
            self.visible = 1

        # Offset the ToolTip 10x10 pixes southwest of the pointer
        self.geometry('+%i+%i' % (event.x_root + 20, event.y_root - 10))
        try:
            # Try to call the message function.  Will not change
            # the message if the message function is None or
            # the message function fails
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget
        Arguments:
          event: The event that called this function
        """
        self.visible = 0
        self.withdraw()


# ===========================================================
#                   End of Class ToolTip
# ===========================================================

if __name__ == '__main__':
    vp_start_gui()
