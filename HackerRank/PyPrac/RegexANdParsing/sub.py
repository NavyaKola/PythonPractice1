# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 14:07:06 2018

@author: navya
"""

for _ in range(int(input())):
    line = input()
    
    while ' && ' in line or ' || ' in line:
        line = line.replace(" && ", " and ").replace(" || ", " or ")
    
    print(line)