#Main GUI Module
#move to qt

#imports
import PySide6.QtWidgets as qt
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from sys import argv

from PIL import Image, ImageTk

# from bin import etc, globals, util, rendering

#class for the mouth selector thingy
#TODO: Rewrite selector widget into seperate functions -> add to dict + remove static, remove this class / split (counteract the offset bug)
class selector_widget:
    faces = None
    labels = None
    buttons = None

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
        
        self.frame_init(window=window)

    @classmethod
    def frame_init(self, window):
        if selector_widget.faces == None:
            selector_widget.faces = tk.Frame(window)
        if selector_widget.labels == None:
            selector_widget.labels = tk.Frame(window)
        if selector_widget.buttons == None:
            selector_widget.buttons = tk.Frame(window)
        pass

    def create_wid(self):
        
        #mouthshape îdentifier
        prevstr = self.logo

        if self.ext == True:
            prevstr += "\n " + "(Optional)"

        tk.Label(selector_widget.labels, text=prevstr).grid(column=1, row=int(len(selector_widget.labels.children) + 1), padx=15)

        #Mouthshape preview (https://github.com/DanielSWolf/rhubarb-lip-sync#readme)
    
        img = ImageTk.PhotoImage(Image.open(self.image).resize((75, 62)))
        imgframe = tk.Label(selector_widget.faces, image=img)
        imgframe.image = img
        imgframe.grid(column=1, row=int(len(selector_widget.faces.children) + 1))
        print(imgframe.grid_info())


        #seperate Frame for buttons
        buttons = tk.Frame(selector_widget.buttons)
        #button to remove image
        rembutton = tk.Button(buttons, text="X", command=self.remove_from_dict)
        rembutton.grid(column=2, row=1)

        #button to open filedialog
        self.button = tk.Button(buttons, text="Add an Image", command=self.add_to_dict)
        self.button.grid(column=1, row=1)

        buttons.grid(column=1, row=len(selector_widget.buttons.children) + 1)

    def remove_from_dict(self):
        #reset button color
        self.button.config(background="#F0F0F0", foreground="black")

        #remove from dict
        try:
            del globals.IMAGES[self.logo]
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


#Widget for Seetings
class settings(qt.QWidget):

    def __init__(self):
        super().__init__()

        #test ui
        self.text = qt.QLabel("Hey")
        self.button = qt.QPushButton(text="hey")


        #add layout and add to it
        self.layout = qt.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)



#Gui class to keep everything sorted

#Resolution Radio Button, Background Transparent Radio Button (Overrides chosen Background)


if __name__ == "__main__":
    app = qt.QApplication(argv)

    gui = main_gui()

    gui.show()
    
    app.exec()
    
