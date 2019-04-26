# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:55:27 2019

giveRaise here demonstrate's OOP's polymorphism and inheritance structure.

@author: brian
"""

from person import Person

class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')
    def giveRaise(self, percent, bonus = .1): #Manager inherits lastName from person, but giveRaise is customized for Managers.
        self.pay *= (1+ percent + bonus)
    #augmenting instead
#    def giveRaise(self, percent, bonus = .1):
#        Person.giveRaise(self, percent + bonus)    <-calls method from superclass as an augmentation to original method

if __name__ == '__main__':
    tom = Manager(name = 'Tom Doe', age = 50, pay = 50000)
    print(tom.lastName())
    tom.giveRaise(.2)
    print(tom.pay)
    print(tom)