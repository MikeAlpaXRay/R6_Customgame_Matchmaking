import tkinter as tk
import tkinter.ttk as ttk
import functions as fnc

#ToDo: Layout
#ToDo:_changePlayer function
#ToDo: Rewrite?



py3 = True

import gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    gui_support.set_Tk_var()
    top = Toplevel1 (root)
    gui_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    gui_support.set_Tk_var()
    top = Toplevel1 (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("640x480+1357+318")
        top.minsize(500, 360)
        top.maxsize(854, 480)
        top.resizable(0, 0)
        top.title("R6 Custom Matchmaking")
        top.configure(background="#d9d9d9")

        self.Player_Entry = tk.Entry(top)
        self.Player_Entry.place(relx=0.047, rely=0.083, height=20
                , relwidth=0.188)
        self.Player_Entry.configure(background="white")
        self.Player_Entry.configure(cursor="fleur")
        self.Player_Entry.configure(disabledforeground="#a3a3a3")
        self.Player_Entry.configure(font="TkFixedFont")
        self.Player_Entry.configure(foreground="#000000")
        self.Player_Entry.configure(insertbackground="black")

        self.Player_Canvas = tk.Canvas(top)
        self.Player_Canvas.place(relx=0.047, rely=0.146, relheight=0.667
                , relwidth=0.344)
        self.Player_Canvas.configure(background="#d9d9d9")
        self.Player_Canvas.configure(borderwidth="2")
        self.Player_Canvas.configure(cursor="fleur")
        self.Player_Canvas.configure(insertbackground="black")
        self.Player_Canvas.configure(relief="ridge")
        self.Player_Canvas.configure(selectbackground="#c4c4c4")
        self.Player_Canvas.configure(selectforeground="black")

        self.PlayerCanvas_Label = tk.Label(self.Player_Canvas)
        self.PlayerCanvas_Label.place(relx=0.091, rely=0.063, height=20
                , width=50)
        self.PlayerCanvas_Label.configure(background="#d9d9d9")
        self.PlayerCanvas_Label.configure(disabledforeground="#a3a3a3")
        self.PlayerCanvas_Label.configure(foreground="#000000")
        self.PlayerCanvas_Label.configure(text='''Players:''')

        self.removePlayer1_Button = tk.Button(self.Player_Canvas)
        self.removePlayer1_Button.place(relx=0.045, rely=0.156, height=20
                , width=20)
        self.removePlayer1_Button.configure(activebackground="#ececec")
        self.removePlayer1_Button.configure(activeforeground="#000000")
        self.removePlayer1_Button.configure(background="#d9d9d9")
        self.removePlayer1_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer1_Button.configure(foreground="#000000")
        self.removePlayer1_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer1_Button.configure(highlightcolor="black")
        self.removePlayer1_Button.configure(pady="0")
        self.removePlayer1_Button.configure(text='''<''')

        self.addPlayer1_Button = tk.Button(self.Player_Canvas)
        self.addPlayer1_Button.place(relx=0.136, rely=0.156, height=20, width=20)

        self.addPlayer1_Button.configure(activebackground="#ececec")
        self.addPlayer1_Button.configure(activeforeground="#000000")
        self.addPlayer1_Button.configure(background="#d9d9d9")
        self.addPlayer1_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer1_Button.configure(foreground="#000000")
        self.addPlayer1_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer1_Button.configure(highlightcolor="black")
        self.addPlayer1_Button.configure(pady="0")
        self.addPlayer1_Button.configure(text='''>''')

        self.Player1_Label = tk.Label(self.Player_Canvas)
        self.Player1_Label.place(relx=0.273, rely=0.156, height=20, width=120)
        self.Player1_Label.configure(background="#d9d9d9")
        self.Player1_Label.configure(disabledforeground="#a3a3a3")
        self.Player1_Label.configure(foreground="#000000")
        self.Player1_Label.configure(text='''Player 1''')
        self.Player1_Label.configure(textvariable=gui_support.player1)

        self.removePlayer2_Button = tk.Button(self.Player_Canvas)
        self.removePlayer2_Button.place(relx=0.045, rely=0.234, height=20
                , width=20)
        self.removePlayer2_Button.configure(activebackground="#ececec")
        self.removePlayer2_Button.configure(activeforeground="#000000")
        self.removePlayer2_Button.configure(background="#d9d9d9")
        self.removePlayer2_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer2_Button.configure(foreground="#000000")
        self.removePlayer2_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer2_Button.configure(highlightcolor="black")
        self.removePlayer2_Button.configure(pady="0")
        self.removePlayer2_Button.configure(text='''<''')

        self.addPlayer2_Button = tk.Button(self.Player_Canvas)
        self.addPlayer2_Button.place(relx=0.136, rely=0.234, height=20, width=20)

        self.addPlayer2_Button.configure(activebackground="#ececec")
        self.addPlayer2_Button.configure(activeforeground="#000000")
        self.addPlayer2_Button.configure(background="#d9d9d9")
        self.addPlayer2_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer2_Button.configure(foreground="#000000")
        self.addPlayer2_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer2_Button.configure(highlightcolor="black")
        self.addPlayer2_Button.configure(pady="0")
        self.addPlayer2_Button.configure(text='''>''')

        self.Player2_Label = tk.Label(self.Player_Canvas)
        self.Player2_Label.place(relx=0.273, rely=0.234, height=20, width=120)
        self.Player2_Label.configure(background="#d9d9d9")
        self.Player2_Label.configure(cursor="fleur")
        self.Player2_Label.configure(disabledforeground="#a3a3a3")
        self.Player2_Label.configure(foreground="#000000")
        self.Player2_Label.configure(text='''Player 2''')
        self.Player2_Label.configure(textvariable=gui_support.player2)

        self.removePlayer3_Button = tk.Button(self.Player_Canvas)
        self.removePlayer3_Button.place(relx=0.045, rely=0.313, height=20
                , width=20)
        self.removePlayer3_Button.configure(activebackground="#ececec")
        self.removePlayer3_Button.configure(activeforeground="#000000")
        self.removePlayer3_Button.configure(background="#d9d9d9")
        self.removePlayer3_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer3_Button.configure(foreground="#000000")
        self.removePlayer3_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer3_Button.configure(highlightcolor="black")
        self.removePlayer3_Button.configure(pady="0")
        self.removePlayer3_Button.configure(text='''<''')

        self.addPlayer3_Button = tk.Button(self.Player_Canvas)
        self.addPlayer3_Button.place(relx=0.136, rely=0.313, height=20, width=20)

        self.addPlayer3_Button.configure(activebackground="#ececec")
        self.addPlayer3_Button.configure(activeforeground="#000000")
        self.addPlayer3_Button.configure(background="#d9d9d9")
        self.addPlayer3_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer3_Button.configure(foreground="#000000")
        self.addPlayer3_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer3_Button.configure(highlightcolor="black")
        self.addPlayer3_Button.configure(pady="0")
        self.addPlayer3_Button.configure(text='''>''')

        self.Player3_Label = tk.Label(self.Player_Canvas)
        self.Player3_Label.place(relx=0.273, rely=0.313, height=20, width=120)
        self.Player3_Label.configure(background="#d9d9d9")
        self.Player3_Label.configure(disabledforeground="#a3a3a3")
        self.Player3_Label.configure(foreground="#000000")
        self.Player3_Label.configure(text='''Player 3''')
        self.Player3_Label.configure(textvariable=gui_support.player3)

        self.removePlayer4_Button = tk.Button(self.Player_Canvas)
        self.removePlayer4_Button.place(relx=0.045, rely=0.391, height=20
                , width=20)
        self.removePlayer4_Button.configure(activebackground="#ececec")
        self.removePlayer4_Button.configure(activeforeground="#000000")
        self.removePlayer4_Button.configure(background="#d9d9d9")
        self.removePlayer4_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer4_Button.configure(foreground="#000000")
        self.removePlayer4_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer4_Button.configure(highlightcolor="black")
        self.removePlayer4_Button.configure(pady="0")
        self.removePlayer4_Button.configure(text='''<''')

        self.addPlayer4_Button = tk.Button(self.Player_Canvas)
        self.addPlayer4_Button.place(relx=0.136, rely=0.391, height=20, width=20)

        self.addPlayer4_Button.configure(activebackground="#ececec")
        self.addPlayer4_Button.configure(activeforeground="#000000")
        self.addPlayer4_Button.configure(background="#d9d9d9")
        self.addPlayer4_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer4_Button.configure(foreground="#000000")
        self.addPlayer4_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer4_Button.configure(highlightcolor="black")
        self.addPlayer4_Button.configure(pady="0")
        self.addPlayer4_Button.configure(text='''>''')

        self.Player4_Label = tk.Label(self.Player_Canvas)
        self.Player4_Label.place(relx=0.273, rely=0.391, height=20, width=120)
        self.Player4_Label.configure(background="#d9d9d9")
        self.Player4_Label.configure(cursor="fleur")
        self.Player4_Label.configure(disabledforeground="#a3a3a3")
        self.Player4_Label.configure(foreground="#000000")
        self.Player4_Label.configure(text='''Player 4''')
        self.Player4_Label.configure(textvariable=gui_support.player4)

        self.removePlayer5_Button = tk.Button(self.Player_Canvas)
        self.removePlayer5_Button.place(relx=0.045, rely=0.469, height=20
                , width=20)
        self.removePlayer5_Button.configure(activebackground="#ececec")
        self.removePlayer5_Button.configure(activeforeground="#000000")
        self.removePlayer5_Button.configure(background="#d9d9d9")
        self.removePlayer5_Button.configure(cursor="fleur")
        self.removePlayer5_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer5_Button.configure(foreground="#000000")
        self.removePlayer5_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer5_Button.configure(highlightcolor="black")
        self.removePlayer5_Button.configure(pady="0")
        self.removePlayer5_Button.configure(text='''<''')

        self.addPlayer5_Player = tk.Button(self.Player_Canvas)
        self.addPlayer5_Player.place(relx=0.136, rely=0.469, height=20, width=20)

        self.addPlayer5_Player.configure(activebackground="#ececec")
        self.addPlayer5_Player.configure(activeforeground="#000000")
        self.addPlayer5_Player.configure(background="#d9d9d9")
        self.addPlayer5_Player.configure(disabledforeground="#a3a3a3")
        self.addPlayer5_Player.configure(foreground="#000000")
        self.addPlayer5_Player.configure(highlightbackground="#d9d9d9")
        self.addPlayer5_Player.configure(highlightcolor="black")
        self.addPlayer5_Player.configure(pady="0")
        self.addPlayer5_Player.configure(text='''>''')

        self.Player5_Label = tk.Label(self.Player_Canvas)
        self.Player5_Label.place(relx=0.273, rely=0.469, height=20, width=120)
        self.Player5_Label.configure(background="#d9d9d9")
        self.Player5_Label.configure(disabledforeground="#a3a3a3")
        self.Player5_Label.configure(foreground="#000000")
        self.Player5_Label.configure(text='''Player 5''')
        self.Player5_Label.configure(textvariable=gui_support.player5)

        self.removePlayer6_Button = tk.Button(self.Player_Canvas)
        self.removePlayer6_Button.place(relx=0.045, rely=0.547, height=20
                , width=20)
        self.removePlayer6_Button.configure(activebackground="#ececec")
        self.removePlayer6_Button.configure(activeforeground="#000000")
        self.removePlayer6_Button.configure(background="#d9d9d9")
        self.removePlayer6_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer6_Button.configure(foreground="#000000")
        self.removePlayer6_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer6_Button.configure(highlightcolor="black")
        self.removePlayer6_Button.configure(pady="0")
        self.removePlayer6_Button.configure(text='''<''')

        self.addPlayer6_Button = tk.Button(self.Player_Canvas)
        self.addPlayer6_Button.place(relx=0.136, rely=0.547, height=20, width=20)

        self.addPlayer6_Button.configure(activebackground="#ececec")
        self.addPlayer6_Button.configure(activeforeground="#000000")
        self.addPlayer6_Button.configure(background="#d9d9d9")
        self.addPlayer6_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer6_Button.configure(foreground="#000000")
        self.addPlayer6_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer6_Button.configure(highlightcolor="black")
        self.addPlayer6_Button.configure(pady="0")
        self.addPlayer6_Button.configure(text='''>''')

        self.Player6_Label = tk.Label(self.Player_Canvas)
        self.Player6_Label.place(relx=0.273, rely=0.547, height=20, width=120)
        self.Player6_Label.configure(background="#d9d9d9")
        self.Player6_Label.configure(disabledforeground="#a3a3a3")
        self.Player6_Label.configure(foreground="#000000")
        self.Player6_Label.configure(text='''Player 6''')
        self.Player6_Label.configure(textvariable=gui_support.player6)

        self.removePlayer7_Button = tk.Button(self.Player_Canvas)
        self.removePlayer7_Button.place(relx=0.045, rely=0.625, height=20
                , width=20)
        self.removePlayer7_Button.configure(activebackground="#ececec")
        self.removePlayer7_Button.configure(activeforeground="#000000")
        self.removePlayer7_Button.configure(background="#d9d9d9")
        self.removePlayer7_Button.configure(cursor="fleur")
        self.removePlayer7_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer7_Button.configure(foreground="#000000")
        self.removePlayer7_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer7_Button.configure(highlightcolor="black")
        self.removePlayer7_Button.configure(pady="0")
        self.removePlayer7_Button.configure(text='''<''')

        self.addPlayer7_Button = tk.Button(self.Player_Canvas)
        self.addPlayer7_Button.place(relx=0.136, rely=0.625, height=20, width=20)

        self.addPlayer7_Button.configure(activebackground="#ececec")
        self.addPlayer7_Button.configure(activeforeground="#000000")
        self.addPlayer7_Button.configure(background="#d9d9d9")
        self.addPlayer7_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer7_Button.configure(foreground="#000000")
        self.addPlayer7_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer7_Button.configure(highlightcolor="black")
        self.addPlayer7_Button.configure(pady="0")
        self.addPlayer7_Button.configure(text='''>''')

        self.Player7_Label = tk.Label(self.Player_Canvas)
        self.Player7_Label.place(relx=0.273, rely=0.625, height=20, width=120)
        self.Player7_Label.configure(background="#d9d9d9")
        self.Player7_Label.configure(disabledforeground="#a3a3a3")
        self.Player7_Label.configure(foreground="#000000")
        self.Player7_Label.configure(text='''Player 7''')
        self.Player7_Label.configure(textvariable=gui_support.player7)

        self.removePlayer8_Button = tk.Button(self.Player_Canvas)
        self.removePlayer8_Button.place(relx=0.045, rely=0.703, height=20
                , width=20)
        self.removePlayer8_Button.configure(activebackground="#ececec")
        self.removePlayer8_Button.configure(activeforeground="#000000")
        self.removePlayer8_Button.configure(background="#d9d9d9")
        self.removePlayer8_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer8_Button.configure(foreground="#000000")
        self.removePlayer8_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer8_Button.configure(highlightcolor="black")
        self.removePlayer8_Button.configure(pady="0")
        self.removePlayer8_Button.configure(text='''<''')

        self.addPlayer8_Button = tk.Button(self.Player_Canvas)
        self.addPlayer8_Button.place(relx=0.136, rely=0.703, height=20, width=20)

        self.addPlayer8_Button.configure(activebackground="#ececec")
        self.addPlayer8_Button.configure(activeforeground="#000000")
        self.addPlayer8_Button.configure(background="#d9d9d9")
        self.addPlayer8_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer8_Button.configure(foreground="#000000")
        self.addPlayer8_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer8_Button.configure(highlightcolor="black")
        self.addPlayer8_Button.configure(pady="0")
        self.addPlayer8_Button.configure(text='''>''')

        self.Player8_Label = tk.Label(self.Player_Canvas)
        self.Player8_Label.place(relx=0.273, rely=0.703, height=20, width=120)
        self.Player8_Label.configure(background="#d9d9d9")
        self.Player8_Label.configure(disabledforeground="#a3a3a3")
        self.Player8_Label.configure(foreground="#000000")
        self.Player8_Label.configure(text='''Player 8''')
        self.Player8_Label.configure(textvariable=gui_support.player8)

        self.removePlayer9_Button = tk.Button(self.Player_Canvas)
        self.removePlayer9_Button.place(relx=0.045, rely=0.781, height=20
                , width=20)
        self.removePlayer9_Button.configure(activebackground="#ececec")
        self.removePlayer9_Button.configure(activeforeground="#000000")
        self.removePlayer9_Button.configure(background="#d9d9d9")
        self.removePlayer9_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer9_Button.configure(foreground="#000000")
        self.removePlayer9_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer9_Button.configure(highlightcolor="black")
        self.removePlayer9_Button.configure(pady="0")
        self.removePlayer9_Button.configure(text='''<''')

        self.addPlayer9_Button = tk.Button(self.Player_Canvas)
        self.addPlayer9_Button.place(relx=0.136, rely=0.781, height=20, width=20)

        self.addPlayer9_Button.configure(activebackground="#ececec")
        self.addPlayer9_Button.configure(activeforeground="#000000")
        self.addPlayer9_Button.configure(background="#d9d9d9")
        self.addPlayer9_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer9_Button.configure(foreground="#000000")
        self.addPlayer9_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer9_Button.configure(highlightcolor="black")
        self.addPlayer9_Button.configure(pady="0")
        self.addPlayer9_Button.configure(text='''>''')

        self.Player9_Label = tk.Label(self.Player_Canvas)
        self.Player9_Label.place(relx=0.273, rely=0.781, height=20, width=120)
        self.Player9_Label.configure(background="#d9d9d9")
        self.Player9_Label.configure(disabledforeground="#a3a3a3")
        self.Player9_Label.configure(foreground="#000000")
        self.Player9_Label.configure(text='''Player 9''')
        self.Player9_Label.configure(textvariable=gui_support.player9)

        self.removePlayer10_Button = tk.Button(self.Player_Canvas)
        self.removePlayer10_Button.place(relx=0.045, rely=0.859, height=20
                , width=20)
        self.removePlayer10_Button.configure(activebackground="#ececec")
        self.removePlayer10_Button.configure(activeforeground="#000000")
        self.removePlayer10_Button.configure(background="#d9d9d9")
        self.removePlayer10_Button.configure(disabledforeground="#a3a3a3")
        self.removePlayer10_Button.configure(foreground="#000000")
        self.removePlayer10_Button.configure(highlightbackground="#d9d9d9")
        self.removePlayer10_Button.configure(highlightcolor="black")
        self.removePlayer10_Button.configure(pady="0")
        self.removePlayer10_Button.configure(text='''<''')

        self.addPlayer10_Button = tk.Button(self.Player_Canvas)
        self.addPlayer10_Button.place(relx=0.136, rely=0.859, height=20
                , width=20)
        self.addPlayer10_Button.configure(activebackground="#ececec")
        self.addPlayer10_Button.configure(activeforeground="#000000")
        self.addPlayer10_Button.configure(background="#d9d9d9")
        self.addPlayer10_Button.configure(disabledforeground="#a3a3a3")
        self.addPlayer10_Button.configure(foreground="#000000")
        self.addPlayer10_Button.configure(highlightbackground="#d9d9d9")
        self.addPlayer10_Button.configure(highlightcolor="black")
        self.addPlayer10_Button.configure(pady="0")
        self.addPlayer10_Button.configure(text='''>''')

        self.Player10_Label = tk.Label(self.Player_Canvas)
        self.Player10_Label.place(relx=0.273, rely=0.859, height=20, width=120)
        self.Player10_Label.configure(background="#d9d9d9")
        self.Player10_Label.configure(disabledforeground="#a3a3a3")
        self.Player10_Label.configure(foreground="#000000")
        self.Player10_Label.configure(text='''Player 10''')
        self.Player10_Label.configure(textvariable=gui_support.player10)

        self.PlayerEntry:Label = tk.Label(top)
        self.PlayerEntry:Label.place(relx=0.039, rely=0.042, height=20, width=60)

        self.PlayerEntry:Label.configure(background="#d9d9d9")
        self.PlayerEntry:Label.configure(cursor="fleur")
        self.PlayerEntry:Label.configure(disabledforeground="#a3a3a3")
        self.PlayerEntry:Label.configure(foreground="#000000")
        self.PlayerEntry:Label.configure(text='''Player:''')

        self.Matchmaking_Text = tk.Text(top)
        self.Matchmaking_Text.place(relx=0.422, rely=0.146, relheight=0.667
                , relwidth=0.531)
        self.Matchmaking_Text.configure(background="white")
        self.Matchmaking_Text.configure(cursor="fleur")
        self.Matchmaking_Text.configure(font="TkTextFont")
        self.Matchmaking_Text.configure(foreground="black")
        self.Matchmaking_Text.configure(highlightbackground="#d9d9d9")
        self.Matchmaking_Text.configure(highlightcolor="black")
        self.Matchmaking_Text.configure(insertbackground="black")
        self.Matchmaking_Text.configure(selectbackground="#c4c4c4")
        self.Matchmaking_Text.configure(selectforeground="black")
        self.Matchmaking_Text.configure(wrap="word")

if __name__ == '__main__':
    vp_start_gui()
