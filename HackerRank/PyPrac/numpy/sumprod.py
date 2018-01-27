# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:07:13 2018

@author: navya
"""
import numpy
l=[]
l1=[]
N,M=map(int,input().split())
for i in range(N):
    l.append(list(map(int,input().split())))


arr=numpy.array(l)
sum1=numpy.sum(arr, axis = 0) 
print( numpy.prod(sum1)   )