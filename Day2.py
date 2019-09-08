'''
Complexity O(n):
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
***without division***
'''
import math
def multiOfList(list1):
    mul=[]
    sum=0
    EPS=1e-4
    for i in list1:
        sum+=math.log10(i)
    for i in list1:
        mul.append(int((EPS+pow(10.00,sum-math.log10(i)))))
    print(mul)
multiOfList([1, 2, 3, 4, 5])
