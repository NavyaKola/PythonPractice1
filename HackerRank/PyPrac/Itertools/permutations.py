# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 20:36:03 2018

@author: navya
"""
import itertools as it;
s=input().split();
l= list((it.permutations(sorted(s[0]),int(s[1]))));
for i in l:
    print (*[''.join(i)])