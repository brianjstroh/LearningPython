# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:23:15 2019

@author: brian.stroh
"""

from SecondScript import bob, sue, tom
import pickle
for(key, record) in [('bob', bob), ('sue',sue),('tom', tom)]:
        recfile = open(key +'.pkl', 'wb')
        pickle.dump(record,recfile)
        recfile.close()
suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])