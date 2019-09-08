# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:37:30 2019

@author: Swathi
"""
class HashTable:
    def __init__(self):
        self.size=11
        self.slots=[None]*self.size
        self.data=[None]*self.size
    def __getitem__(self,key):
        return (self.get(key))
    def __setitem__(self,key,data):
        return(self.put(key,data))
    def put(self,key,data):
        hashvalue=self.hashfunction(key,len(self.slots))
        if(self.slots[hashvalue]==None):
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        else:
            if(self.slots[hashvalue]==key):
                self.data[hashvalue]=data
            else:
                nextslot=self.rehash(hashvalue,len(self.slots))
                while(self.slots[nextslot]!=None and self.slots[nextslot]!=key):
                    nextslot=self.rehash(nextslot,len(self.slots))
                if(self.slots[nextslot]==None):
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot]=data
    def hashfunction(self,key,size):
        return key%size
    def rehash(self,olhash,size):
        return (olhash+1)%size
    def get(self,key):
        startslot=self.hashfunction(key,len(self.slots))
        data=None
        stop=False
        Found=False
        position=startslot
        while(self.slots[position]!=None and not Found and not stop):
            if(self.slots[position]==key):
                Found=True
                data=self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if (position==startslot):
                    stop=True
        return data

H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"

