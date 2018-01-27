# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 22:19:10 2018

@author: navya
"""

import numpy
l=[]
l1=[]
N,M=map(int,input().split())
for i in range(N):
    l.append(list(map(int,input().split())))


arr=numpy.array(l)
m=numpy.min(arr, axis = 1)
print(numpy.max(m))