# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 12:22:49 2019

@author: Swathi
"""
import math
def partition(items,left,right):
    print("The current items are ",items)
    pivot=items[math.floor((left+right)/2)]
    l=left
    r=right
    print("--pivot is ",pivot)
    print("--left element is and it's index is ",items[left],l)
    print("--right element is and it's index is  ",items[right],r)
    #print("--left pointer is ",l)
    #print("--right pointer is ",r)
    while(l<=r):
        while(items[l]<pivot):
            l+=1
            print("l is now pointing to: ",items[l])

        while(items[r]>pivot):
            r-=1
            print("r is now pointing to: ",items[r])
        if(l<=r):
            print("swaping the left and right elements: ",items[l],items[r])
            swap(items,l,r)
            l+=1
            r-=1
    return l
def quicksort(items,leftindex,rightindex):
    if(len(items)>1):
        pivotindex=partition(items,leftindex,rightindex)
        print("The pivot is",pivotindex)
        print("The one that have been found now to be pivot",items[pivotindex])
        if(leftindex<pivotindex-1):
            print("The pivot to the right-left sort is",pivotindex)
            quicksort(items,leftindex,pivotindex-1)
        print("The pivot to the right-middle sort is",pivotindex)#some stack magic happening here!!!
        if(rightindex>pivotindex):
            print("The pivot to the right sort is",pivotindex)
            print("The right index is",rightindex)
            quicksort(items,pivotindex-1,rightindex)
    return items
def swap(items,leftpointer,rightpointer):
    tempreference=items[leftpointer]
    items[leftpointer]=items[rightpointer]
    items[rightpointer]=tempreference
items=[19, 22, 63, 105, 2, 46]
print(quicksort(items, 0,len(items) - 1))
    
    
        