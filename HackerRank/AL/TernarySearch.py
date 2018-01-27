# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 13:44:45 2018

@author: navya
"""

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def func(x):
    return (2*x**2-12*x+7)

def mino(start,end):
    l = start
    r = end

    for i in range(200):
        l1 = (l*2+r)/3
        r1 = (l+2*r)/3

    if func(l1) < func(r1):
        r = r1
    else:
        l = l1


    return func(l)

num = int(input())

for i in range(num):
    rng = input().split(' ')
    x = (mino(int(rng[0]),int(rng[1])))

print(round(x))
