# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:58:57 2019

@author: Swathi
complexity: O(n^2)
"""

def powerset(org):
    result=[[]]
    for x in org:
        newsubset=[subset +[x] for subset in result]
        print(newsubset)
        result.extend(newsubset)
    return result


def powerset2(org,newsubset):
    if org==[]:
        return [newsubset]
    else:
        res=[]
        for s in powerset2(org[1:],newsubset+[org[0]]):
            print(s)
            res.append(s)
        for s in powerset2(org[1:],newsubset):
            res.append(s)
    return res
ls=[1,2,3]
print(powerset(ls))
#print(powerset2(ls,[]))