# -*- coding: utf-8 -*-
n=int(input())
num=input().split()
num=[int(x) for x in num]
numSet=set(num)
N=int(input())
sum1=0;
for i in range(N):
    s=input().split();
    op=s[0];
    if(len(s)>1):
        arg=s[1]
        z=op+"("+ arg + ")";
        eval("numSet."+z);
    else:
        z=op+"("+")";
        eval("numSet."+z);
for i in numSet:
    sum1=sum1+int(i);
print (sum1) 

