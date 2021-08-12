from bin import gui, etc
import tkinter as tk
import json
from random import random

#implement safe here
def main():
    #open config file and fetch and make random name
    global config
    global output
    global window
    config = json.loads(open("config.json", mode="r").read())
    
    #standard config
    if config["standard-savepath"] != "":
        standard = config["standard-savepath"] + "/" + str(round(random()*100000 + 1)) + ".avi"
        output = standard
    else:
        standard = "Outputpath"
    
    #construct main window and call GUI
    
    window = tk.Tk()
    window.title("RhubarbBarbara by Christoferis (v1.0)")
    
    gui(window=window, stdpath=standard)


    window.mainloop()
    
    pass

if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        etc.error(e)
