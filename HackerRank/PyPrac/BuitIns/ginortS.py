# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:33:08 2018

@author: navya
"""

order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index),order.index, sep='')