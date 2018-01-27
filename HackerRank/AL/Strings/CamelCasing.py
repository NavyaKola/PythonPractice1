# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 22:24:31 2018

@author: navya
"""

import re
#!/bin/python3

import sys

def camelcase(s):
    # Complete this function
    c=re.findall(r'[A-Z]',s)
    return (len(c)+1)

if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
