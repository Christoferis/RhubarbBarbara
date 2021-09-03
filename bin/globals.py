#global Preferences (paths, Settings etc.)

#imports
import json

#Standard FPS is 30
FPS = int

#Resolution: 0: w, 1: h
RES = list

#Paths
SAVE = str

AUDIO = str

CONFIG = json.loads(open("config.json", mode="r").read())

#internal 
#mouthshape paths, Background
IMAGES = dict()

RENDER_SETTINGS = {"FPS": 30, "Resolution": None}



