# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 17:17:58 2018

@author: navya
"""
t=int(input())
for x in range(t):
    N=int(input())
    l=[]
    A=list(map(int,input().split()))
    for i in range(1,N+1):
        for j in range(N):
            #if(i+j<=N):
            l.append(i*sum(A[j:j+i]))
print(max(l))
        