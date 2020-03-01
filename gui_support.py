import sys
import tkinter as tk
import tkinter.ttk as ttk

py3 = True


def set_Tk_var():
    global player1
    player1 = tk.StringVar()
    player1.set('Player 1')
    global player2
    player2 = tk.StringVar()
    player2.set('Player 2')
    global player3
    player3 = tk.StringVar()
    player3.set('Player 3')
    global player4
    player4 = tk.StringVar()
    player4.set('Player 4')
    global player5
    player5 = tk.StringVar()
    player5.set('Player 5')
    global player6
    player6 = tk.StringVar()
    player6.set('Player 6')
    global player7
    player7 = tk.StringVar()
    player7.set('Player 7')
    global player8
    player8 = tk.StringVar()
    player8.set('Player 8')
    global player9
    player9 = tk.StringVar()
    player9.set('Player 9')
    global player10
    player10 = tk.StringVar()
    player10.set('Player 10')


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import unknown

    unknown.vp_start_gui()
