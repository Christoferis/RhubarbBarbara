#RhubarbBarbara is a Python tool for using Rhubarb Lip Sync in Production, without the need of Software like AE, OpenToonz etc.
#by creating videos out of the data provided
#by Christoferis CC BY 4.0 (https://www.sites.google.com/view/christoferis)
#trying to use a minimal amount of non stock dependencies

import json
import tkinter as tk
import tkinter.filedialog as fd
from random import random
from subprocess import PIPE, Popen
from tkinter import messagebox
from tkinter.constants import BOTH, BOTTOM, DISABLED, END, LEFT, RIGHT, X

from moviepy.editor import ImageClip, concatenate_videoclips
from PIL import Image, ImageTk

#Todo: 
# - Loading bar 
# - make threads parameter variable by computer
# - more Video options? (add MP4, PNG Sequence)
# - About Page, icon + info
# - Path Information display at image thing
# - Better UI
# - freeze

#vars
output = str()
audiopath = str()
savepath = str()
config = None


def videoImage(data):
    #function version of prior videoImage Class (Problems with class instances)    
    return ImageClip(img=mouthSelector.mouthshapes[data["value"]], transparent=True, duration=float(data["end"]) - float(data["start"]))

#Rhubarb integration
def rhubarb():
    global audiopath
    global config

    #get rhubarb path
    rhu = config["rhubarb"]

    #check for extended shapes
    extshapes = ""
    for shape in mouthSelector.mouthshapes:
        #g
        if shape.find("G"):
            extshapes += "G"
        #h
        elif shape.find("H"):
            extshapes += "H"
        #x
        elif shape.find("X"):
            extshapes += "X"
        else:
            pass

    #open a cmd instance of Rhubarb
    cmd = Popen([rhu, "-f", "json", "--extendedShapes", extshapes, audiopath], stdout=PIPE)
    
    result = cmd.communicate()

    return json.loads(result[0])["mouthCues"]

#class for mouthselector thingy
class mouthSelector:
    mouthshapes = dict()

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

        tk.Label(shape, text=prevstr).pack(side=LEFT)

        #Mouthshape preview (https://github.com/DanielSWolf/rhubarb-lip-sync#readme)
        img = ImageTk.PhotoImage(Image.open(self.image).resize((75, 62)))
        imgframe = tk.Label(shape, image=img)
        imgframe.image = img
        imgframe.pack(side=LEFT)


        #button to remove image
        rembutton = tk.Button(shape, text="X", command=self.remove_from_dict)
        rembutton.pack(side=RIGHT, fill=BOTH)

        #button to open filedialog
        self.button = tk.Button(shape, text="Add an Image", command=self.add_to_dict)
        self.button.pack(side=RIGHT, fill=BOTH)

        
        return shape

    def remove_from_dict(self):
        #reset button color
        self.button.config(background="#F0F0F0", foreground="black")

        #remove from dict
        try:
            del mouthSelector.mouthshapes[self.logo]
        except KeyError:
            pass

        pass

    def add_to_dict(self):
        #add in only png images / jpg 
        shape = fd.askopenfilename()
        
        
        if shape != "":
            #open and append to dict
            mouthSelector.mouthshapes[self.logo] = shape

            #set button color
            self.button.config(background="blue", foreground="white")
        else:
            print(shape)

def process():
    global output

    mouthData = rhubarb()

    imageclips = list()

    for data in mouthData:
        imageclips.append(videoImage(data))
    
    #concatenate all 
    final = concatenate_videoclips(imageclips, method="compose")

    #Render out
    print(output)
    final.write_videofile(output, codec="png", fps=60)

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

    #check audiopath + output
    if output == "":
        flag += 1
    
    if audiopath == "":
        flag += 1 

    #endcheck  
    print(flag)
    if flag > 0:
        #show error screen
        messagebox.showinfo(title="You forgot something!",
        message=
        '''
        You can't start yet!
        Parts are incomplete, please correct them and try again
        if this Problem persists please open an issue on GitHub"
        ''' + " " + str(flag))
    else:
        process()
        pass
        

#Filegrabber for arbitrary files
def get_path(widget, type):
    global audiopath
    global output

    #reset display widget and add in path info
    #audio for audio path, output for output path
    if type == "audio":
        path = fd.askopenfilename(defaultextension=".wav", filetypes=[('WAV-Audio(*.wav)', '*.wav')])

        if path != '':
            widget.set(path)
            audiopath = path
        else:
            pass

    elif type == "output":
        path = fd.asksaveasfilename(defaultextension=".avi", filetypes=[('MP4-Video(*.mp4)', '*.mp4'), ("AVI-Video(*.avi)", "*.avi")])

        if path != '':
            widget.set(path)
            output = path
        else:
            pass

#GUI
def gui(window, stdpath):
    #make main Frame for the images
    top = tk.Frame(window)

    for shape in ("X","H","G","F","E","D","C","B","A"):
        frame = mouthSelector(window=top, mouthshape=shape)
        frame.create_wid().pack(side=BOTTOM)

    top.pack(expand=2, pady=10, fill=BOTH)

    #Frame for the start Button and Audio Input
    bottom = tk.Frame(window)
    
    #audio Entry box + Stringvar
    audiopath = tk.StringVar()
    audiopath.set("Path to Audio")

    audio = tk.Entry(bottom, state=DISABLED, textvariable=audiopath)
    audio.pack(side=LEFT, expand=1, fill=X)

    #outputpath
    outputpath = tk.StringVar()
    outputpath.set(stdpath)

    output = tk.Entry(bottom, state=DISABLED, textvariable=outputpath)
    output.pack(side=LEFT, expand=1, fill=X)

    #start button
    tk.Button(bottom, text="start", background="green", foreground="white", command=start).pack(side=RIGHT, fill=BOTH)
    
    #search file buttons
    #Audio File Button
    tk.Button(bottom, text="Open Audio File", command=lambda: get_path(audiopath, type="audio")).pack(side=RIGHT, fill=BOTH)

    #Output Button
    tk.Button(bottom, text="Set Output", command=lambda: get_path(outputpath, type="output")).pack(side=BOTTOM, fill=BOTH)

    bottom.pack(side=BOTTOM, fill=BOTH, expand=2, pady= 50, padx=50)

#Main Function 
def main():
    #open config file and fetch and make random name
    global config
    global output
    config = json.loads(open("config.json", mode="r").read())
    
    #standard config
    if config["standard-savepath"] != "":
        standard = config["standard-savepath"] + "/" + str(round(random()*100000 + 1)) + ".avi"
        output = standard
    else:
        standard = "Outputpath"
    
    #construct main window and call GUI
    
    window = tk.Tk()
    window.title("RhubarbBarbara by Christoferis (v0.9)")
    
    gui(window=window, stdpath=standard)


    window.mainloop()
    
    pass

main()
