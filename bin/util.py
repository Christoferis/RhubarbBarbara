#Utillity functions used by Rhubarb Barbara

import bin.globals
from random import random
import tkinter.filedialog as fd

#util funcs

#mouthshape order
mouthshape_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'X']

#Path Update Function
def update_paths():

    #standard config
    if globals.CONFIG["standard-savepath"] != "":
        globals.SAVE = globals.CONFIG["standard-savepath"] + "/" + str(round(random()*100000 + 1)) + ".avi"
    else:
        #TODO: Handle Outputpath
        globals.SAVE = "Outputpath"


#get path function
def get_path(widget, type):

    #reset display widget and add in path info
    #audio for audio path, output for output path
    if type == "audio":
        path = fd.askopenfilename(defaultextension=".wav", filetypes=[('WAV-Audio(*.wav)', '*.wav')])

        if path != '':
            widget.set(path)
            globals.AUDIO = path
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