from bin import gui, etc
import tkinter as tk

#implement safe here
def main():
    #open config file and fetch and make random name
    global config
    global output
    global window

    
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
