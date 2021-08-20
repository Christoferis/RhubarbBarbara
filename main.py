from bin import gui, etc
import tkinter as tk

#implement safe here
def main():
    #open config file and fetch and make random name    
    #construct main window and call GUI
    
    window = tk.Tk()
    window.title(etc.TITLE)
    
    gui.gui(window=window)

    window.mainloop()    
    pass

if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        etc.error(e)
