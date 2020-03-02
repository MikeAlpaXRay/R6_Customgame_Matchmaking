import functions as fnc
import gui

if __name__ == "__main__":
    player_name_list = fnc.load_json()

    gui.vp_start_gui(player_name_list)
    fnc.save_json()
