# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 20:50:13 2018

@author: navya
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 20:36:03 2018

@author: navya
"""
import itertools as it;
s=input().split();
l=[];
for i in range(1,int(s[1])+1):
    temp= list((it.combinations(sorted(s[0]),i)));
    l.extend(temp);
for i in l:
    print (*[''.join(i)])