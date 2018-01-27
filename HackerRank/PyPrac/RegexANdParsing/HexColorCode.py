# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 14:43:02 2018

@author: navya
"""
import re, sys
[print(j) for i in sys.stdin for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', i, re.I)]
    