# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:27:23 2019

@author: Swathi
"""

class Singleton:
    _instance1=None
    _instance2=None
    @staticmethod
    def getInstance(n):
        if(Singleton._instance1==None):
            print("something")
            Singleton()
        else:
            if(Singleton._instance2==None):
                print("something1")
                Singleton()
        if(n%2==0):
            return(Singleton._instance1)
        else:
            return(Singleton._instance2)
    def _init_(self):
        Singleton._instance1=self
        Singleton._instance2=self
s=Singleton()
print(s)    
for n in range(0,10):
    s=Singleton.getInstance(n)
    print(s)
    

            