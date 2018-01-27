# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 15:15:38 2018

@author: navya
"""
import calendar;
month,day,year=map(int,input().split());

calendar.setfirstweekday(calendar.SUNDAY)
a=["MONDAY", "TUESDAY","WEDNESDAY","THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
x=calendar.weekday(year, month, day)
print(a[x])
