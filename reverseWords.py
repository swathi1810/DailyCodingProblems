# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 10:29:41 2019
Complexity :O(n)
Question:Facebook
@author: Swathi
"""

def reverseWords(striy):
    list_words=list(striy.split(" "))
    striy_out=""
    for var in list_words:
        var_rev=var[::-1]
        striy_out=striy_out+var_rev+" "
    return(striy_out)
print(reverseWords("The cat in the hat"))