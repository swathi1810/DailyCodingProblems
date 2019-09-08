# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 09:26:12 2019

Complexity: O(n)
Question : Facebook
@author: Swathi
"""

def findRanges(a):
    j=0
    out=[]
    for i in range(0,len(a)):
        if(i==len(a)-1):
            stri=str(a[i-j])+"->"+str(a[i])
            out.append(stri)
            break
        if(a[i+1]-a[i]==1 or a[i+1]-a[i]==0 ):
            j=j+1
            #continue
        else:
            stri=str(a[i-j])+"->"+str(a[i])
            out.append(stri)
            j=0
    return(out)
    
print (findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
            