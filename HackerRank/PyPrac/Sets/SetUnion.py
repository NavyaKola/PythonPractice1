# -*- coding: utf-8 -*-
n=int(input());
nums1=set(input().split());
b=int(input());
nums2=set(input().split());
setC=nums1.union(nums2);
print (len(setC));

