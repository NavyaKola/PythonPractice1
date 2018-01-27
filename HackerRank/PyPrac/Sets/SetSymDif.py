# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 11:18:38 2018

@author: navya
"""

# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 11:15:05 2018

@author: navya
"""

n=int(input());
nums1=set(input().split());
b=int(input());
nums2=set(input().split());
setC=nums1.symmetric_difference(nums2);
print (len(setC));

