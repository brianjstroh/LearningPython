# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 07:32:05 2019

@author: brian.stroh
"""

from tkinter import *
from tkinter102 import MyGui

# main app window
mainwin = Tk()
Label(mainwin, text=__name__).pack()

#popup window
popup = Toplevel()
Label(popup, text = 'Attach').pack(side = LEFT)
MyGui(popup).pack(side = RIGHT)
mainwin.mainloop()