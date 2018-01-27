# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 12:55:52 2018

@author: navya
"""

S = input()
k = input()
import re
pattern = re.compile(k)
r = pattern.search(S)
if not r: print ("(-1, -1)")
while r:
    print ("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(S,r.start() + 1)