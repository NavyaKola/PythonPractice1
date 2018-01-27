# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 20:18:48 2018

@author: navya
"""
from collections import deque
d = deque()
N=int(input());
for i in range(N):
    s= input().split()
    if (len(s)>1):
        op=s[0]
        val=s[1]
    else:
        op=s[0]
    if(op!='pop' and op!='popleft'):
        z="d." +op+"("+val+")"
    else:
        z="d." +op+"("+")"   
    eval(z)
print (*d)
        
        
        