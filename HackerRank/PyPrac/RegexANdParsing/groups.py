# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 22:49:49 2018

@author: navya
"""

import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)