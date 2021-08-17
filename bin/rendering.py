#All code related to Rendering or Backend

#Imports
from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips
from PIL import Image, ImageTk
import json
import tkinter as tk 
from os import mkdir
from subprocess import Popen, PIPE


#startmethod + checker
def start():
    #flag int for keeping missing things at minimum

    flag = int(0)
    
    #check images (for the important ones)
    for shape in ("A","B","C","D","E","F"):
        if shape not in globals.MOUTHSHAPES:
            flag += 1
            break

    #check audiopath + globals.SAVE
    if globals.SAVE  == "":
        flag += 1
    
    if globals.AUDIO == "":
        flag += 1 

    #endcheck  
    print(flag)
    if flag > 0:
        #show error screen
        tk.messagebox.showinfo(title="You forgot something!",
        message=
        '''
        You can't start yet!
        Parts are incomplete, please correct them and try again
        if this Problem persists please open an issue on GitHub"
        ''' + " " + str(flag))
    else:
        process()
        pass


def video_Image(data):
    #function version of prior videoImage Class (Problems with class instances)
    return ImageClip(img=globals.MOUTHSHAPES[data["value"]], transparent=True, duration=float(data["end"]) - float(data["start"]))

#Rhubarb Integration
def rhubarb():
    global audiopath
    global config

    #get rhubarb path
    rhu = globals.CONFIG["rhubarb"]

    #check for extended shapes
    extshapes = ""
    for shape in globals.MOUTHSHAPES:
        #g
        if shape == "G":
            extshapes += "G"
        #h
        elif shape == "H":
            extshapes += "H"
        #x
        elif shape == "X":
            extshapes += "X"
        else:
            pass
    
    print(extshapes)

    #open a cmd instance of Rhubarb
    cmd = Popen([rhu, "-f", "json", "--extendedShapes", extshapes, globals.AUDIO], stdout=PIPE)
    
    result = cmd.communicate()

    return json.loads(result[0])["mouthCues"]

#Processes Videoclips and Renders it
def process():


    #find the codec
    mouthData = rhubarb()

    if globals.SAVE.find(".mp4") >= 0:
        codec = "libx264"
        video = True

    elif globals.SAVE.find(".avi") >= 0:
        codec = "png"
        video = True

    #add in image sequence format and convert to path + img identifier using the foldername
    elif globals.SAVE.find(".folder"):
        #make directory
        globals.SAVE = globals.SAVE.replace(".folder", "")
        mkdir(globals.SAVE)
        #make identifier + complete output path
        ident = globals.SAVE.split("/")
        #complete output
        globals.SAVE = globals.SAVE + "\\" + ident[len(ident) - 1] + "%06d.png"

        video = False


    imageclips = list()

    for data in mouthData:
        imageclips.append(video_Image(data))
    
    #concatenate all 
    final = concatenate_videoclips(imageclips, method="compose")
    

    #Render out, if video True = Render video and add audio, else render imagesequence
    if video == True:
        final = final.set_audio(AudioFileClip(globals.AUDIO))
        final.write_videofile(globals.SAVE, codec=codec, fps=60)
        
    elif video == False:
        final.write_images_sequence(fps=60, withmask=True, nameformat=globals.SAVE)
