'''Complexity O(n):
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.'''
def sumOfTwo(list1,k):
    f=False
    for i in range(0,len(list1)):
        if ((k-list1[i]) in list1):

            f=True
            break
    if(f==True):
        print("Found")
    else:
        print("Not found")



