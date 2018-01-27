# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 23:39:05 2018

@author: navya
"""

import sys

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 23:39:05 2018

@author: navya
"""



def super_reduced_string(s):
    # Complete this function
    i=0
    if len(s)==2:
        if s[i]==s[i+1]:
            return "Empty String"
    elif len(s)==1:
        return(s)
    else:           
        while(i<=len(s)-2):
            if s[i]==s[i+1]:
                s = s[:i] + s[i + 2:]
                i=0
            else:
                i+=1
        if (len(s)==0):
            s="Empty String"
    return s;
                
        

s = input().strip()
result = super_reduced_string(s)
print(result)