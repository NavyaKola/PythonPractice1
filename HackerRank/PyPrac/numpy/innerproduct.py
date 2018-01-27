# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 22:46:18 2018

@author: navya
"""

import numpy

A, B = [numpy.array(input().split(), int) for _ in range(2)]
print ('\n'.join(str(op(A, B)) for op in (numpy.inner, numpy.outer)))