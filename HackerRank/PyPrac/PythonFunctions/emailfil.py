# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:54:14 2018

@author: navya
"""

def check_valid(email):
    try:
        username, url = email.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False
    
    if not username.replace("-", "").replace("_", "").isalnum():
        return False
    if not website.isalnum():
        return False
    if len(extension) > 3:
        return False
    return True

n = int(input())
emails = [input() for email in range(n)]

valid = list(filter(check_valid, emails))
print(sorted(valid))