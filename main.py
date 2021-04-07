#RhubarbBarbara is a Python tool for using Rhubarb

from tkinter.constants import LEFT, RIGHT
import moviepy as mov
import tkinter as tk
from PIL import Image




#ⒶⒷⒸⒹⒺⒻ extended shapes(ⒼⒽⓍ)

#GUI

class mouthSelector:

    def __init__(self, window, mouthshape):
        self.window = window
        self.logo = mouthshape

        #mouthshape selector:
        if mouthshape in ("Ⓐ","Ⓑ","Ⓒ","Ⓓ","Ⓔ","Ⓕ"):
            self.ext = False
        else:
            self.ext = True
        
        pass

    def create_wid(self):

        shape = tk.Frame(self.window)
        
        #mouthshape îdentifier
        tk.Label(shape, text=self.mouthshape).pack(side=LEFT)
        #Image preview
        


        #build frame
        shape.pack()
        return 



def gui(window):
    #make main Frame for the images

    #Frame for the start Button and Audio Input
    bottom = tk.Frame(window)
    
    tk.Text(bottom).pack(side=LEFT)

    #start button
    tk.Button(bottom, text="start").pack(side=RIGHT)
    #search file button
    tk.Button(bottom, text="Open Audio File").pack(side=RIGHT)

    bottom.pack()





def main():
    #construct main window
    window = tk.Tk()

    gui(window=window)


    window.mainloop()
    pass

main()