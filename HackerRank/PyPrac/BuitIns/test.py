# -*- coding: utf-8 -*-

# =============================================================================
# import sys;
# l=[];
# s="insert(0,5)"
# eval("l."+ s);
# print (l);
# =============================================================================
l=[]
#y=[]
N,X=map(int,input().split())
for i in range(X):
    l.append(map(float,(input().split())))
for y in zip(*l):
    print((sum(y)/len(y) ));