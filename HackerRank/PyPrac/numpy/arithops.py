import numpy
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 20:55:01 2018

@author: navya
"""

import numpy
N,M=map(int,input().split())
l=[]
l1=[]
for i in range(N):
    l.append(list(map(int,input().split())))
A=numpy.array(l)
for i in range(N):
    l1.append(list(map(int,input().split())))
B=numpy.array(l1)
print(A+B,A-B,A*B, A//B,A%B,A**B,sep='\n')
