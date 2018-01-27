# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:07:33 2018

@author: navya
"""

import numpy
A=numpy.array(list(map(float,input().split())))
print(numpy.floor(A),numpy.ceil(A),numpy.rint(A),sep='\n')