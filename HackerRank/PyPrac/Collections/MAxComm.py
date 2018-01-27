# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 23:54:17 2018

@author: navya
"""
from collections import Counter
s=dict(Counter(input()))
s1={}
l=list(s.values());
l=(sorted(l,key=int,reverse=True))
l1=[];
l2=list(s.keys());
l2=(sorted(l2,key=str,reverse=False))


for k,v in s.items():
    t=list(s1.keys())
    if v not in t:
        s1[v]=[k];
    else:
        s1[v].append(k);

for i in range(3):
        if(l[i]!=l[i-1]):
            z=sorted(s1[l[i]])
            for j in range(len(z)):
                l1.append(z[j])
                if(len(l1)<4):
                    print (z[j],s[z[j]])
        elif(max(l)==min(l)):
            print(l2[i],l[i])
