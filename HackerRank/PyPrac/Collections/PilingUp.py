# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 23:10:28 2018

@author: navya
"""
from collections import deque
T=int(input());

#d=deque();
for t in range(T):
    input()
    lst = map(int, input().split())
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    print ("Yes" if i == l - 1 else "No")
    
    

