#installer for Rhubarb Barbara by Christoferis CC BY 4.0
# https://github.com/christoferis/rhubarbbarbara

import json
from os import system, path as pt



welcome = '''
Welcome to the Installer / Configurator of RhubarbBarbara written by Christoferis!
This Wizard will guide you through configurating and installing all the needs of RhubarbBarbara.
'''
config = None


def get_rhubarb():
    global config
    
    path = input("Please provide the path to Rhubarb Barbara \n (ex.: D:/Music/rhubarb-lip-sync-1.10.0-win32/rhubarb-lip-sync-1.10.0-win32 or D:/Music/rhubarb-lip-sync-1.10.0-win32/rhubarb-lip-sync-1.10.0-win32/rhubarb.exe): ")


    #check for .exe
    if path.find(".exe") <= 0:
        path + "rhubarb.exe"
    
    #test if file exists
    try:
        open(path, mode="r")
    except FileNotFoundError:
        print("Invalid Path or File not Found")
        return get_rhubarb()
    #make path to rhubarb path in the config
    else:
        config["rhubarb"] = path
        pass


#get the standard path if desired
def standard_path():
    global config
    path = input("Do you want to set a standard output path? Type NONE to skip: ")

    if path in ("NONE", "none"):
        config["standard-savepath"] = ""
    else:
        if pt.isdir(path) == True:
            config["standard-savepath"] = path

        #return the function if check fails
        else:
            print("Invalid Path or Path doesn't exist")
            return standard_path()

    
#install the packages + write config
def finalize():
    global config

    #write everything
    with open("config.json", mode="w") as cfg:
        cfg.write(json.dumps(config))

    #confirm
    choice = input("Do you want to proceed installing the packages? [y / n]: ")

    if choice in ("Y", "y"):
        system("")




def main():
    global welcome
    global config

    #open config
    with open("config", mode="r") as cfg:
        config = json.loads(cfg.read())

    print(welcome)
