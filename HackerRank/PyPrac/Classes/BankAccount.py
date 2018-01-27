# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 23:28:26 2018

@author: navya
"""

class BankAccount:
    def __init__(self,balance):
        self.balance=balance;
        
    def withdraw(self,amount):
        self.balance-=amount;
        return self.balance;
    
    def deposit(self,amount):
        self.balance+=amount;
        return self.balance;
    
if __name__=='__main__':
    a=BankAccount(10);
    print (a.withdraw(5))
        