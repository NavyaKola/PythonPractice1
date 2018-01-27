# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 21:13:02 2018

@author: navya
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 20:50:13 2018

@author: navya
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 20:36:03 2018

@author: navya
"""
import itertools as it;
s=input().split();
l=[];
l= list((it.combinations_with_replacement(sorted(s[0]),int(s[1]))));
for i in l:
    print (*[''.join(i)])