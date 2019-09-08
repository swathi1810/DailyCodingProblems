# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:51:30 2019

@author: Swathi
"""

class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 
print("Preorder traversal of binary tree is")
preorder(root) 
  
print("\nInorder traversal of binary tree is")
inorder(root) 
  
print("\nPostorder traversal of binary tree is")
postorder(root)
        
    