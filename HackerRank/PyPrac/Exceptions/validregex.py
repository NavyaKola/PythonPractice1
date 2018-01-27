# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 19:36:02 2018

@author: navya
"""
import re;
for i in range(int(input())):
    S=input().strip();
    try:
        pattern=re.compile(S);
        print("True")
    except Exception as e:
        print("False")