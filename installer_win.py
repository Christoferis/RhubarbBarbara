#installer for Rhubarb Barbara by Christoferis CC BY 4.0
# https://github.com/christoferis/rhubarbbarbara

import json
from os import system, path as pt
import pip
from time import sleep



welcome = '''
Welcome to the Installer / Configurator of RhubarbBarbara written by Christoferis!
This Wizard will guide you through configurating and installing all the needs of RhubarbBarbara.
'''
config = None


def get_rhubarb():
    global config
    
    path = input("Please provide the path to Rhubarb Barbara \n (ex.: D:/Music/rhubarb-lip-sync-1.10.0-win32/rhubarb-lip-sync-1.10.0-win32 or D:/Music/rhubarb-lip-sync-1.10.0-win32/rhubarb-lip-sync-1.10.0-win32/rhubarb.exe): ")


    #check for .exe
    if path.find(".exe") <= -1:
        path += "rhubarb.exe"
    


    #test if file exists
    config["rhubarb"] = path


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
        pip.main(args=["install", "moviepy"])


def main():
    global welcome
    global config

    #open config
    with open("config.json", mode="r") as cfg:
        config = json.loads(cfg.read())

    print(welcome)
    get_rhubarb()
    standard_path()
    finalize()

    print("\n\nThanks for installing RhubarbBarbara! Usage Tutorial can be found here: https://sites.google.com/view/christoferis/code-projects/rhubarbbarbara")
    sleep(10)



try:
    main()
except Exception as e:
    print("An Error Occured while Installing, try running it again, if problem persists make an Github Issue \n(https://github.com/christoferis/RhubarbBarbara)\n\n" + str(e) + "\n\n This window closes in 10 Seconds automatically")
    sleep(10)