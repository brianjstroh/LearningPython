# -*- coding: utf-8 -*-
"""
split and interactively page a string or file of text
this thing doesn't work and returns the same errors as the example
Created on Tue Apr 30 10:28:51 2019

@author: BRIAN.STROH
"""

def more(text, numlines = 15):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and input('More?') not in ['y', 'Y']: break
    
if __name__ =='__main__':
    #import sys
    #more(open(sys.argv[1]).read(), 10) <-This line does not work
    
    more("I\nLike\nTo\nEat\nEat\nEat\nApples\nAnd\nBananas\nAnd\nA\nWhole\nLot\nOf\nOther\nThings\nToo\n!!!\n\n\n\n\nEndTest", 10)