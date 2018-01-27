# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 23:08:49 2018

@author: navya
"""

s = input()
print(s.isdigit() and 100000 <= int(s) <= 999999 and 
      sum([s[i] == s[i+2] for i in range(0, 4)]) < 2)