# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:53:21 2019

@author: brian.stroh
"""

from SecondScript import bob, sue
import shelve
db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close