# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 22:22:58 2018

@author: navya
"""

import numpy
l=[]
l1=[]
N,M=map(int,input().split())
for i in range(N):
    l.append(list(map(int,input().split())))


arr=numpy.array(l)
print(numpy.mean(arr,axis=1))
print(numpy.var(arr,axis=0))
print(numpy.std(arr))