# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 06:05:11 2019

@author: satye
"""

newDict = {'key1':'value1','satyen':'amonkar','priyanka':'amonkar'}
print(newDict['key1'])
#newDict[0] There is no first item in dictionary as compared to list

newDict2 = {'priyanka':'amonkar','key1':'value1','satyen':'amonkar'}

print(newDict==newDict2) #dictionary keys don't have any particular order

print(newDict['satyen'])

print('key1' in newDict)
print('satyen' not in newDict) 
#Dictionary  are mutable (like list): variables hold references

#Dictionary Methods:
print(list(newDict.keys())) #print list of keys
#print(list(newDict.values())) #print values
#print(list(newDict.items())) #print list of key, value pairs

#for key in newDict.keys():
#    print(key)
#    
#
#for value in newDict.values():
#    print(value)
#    
#for key,value in newDict.items():
#    print(key,value)
#    
#for tuple in newDict.items():
#    print(tuple) #print tuples
    
print(newDict.get('satyen','not present')) #if key present return value else return not present

newDict.setdefault('satyen','black') #sets default value of key 'satyen' as 'black' if key doesnt exist

text = ' this is it!'
count = {}
for character in text.upper():
    count.setdefault(character,0) #set value of key as 0 if not found
    count[character] = count[character]+1 #increase count value of the key
print(count)

import pprint #pprint is pretty print function that can display dictionary value cleanly
#pprint.pprint(count)
rjtext = pprint.pformat(count) #pformat returns output as a string
print(rjtext)