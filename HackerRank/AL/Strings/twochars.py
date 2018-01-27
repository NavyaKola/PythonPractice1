# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:48:41 2018

@author: navya
"""
import collections
s='beabeefeab';
l=list(s)
for i in range(len(l)-1):
    if (l[i]==l[i-1]):
        l=list(filter(lambda a: a == l[i], l))
        i=0
print(l)