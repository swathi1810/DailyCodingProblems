# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:37:44 2019
Complexity:O(n2)
Question:Airbnb
@author: Swathi
"""

import collections
def groupAnagramWords(strs):
    out=[]
    inter=[]
    ind=[]
    for v in range(len(strs)):
        if (v not in ind):
            ind.append(v)
            inter.append(strs[v])
        for w in range(v,len(strs)):
            if(w not in ind):
                
                sort_first=sorted(strs[v])
                sort_second=sorted(strs[w])
                if(sort_first==sort_second):
                    inter.append(strs[w])
                    ind.append(w)
        if(len(inter)!=0):
            out.append(inter)
            inter=[]
    return(out)
print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))


            
            
        