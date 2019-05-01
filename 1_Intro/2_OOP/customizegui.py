# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 07:38:57 2019

@author: brian.stroh
"""

from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter102 import MyGui

class CustomGui(MyGui):
    def reply(self):
        showinfo(title = 'popup', message = 'Ouch!')

if __name__ == '__main__':
    CustomGui().pack()
    mainloop()