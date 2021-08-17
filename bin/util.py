#Utillity functions used by Rhubarb Barbara

from bin import globals
from random import random

#Path Update Function
def update_paths():
    global CONFIG
    global SAVE

    #standard config
    if globals.CONFIG["standard-savepath"] != "":
        SAVE = globals.CONFIG["standard-savepath"] + "/" + str(round(random()*100000 + 1)) + ".avi"
    else:
        #TODO: Handle Outputpath
        SAVE = "Outputpath"


#get path function
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
        path = fd.asksaveasfilename(defaultextension=".avi", filetypes=
        [('MP4-Video(*.mp4)', '*.mp4'), ("AVI-Video(*.avi)", "*.avi"), ('Image Sequence(*.*)', '*.folder')]
        )

        if path != '':
            widget.set(path)
            globals.SAVE = path
        else:
            pass