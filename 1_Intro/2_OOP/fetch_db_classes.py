# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 19:15:38 2019

@author: brian
"""

import shelve
db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n ', db[key].name, db[key].pay)
    
bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())