# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:16:45 2019

@author: brian.stroh
"""

import pickle
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])