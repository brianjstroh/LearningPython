# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:02:39 2019

@author: brian.stroh
"""

from SecondScript import tom
import shelve
db = shelve.open('people-shelve')
sue = db['sue']
sue['pay'] *= 1.50
db['sue'] = sue
db['tom'] = tom
db.close()