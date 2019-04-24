# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:37:29 2019

@author: brian.stroh
"""

import pickle
suefile = open('sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close()

sue['pay'] *= 1.10
suefile = open('sue.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close