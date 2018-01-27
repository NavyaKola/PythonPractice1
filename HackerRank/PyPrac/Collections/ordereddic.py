# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 18:36:50 2018

@author: navya
"""

N=int(input());
from collections import OrderedDict;
itemnames=OrderedDict();
for i in range(N):
    item, space, quantity = input().rpartition(' ')
    itemnames[item] = itemnames.get(item, 0) + int(quantity)
for item, quantity in itemnames.items():
    print(item, quantity)
    
    