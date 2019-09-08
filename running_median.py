# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 11:36:24 2019
Complexity: O(n) -- more than that?
Question: Google
@author: Swathi
"""

def running_median(stream):
    list_new=[]
    out=[]
    i=1
    sum_=0
    for var in stream:
       list_new.append(var)
       list_new.sort()
       print(list_new)
       if(i%2==0):
           med=sum(list_new)/i
       else:
           med_ind=int(i/2)
           med=list_new[med_ind]
       out.append(med)
       i=i+1
    return(out)
print(running_median([2, 1, 4, 7, 2, 0, 5]))