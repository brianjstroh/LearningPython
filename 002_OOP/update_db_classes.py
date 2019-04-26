# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 19:29:45 2019

@author: brian
"""

import shelve
db = shelve.open('class-shelve')

sue = db['sue']
sue.giveRaise(.25)
db['sue'] = sue

tom = db['tom']
tom.giveRaise(.2)
db['tom'] = tom
db.close()