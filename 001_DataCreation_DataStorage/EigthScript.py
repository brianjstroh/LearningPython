# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:32:53 2019

@author: brian.stroh
"""

import pickle, glob
for filename in glob.glob('*.pkl'):
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n ', record)
suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])