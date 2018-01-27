# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 21:44:43 2018

@author: navya
"""
import itertools;
print(*[(len(list(c)), int(k)) for k, c in itertools.groupby(input())])
#for k,c in itertools.groupby(input()):
 #   print ((list(c)),int(k))
#dic={};
#for i in data:
#    dic[data.count(i)]=int(i);
#
#    
#print (dic.items());
#print (*[dic.items()])
#for g,k in itertools.groupby(dic,k):
 #   print(g,k)
#    groups.append(list(g)) 
#    uniquekeys.append(k) 
#print (list(groups))
#print (uniquekeys)
#    # Store group iterator as a list
##    uniquekeys.append(k)