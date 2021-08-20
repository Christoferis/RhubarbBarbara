#non Utillity stuff that is meant to make the app more Userfriendly (GUI Prompts, Credits etc.)

import tkinter as tk
from tkinter import messagebox as mb


#Vars for Headers and Stuff
TITLE = "RhubarbBarbara by Christoferis (v2.0)"

#Standard Error Message

def error(e):
    mb.showwarning(message="A problem occured, check Error message for details, and if issue persists, make an Github Issue \n(https://github.com/christoferis/RhubarbBarbara) \n\n" + str(e))
    exit()


#GUI For Credit thing
def about():
    abt = tk.Toplevel()

    #Creator, and Thanks
    tk.Label(abt, text='''
    RhubarbBarbara, an application by Christoferis\n
    written in Python 3.9.6, Version 2.0\n
    This App uses parts from Rhubarb Lip Sync by Daniel S. Wolf(https://github.com/DanielSWolf/rhubarb-lip-sync) and MoviePy by Zulko(https://github.com/Zulko/moviepy) \n 
    This App is maintained by Christoferis but feel free to help out!\n\n

    Repo: https://github.com/Christoferis/RhubarbBarbara

    Submit an Issue on Github if a problem persists or view the website (https://sites.google.com/view/christoferis/code-projects/rhubarbbarbara) for Troubleshooting measures.

    '''
    ).pack()
