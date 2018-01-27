# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 14:06:37 2018

@author: navya
"""

import re

thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'
print (bool(re.match(thousand + hundred+ten+digit +'$', input())))