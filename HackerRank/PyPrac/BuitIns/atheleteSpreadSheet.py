# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 16:56:03 2018

@author: navya
"""

N, M = map(int, input().split())
rows = [input() for _ in range(N)]
print(rows)
K = int(input())

for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row)
