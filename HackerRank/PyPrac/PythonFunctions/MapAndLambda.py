# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 12:34:49 2018

@author: navya
"""
N=int(input());
fibSer=[]
for i in range(N):
    if (i==0):
        fibSer.append(0);
    elif (i==1):
        fibSer.append(1);
    else:
        fibSer.append(fibSer[i-2]+fibSer[i-1]);
    
print(list(map(lambda z: z**3,fibSer)))
