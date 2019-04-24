# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:19:37 2019

@author: brian.stroh
"""

import pickle
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()
db['sue']['pay'] *= 1.1
db['tom']['name'] = 'Tom Tom'

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
