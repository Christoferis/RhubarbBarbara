#RhubarbBarbara is a Python tool for using Rhubarb

import tkinter as tk
import tkinter.filedialog as fd
from tkinter.constants import BOTH, BOTTOM, END, LEFT, RIGHT, TOP, X, Y

import moviepy as mov
from PIL import Image, ImageTk

mouthshapes = dict()

#ⒶⒷⒸⒹⒺⒻ extended shapes(ⒼⒽⓍ)

#GUI

class mouthSelector:

    def __init__(self, window, mouthshape):
        self.window = window
        self.logo = mouthshape + "\n "
        

        #mouthshape selector:
        if mouthshape in ("A","B","C","D","E","F"):
            self.ext = False
        else:
            self.ext = True

        if mouthshape == "A":
            self.image = "icons\lisa-A.png"
        elif mouthshape == "B":
            self.image = "icons\lisa-B.png"
        elif mouthshape == "C":
            self.image = "icons\lisa-C.png"
        elif mouthshape == "D":
            self.image = "icons\lisa-D.png"
        elif mouthshape == "E":
            self.image = "icons\lisa-E.png"
        elif mouthshape == "F":
            self.image = "icons\lisa-F.png"
        elif mouthshape == "G":
            self.image = "icons\lisa-G.png"
        elif mouthshape == "H":
            self.image = "icons\lisa-H.png"
        elif mouthshape == "X":
            self.image = "icons\lisa-X.png"
        
        pass

    def create_wid(self):

        shape = tk.Frame(self.window)
        
        #mouthshape îdentifier
        if self.ext == True:
            prevstr = self.logo + "\n " + "(Optional)"
        else:
            prevstr = self.logo

        tk.Label(shape, text=prevstr).pack(side=LEFT)

        #Mouthshape preview (https://github.com/DanielSWolf/rhubarb-lip-sync#readme)
        img = ImageTk.PhotoImage(Image.open(self.image).resize((75, 62)))
        imgframe = tk.Label(shape, image=img)
        imgframe.image = img
        imgframe.pack(side=LEFT)

        #button to open filedialog
        tk.Button(shape, text="add a image", command=self.add_to_dict).pack(side=RIGHT, fill=BOTH)
        
        return shape

    def add_to_dict(self):
        global mouthshapes
        shape = fd.askopenfile()
        
        #mouthshapes[self.logo] = shape


def gui(window):
    #make main Frame for the images
    top = tk.Frame(window)

    for shape in ("X","H","G","F","E","D","C","B","A"):
        frame = mouthSelector(window=top, mouthshape=shape)
        frame.create_wid().pack(side=BOTTOM)

    top.pack(expand=2, pady=50, fill=BOTH)

    #Frame for the start Button and Audio Input
    bottom = tk.Frame(window)
    
    audiopath = tk.Entry(bottom)
    audiopath.pack(side=LEFT, expand=1, fill=X)
    audiopath.insert(END, "Path to audio")

    #start button
    tk.Button(bottom, text="start").pack(side=RIGHT)
    #search file button
    tk.Button(bottom, text="Open Audio File").pack(side=RIGHT)

    bottom.pack(side=BOTTOM, fill=BOTH, expand=2)


def main():
    #construct main window
    window = tk.Tk()

    gui(window=window)


    window.mainloop()
    pass

main()
