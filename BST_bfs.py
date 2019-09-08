# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 23:37:03 2019

@author: Swathi
complexity:O(n)
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def levelOrderTraversal(root):
    if root is None:
        return
    queue=[]
    queue.append(root)
    while(len(queue)>0):
        print(queue[0].data)
        node=queue.pop(0)
        if(node.left is not None):
            queue.append(node.left)
            
        if(node.right is not None):
            queue.append(node.right)
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
print("Level Order Traversal of binary tree is -")
levelOrderTraversal(root)
            
        