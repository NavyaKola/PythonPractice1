# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 21:28:15 2018

@author: navya
"""

import numpy
N,M=map(int,input().split())
l=[]
for i in range(N):
    l.append(list(map(int,input().split())))
myarr=numpy.array(l)
print (myarr)
#myarr=myarr.reshape(N,M)
print(numpy.transpose(myarr))             
print(myarr.flatten())
    
