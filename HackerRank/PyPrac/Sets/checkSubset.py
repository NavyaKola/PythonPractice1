# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:30:24 2018

@author: navya
"""

for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    print ((A.intersection(B))==A)
