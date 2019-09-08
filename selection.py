# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:02:47 2019

@author: Swathi
selection sort with complexity O(n2)
"""

def selection_Sort(lst):
    min1 =lst[0]
    for i in range(0,len(lst)):
        min1=lst[i]
        for j in range(i+1,len(lst)):
            if(min1>lst[j]):
                min1=lst[j]
        if(lst.index(min1)!=i):
            indi=lst.index(min1)
            temp=min1
            lst[indi]=lst[i]
            lst[i]=temp
    return lst
        
