# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 12:42:57 2019

@author: brian.stroh
"""

from SecondScript import db
import pickle
dbfile = open('people-pickle', 'wb') #write binary
pickle.dump(db,dbfile)
dbfile.close()