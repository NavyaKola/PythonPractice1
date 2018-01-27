# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 20:28:53 2018

@author: navya
"""

import numpy

N,M,P=map(int,input().split())
l=[]
l1=[]
for i in range(N):
    l.append(list(map(int,input().split())))
array_1=numpy.array(l)
for i in range(M):
    l1.append(list(map(int,input().split())))
array_2=numpy.array(l1)

print (numpy.concatenate((array_1, array_2), axis = 0)   )

