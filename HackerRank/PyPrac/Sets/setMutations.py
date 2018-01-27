# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 11:22:25 2018

@author: navya
"""

noOfEleInSetA=int(input());
setA=set(input().split());
sumA=0;
N=int(input());
for i in range(N):
    temp1=input().split();
    setB=set(input().split());
    #op="("+ temp1[0]+")"
    eval("setA."+temp1[0]+"("+"setB"+")");
for x in setA:
    sumA=sumA+int(x);
print(sumA);
        
    
