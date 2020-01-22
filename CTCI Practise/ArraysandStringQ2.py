# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:58:12 2019

@author: Satyen
Purpose: Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
Hints: #7, #84, #722, #737
"""

class stringPermuatation:
    
    
    def __init__ (self,a=None,b=None):
        self.s1 = a
        self.s2 = b

    def main(self):
        def compHash(a=None,b=None): #time complexity o(n) but space 
            
            if len(a)!=len(b) :
                return "A is not a permutation of B"
            Hasha ={}
            Hashb ={}
            for i in range(0,len(a)):
                if(Hasha.get(a[i])!=None):
                    Hasha[a[i]] += Hasha[a[i]]
                else:
                    Hasha[a[i]] = 1
            for i in range(0,len(b)):
                if(Hashb.get(b[i])!=None):
                    Hashb[b[i]] += Hashb[b[i]]
                else:
                    Hashb[b[i]] = 1
            for i in range(0, len(a)):
                if Hasha[a[i]]!=Hashb[a[i]]:
                    return "A is not a permutation of B"
            return "A is a permutation of B"
        
        def comparray(a=None, b=None):
            if(len(a)!= len(b)):
                return "A is not a permutation of B"
            x =[0]*256
            for i in range(0,len(a)):
                temp = ord(a[i])
                if(x[temp]!=None):
                    x[temp] +=1
                else:
                    x[temp]=0
            for i in range(0, len(a)):
                temp = ord(b[i])
                if(x[temp]==0):
                    return "A is not a permutation of B"
                x[temp] -=1
            return "A is a permutation of B"
        return comparray(self.s1, self.s2)
        #return compHash(self.s1, self.s2)
        
    
    

if __name__ == "__main__":
    s = stringPermuatation("srinath","nathsrai")
    print(s.main())