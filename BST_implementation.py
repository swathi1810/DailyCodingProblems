# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 19:06:47 2019

@author: Swathi
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if(self.data):
            if(data<self.data):
                if(self.left is None):
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif(data>self.data):
                if(self.right is None):
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    def search(self,data):
        if(data<self.data):
            if(self.left is None):
                return("Not found")
            return(self.left.search(data))
                
        elif(data>self.data):
            if(self.right is None):
                return("Not found")
            return(self.right.search(data))#otherwise the value will be discarded
        else:
            return("found")
                
    def print_tree(self):
        if(self.left):
            self.left.print_tree()
        print(self.data)
        if(self.right):
            self.right.print_tree()
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.print_tree()
print(root.search(7))
print(root.search(14))
        
                
            
                