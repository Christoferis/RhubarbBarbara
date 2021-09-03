#Main GUI Module

#imports
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

from PIL import Image, ImageTk

import etc, globals, util, rendering

#class for the mouth selector thingy
#TODO: Rewrite selector widget into seperate functions -> add to dict + remove static, remove this class / split (counteract the offset bug)
class selector_widget:

    def __init__(self, window, mouthshape):
        self.window = window
        self.logo = mouthshape
        self.button = None
        self.ext = False

        self.image = "icons/lisa-" + mouthshape + ".png"

        #mouthshape selector:
        if mouthshape in ("G","H","X"):
            self.ext = True
        pass

    def create_wid(self):
        shape = tk.Frame(self.window)
        
        #mouthshape îdentifier
        prevstr = self.logo

        if self.ext == True:
            prevstr += "\n " + "(Optional)"

        tk.Label(shape, text=prevstr).grid(column=1, row=1, padx=15)

        #Mouthshape preview (https://github.com/DanielSWolf/rhubarb-lip-sync#readme)
    
        img = ImageTk.PhotoImage(Image.open(self.image).resize((75, 62)))
        imgframe = tk.Label(shape, image=img)
        imgframe.image = img
        imgframe.grid(column=2, row=1)

        #button to remove image
        rembutton = tk.Button(shape, text="X", command=self.remove_from_dict)
        rembutton.grid(column=4, row=1)

        #button to open filedialog
        self.button = tk.Button(shape, text="Add an Image", command=self.add_to_dict)
        self.button.grid(column=3, row=1)

        
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
            globals.IMAGES[self.logo] = shape

            #set button color
            self.button.config(background="blue", foreground="white")
        else:
            print(shape)


#Gui class to keep everything sorted

#Resolution Radio Button, Background Transparent Radio Button (Overrides chosen Background)
class gui:
    window = None

    @staticmethod
    def gui(window):
        #Main GUI Function
        gui.window = window

        gui.mouth_select().pack()


    @staticmethod
    def mouth_select():
        main = tk.Frame(gui.window)

        faces = tk.Frame(main)

        #Spawn the Widgets
        grid_y = 1
        for shape in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'X'):
            frame = selector_widget(window=main, mouthshape=shape)
            frame.create_wid().grid(column=1, row=grid_y)
            grid_y += 1

        return main

    
# def gui(window):

#     #about page
#     tk.Button(window, text="Credits + Help", command=etc.about).pack(side="top")

#     #make main Frame for the images
#     top = tk.Frame(window)

#     for shape in ("X","H","G","F","E","D","C","B","A"):
#         frame = mouthSelector(window=top, mouthshape=shape)
#         frame.create_wid().pack(side="bottom")

#     top.pack(expand=2, pady=10, fill="both")

#     #Frame for the start Button and Audio Input
#     bottom = tk.Frame(window)
    
#     #audio Entry box + Stringvar
#     audiopath = tk.StringVar()
#     audiopath.set("Path to Audio")

#     audio = tk.Entry(bottom, state="readonly", textvariable=audiopath)
#     audio.pack(side="left", expand=1, fill="x")

#     #outputpath
#     outputpath = tk.StringVar()
#     outputpath.set(globals.SAVE)

#     output = tk.Entry(bottom, state="readonly", textvariable=outputpath)
#     output.pack(side="left", expand=1, fill="x")

#     #start button
#     tk.Button(bottom, text="start", background="green", foreground="white", command=rendering.start).pack(side="right", fill="both")
    
#     #search file buttons
#     #Audio File Button
#     tk.Button(bottom, text="Open Audio File", command=lambda: util.get_path(audiopath, type="audio")).pack(side="right", fill="both")

#     #Output Button
#     tk.Button(bottom, text="Set Output", command=lambda: util.get_path(outputpath, type="output")).pack(side="bottom", fill="both")

#     bottom.pack(side="bottom", fill="both", expand=2, pady= 50, padx=50)


if __name__ == "__main__":
    window = tk.Tk()

    gui.gui(window=window)

    window.mainloop()
    
