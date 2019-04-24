# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:58:45 2019

@author: brian.stroh
"""

import shelve
db = shelve.open('people-shelve')
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
db.close()