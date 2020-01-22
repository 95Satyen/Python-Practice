# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:06:04 2019

@author: Satyen
Purpose: Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
Hints: #7, #84, #722, #737
"""

class replaceString:
    
    def __init__ (self,st):
        self.s = st
        self.leny = len( st )
    
    def main(self):
        print(self.s)
        def lencheck():
            st = self.s
            for i in reversed(st):
                if st[i]==" ":
                    if st[i-1]!= " ":
                        self.leny= i-1
                        print(i)
                        break
                else:
                    print("yo")
                    break
        lencheck()
        print(self.leny)
                    
    

x = replaceString("my name is satyen  ")
x.main()