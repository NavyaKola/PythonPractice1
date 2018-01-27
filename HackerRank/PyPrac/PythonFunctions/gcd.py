# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:14:12 2018

@author: navya
"""

n=int(input())
nume=[],deno=[]
from functools import reduce
for i in range(n):
    Ni,Di=map(int,input().split())
    nume.append(Ni)
    deno.append(Di)
    a=reduce(lambda x,y:x*y,nume)
    b=reduce(lambda x,y:x*y,deno)
    