# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:51:14 2018

@author: navya
"""

N=int(input())
l=list(map(int,input().split()))
print(all(i >0 for i in l) and (any(str(i) == str(i)[::-1] for i in l)))