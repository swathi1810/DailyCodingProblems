# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 19:08:42 2019

@author: Swathi
"""
import math
def mergesort(list_mer):
    len_arr=len(list_mer)
    global inv_count
    if(len_arr==1):
        return
    mid_pt=math.floor(len_arr/2)
    left_arr=list_mer[0:mid_pt]
    right_arr=list_mer[mid_pt:]
    mergesort(left_arr)
    mergesort(right_arr)
    inv_count+=merge(left_arr,right_arr,list_mer,mid_pt)
    print(inv_count)
    return list_mer
def merge(left_list,right_list,list_mer,mid_pt):
    index=0
    inv_count=0
    l=0
    print("The midpoint is",mid_pt)
    while(len(left_list) and len(right_list)):
        if(left_list[0]<right_list[0]):
            print("Checking which element is tested {} with {}".format(left_list[0],right_list[0]))
            list_mer[index]=left_list.pop(0)
            l+=1
            index+=1
            print("The left",list_mer)
        else:
            list_mer[index]=right_list.pop(0)
            index+=1
            print("The left is",l)
            inv_count+=(mid_pt-l)
            print("The inversion count",inv_count)
            print("The right",list_mer)
    while(len(left_list)):
        list_mer[index]=left_list.pop(0)
        index+=1
        print("The left full",list_mer)
    while(len(right_list)):
        list_mer[index]=right_list.pop(0)
        index+=1
        print("The right full",list_mer)
    return inv_count
list_mer=[5, 4, 3, 2, 1]
inv_count=0
mergesort(list_mer);
print(list_mer)
print(inv_count)

    
            
    