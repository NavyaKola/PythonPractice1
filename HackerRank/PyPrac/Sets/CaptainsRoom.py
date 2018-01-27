# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 11:46:41 2018

@author: navya
"""

numOfPeopPerEachGroup=int(input());

listOfRoomNumbers=list(map(int, input().split()));
setList=set(listOfRoomNumbers);
temp=((sum(setList)*numOfPeopPerEachGroup)-(sum(listOfRoomNumbers)))
print(temp//(numOfPeopPerEachGroup-1))
