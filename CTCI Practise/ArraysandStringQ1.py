# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:02:59 2019

@author: Satyen
Purpose: Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
Hints: #44, #7 7 7, #732
"""

class UniqueChar:
    def __init__(self, tempstr=None):
            self.givenstring=tempstr
    
    def main(self):
        #print(self.givenstring)
        a = self.givenstring
        a = a.lower() # Handles upper case sensitivity
        def withoutdsB():
            #n^2 complexity using bruteforce
            print(a)
            count=0
            for i in range(0,len(a)):
                for j in range(i+1,len(a)):
                    if(a[j] == a[i]):
                        count += 1
            if(count>0):
                return "Not unique"
            else:
                return "Unique"
                        
        def withds():
            #n complexity
            HashMap = {}
            
# =============================================================================
#             for i in range(0,len(a)):
#                 temp = ord(a[i])-97
#                 if(temp>=0 & temp<26):
#                     HashMap[temp] = HashMap[temp]+1 
# =============================================================================
            for i in range(0,len(a)):
                if(HashMap.get(a[i]) != None):
                    HashMap[a[i]] += 1
                else:
                    HashMap[a[i]] = 1
                    
            for i in HashMap:
                if HashMap[i] >1:
                    return "Not Unique"
            return "Unique"
            
        def withoutdsS():
            #nlog(n) complexity when sorted
            x = sorted(a)
            count = 0
            for i in range(0, len(x)-1):
                if((i<len(a))&(x[i]==x[i+1])):
                    count +=1
            if(count>0):
                return "Not unique"
            else:
                return "Unique"
        return withds()   
        #return withoutdsS()        
        #return withoutdB()

        
if __name__=="__main__":
    #a="Satyen's cool"
    #b = "Satyen"
    c=UniqueChar("Satyen Rocks!")
    print(c.main())