from bin import etc, gui
import tkinter as tk

#implement safe here
def main():

    #open config file and fetch and make random name    
    #construct main window and call GUI
    
    window = tk.Tk()
    window.title(etc.TITLE)
    
    gui.gui.gui(window=window)
    
    window.mainloop()
    pass


if __name__ == "__main__":

    main()

 #   try:
  #      main()
   # except Exception as e:
    #    etc.error(e)
