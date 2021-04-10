#RhubarbBarbara is a Python tool for using Rhubarb Lip Sync in Production, without the need of Software like AE, OpenToonz etc.
#by creating videos out of the data provided
#by Christoferis CC BY 4.0 (https://www.sites.google.com/view/christoferis)
#trying to use a minimal amount of non stock dependencies

import json
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox
from subprocess import Popen, PIPE
from tkinter.constants import BOTH, BOTTOM, END, LEFT, NO, RIGHT, TOP, X, Y

import moviepy as mov
from PIL import Image, ImageTk

#Todo: 
# - Rhubarb Integration
# - Better UI
# - Configfile
# - freeze
# - Moviepy image to video backend
# - Loading bar 
# - Add tempfile

#vars
output = str()
audiopath = str("D:/Users/sdw.wav")
savepath = str() 


#ⒶⒷⒸⒹⒺⒻ extended shapes(ⒼⒽⓍ)

#Rhubarb integration


def rhubarb():
    global audiopath

    rhu = json.loads(open("config.json", mode="r").read())["rhubarb"]

    #open a cmd instance of Rhubarb
    cmd = Popen([rhu, "-f", "json", audiopath], stdout=PIPE)
    
    result = cmd.communicate()

    return json.loads(result[0])["mouthCues"]


#GUI
#class for mouthselector thingy
class mouthSelector:
    mouthshapes = dict()

    def __init__(self, window, mouthshape):
        self.window = window
        self.logo = mouthshape + "\n "
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

        tk.Label(shape, text=prevstr).pack(side=LEFT)

        #Mouthshape preview (https://github.com/DanielSWolf/rhubarb-lip-sync#readme)
        img = ImageTk.PhotoImage(Image.open(self.image).resize((75, 62)))
        imgframe = tk.Label(shape, image=img)
        imgframe.image = img
        imgframe.pack(side=LEFT)

        #button to open filedialog
        self.button = tk.Button(shape, text="add a image", command=self.add_to_dict)
        self.button.pack(side=RIGHT, fill=BOTH)
        
        return shape

    def add_to_dict(self):
        #add in only png images / jpg 
        shape = fd.askopenfilename()
        
        
        if shape != "":
            #open and append to dict
            mouthSelector.mouthshapes[self.logo] = shape

            #set button color
            self.button.config(background="blue", foreground="white")
        else:
            print("nothing")

#startmethod + checker
def start():
    #flag int for keeping missing things at minimum
    global audiopath
    global output

    flag = int(0)

    #check images (for the important ones)

    for shape in ("A","B","C","D","E","F"):
        if shape not in mouthSelector.mouthshapes:
            flag += 1
            break

    #check audiopath +

    #endcheck  
    if flag > 0:
        #show error screen
        messagebox.showinfo(title="You forgot something!",
        message=
        '''
        You can't start yet!
        Parts are incomplete, please correct them and try again
        if this Problem persists please open an issue on GitHub"
        ''')
    else:
        #start rhubarb class, then 
        pass
        


#Filegrabber for arbitrary files
def get_path(widget, type):
    global audiopath
    global output

    #reset display widget and add in path info
    #audio for audio path, output for output path
    if type == "audio":
        path = fd.askopenfilename()

        if path != '':
            widget.delete(0, END)
            widget.insert(0, path)
            audiopath = path
        else:
            pass

    elif type == "output":
        path = fd.asksaveasfilename()

        if path != '':
            widget.delete(0, END)
            widget.insert(0, path)
            output = path
        else:
            pass


def gui(window):
    #make main Frame for the images
    top = tk.Frame(window)

    for shape in ("X","H","G","F","E","D","C","B","A"):
        frame = mouthSelector(window=top, mouthshape=shape)
        frame.create_wid().pack(side=BOTTOM)

    top.pack(expand=2, pady=10, fill=BOTH)

    #Frame for the start Button and Audio Input
    bottom = tk.Frame(window)
    
    audiopath = tk.Entry(bottom)
    audiopath.pack(side=LEFT, expand=1, fill=X)
    audiopath.insert(END, "Path to audio")

    #outputpath
    output = tk.Entry(bottom)
    output.pack(side=LEFT, expand=1, fill=X)
    output.insert(END, "Outputpath")

    #start button
    tk.Button(bottom, text="start", background="green", foreground="white", command=start).pack(side=RIGHT, fill=BOTH)
    
    #search file button
    tk.Button(bottom, text="Open Audio File", command=lambda: get_path(audiopath, type="audio")).pack(side=RIGHT, fill=BOTH)

    bottom.pack(side=BOTTOM, fill=BOTH, expand=2, pady= 50, padx=50)



def main():


    #construct main window and call GUI
    '''
    window = tk.Tk()
    
    gui(window=window)


    window.mainloop()
    '''
    pass

main()
