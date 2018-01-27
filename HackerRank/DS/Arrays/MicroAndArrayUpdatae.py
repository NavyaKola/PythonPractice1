# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 00:16:45 2018

@author: navya
"""

T=int(input())

for i in range(T):
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    if (any(x<K for x in A )):
        print (K-min(A))
    else:
        print(0)