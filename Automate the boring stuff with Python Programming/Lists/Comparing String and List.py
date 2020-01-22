# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 06:22:18 2019

@author: satye
"""

name ='Satyen'
print(name[0:3])

print('Sat' in name)

for i in name:
    print(i)
    
#List value is a mutable datatype: it can have values added, removed or changed
#However, String is a immutable datatype: it cannot be changed

#name[1] ='S' #cannot be assigned this way as String is immutable
newName = name[0]+'S'+name[2:len(name)]
print(newName)

str1=[0,1,2,3,4] #list
temp = str1 #assigning reference
temp[1]= "hi" #modifying both temp and str1 as both are the same list as list is mutable
print(temp,str1)

#to make an exact replica of list deepcopy function is used
import copy
temp2 = copy.deepcopy(temp) #temp2 is now a separate list
temp2[2]= 5
print(temp,temp2)

#Line continuation character
#1: for list: using enter after comma
games =['one piece',
        'dying light',
        'GTA 5']
#2: '\' for any other indentation
print('this is' + \
      ' it')
