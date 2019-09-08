# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 10:45:42 2019
Complexity:O(n)
Question:Google
@author: Swathi
"""

def roomSchedule(stru):
    room=1
    for v in range(len(stru)):
        if(v==len(stru)-1):
            break
        if(stru[v+1][0]<stru[v][1]):
            room=room+1
    return(room)
print(roomSchedule([(30, 75), (0, 50), (60, 150)]))
        