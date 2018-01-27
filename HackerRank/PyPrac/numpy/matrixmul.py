# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 22:41:10 2018

@author: navya
"""

import numpy
N=int(input())
l=[]
l1=[]
for i in range(N):
    l.append(list(map(int,input().split())))
A=numpy.array(l)
for i in range(N):
    l1.append(list(map(int,input().split())))
B=numpy.array(l1)
print(numpy.dot(A,B))