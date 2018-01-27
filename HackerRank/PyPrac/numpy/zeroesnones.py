# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 20:42:09 2018

@author: navya
"""
import numpy
l=tuple(map(int,input().split()))
#print (*l)
print (numpy.zeros(l,dtype=numpy.int))
print (numpy.ones(l,dtype=numpy.int))
