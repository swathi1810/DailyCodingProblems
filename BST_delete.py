# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:30:19 2019

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
    def getinorder(node):
        current=node
        while(current.left is not None):
            current=current.left
        return current
    def deleteNode(root,key):
        if root is None:
            return root
        if key < root.key:
            root.left=deleteNode(root.left,key)
        elif key> root.key:
            root.rigt=deleteNode(root.right,key)
        else:
             if root.left is None : 
                 temp = root.right  
                 root = None 
                 return temp  
              
             elif root.right is None : 
                 temp = root.left  
                 root = None
                 return temp 
  
        # Node with two children: Get the inorder successor 
        # (smallest in the right subtree) 
        temp = minValueNode(root.right) 
  
        # Copy the inorder successor's content to this node 
        root.key = temp.key 
  
        # Delete the inorder successor 
        root.right = deleteNode(root.right , temp.key) 
  
  
    return root  
  
# Driver program to test above functions 
""" Let us create following BST 
              50 
           /     \ 
          30      70 
         /  \    /  \ 
       20   40  60   80 """
  
root = Node(50) 
root.insert(30) 
root.insert(20) 
root.insert(40) 
root.insert(70) 
root.insert(60) 
root.insert(80) 
  
print ("Inorder traversal of the given tree")
root.getinorder() 
  
print ("\nDelete 20")
root = root.deleteNode(root, 20) 
print ("Inorder traversal of the modified tree")
root.getinorder() 
  
print ("\nDelete 30")
root = root.deleteNode(root, 30) 
print ("Inorder traversal of the modified tree")
root.getinorderr() 
  
print ("\nDelete 50")
root = root.deleteNode(root, 50) 
print ("Inorder traversal of the modified tree")
root.etinorder() 