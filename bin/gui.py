#Main GUI Module

#imports
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

from PIL import Image, ImageTk

from bin import etc, globals, util, rendering


#class for the mouthSelector
class mouthSelector:

    def __init__(self, window, mouthshape):
        self.window = window
        self.logo = mouthshape
        self.button = None
        

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

        tk.Label(shape, text=prevstr).pack(side="left")

        #Mouthshape preview (https://github.com/DanielSWolf/rhubarb-lip-sync#readme)
        img = ImageTk.PhotoImage(Image.open(self.image).resize((75, 62)))
        imgframe = tk.Label(shape, image=img)
        imgframe.image = img
        imgframe.pack(side="left")


        #button to remove image
        rembutton = tk.Button(shape, text="X", command=self.remove_from_dict)
        rembutton.pack(side="right", fill="both")

        #button to open filedialog
        self.button = tk.Button(shape, text="Add an Image", command=self.add_to_dict)
        self.button.pack(side="right", fill="both")

        
        return shape

    def remove_from_dict(self):
        #reset button color
        self.button.config(background="#F0F0F0", foreground="black")

        #remove from dict
        try:
            del globals.MOUTHSHAPES[self.logo]
        except KeyError:
            pass

        pass

    def add_to_dict(self):
        #add in only png images / jpg 
        shape = fd.askopenfilename(defaultextension=".png")
        
        
        if shape != "":
            #open and append to dict
            globals.MOUTHSHAPES[self.logo] = shape

            #set button color
            self.button.config(background="blue", foreground="white")
        else:
            print(shape)



#Main GUI Function
def gui(window):

    #about page
    tk.Button(window, text="Credits + Help", command=etc.about).pack(side="top")

    #make main Frame for the images
    top = tk.Frame(window)

    for shape in ("X","H","G","F","E","D","C","B","A"):
        frame = mouthSelector(window=top, mouthshape=shape)
        frame.create_wid().pack(side="bottom")

    top.pack(expand=2, pady=10, fill="both")

    #Frame for the start Button and Audio Input
    bottom = tk.Frame(window)
    
    #audio Entry box + Stringvar
    audiopath = tk.StringVar()
    audiopath.set("Path to Audio")

    audio = tk.Entry(bottom, state="readonly", textvariable=audiopath)
    audio.pack(side="left", expand=1, fill="x")

    #outputpath
    outputpath = tk.StringVar()
    outputpath.set(globals.SAVE)

    output = tk.Entry(bottom, state="readonly", textvariable=outputpath)
    output.pack(side="left", expand=1, fill="x")

    #start button
    tk.Button(bottom, text="start", background="green", foreground="white", command=rendering.start).pack(side="right", fill="both")
    
    #search file buttons
    #Audio File Button
    tk.Button(bottom, text="Open Audio File", command=lambda: util.get_path(audiopath, type="audio")).pack(side="right", fill="both")

    #Output Button
    tk.Button(bottom, text="Set Output", command=lambda: util.get_path(outputpath, type="output")).pack(side="bottom", fill="both")

    bottom.pack(side="bottom", fill="both", expand=2, pady= 50, padx=50)
