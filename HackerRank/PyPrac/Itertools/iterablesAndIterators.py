# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 23:57:52 2018

@author: navya
"""
import itertools;
N=int(input());
s=input().split();
K=int(input());
sum1=0;
l=list(itertools.combinations(s,K));
for i in l:
    if ('a' in i):
        sum1=sum1+1;
print(sum1/len(l));
        
        
        
    