# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 19:35:28 2018

@author: navya
"""
T=int(input())
for i in range(T):
    
    try:
        a,b=map(int,input().split());
        print (a//b)
    except Exception as e:
        print ("Error Code:", e)




