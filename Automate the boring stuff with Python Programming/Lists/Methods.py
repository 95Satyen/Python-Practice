# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 06:01:14 2019

@author: satye
"""

names = ['Fluffy','Tommy','Moti','Fenny','Jolly','Boney']

print(names.index('Jolly')) #prints the index of value in the list if found

names.append('Coffee') #appends value at the end of the list
print(names)

names.insert(1,'Maya') #can inset value at any index in the list
print(names)

#Note: For append and index we do not assign the values, functions return None
names.remove('Tommy')
print(names) #removes value from list if present
#Note: only first instance found is removed using remove
del names[3] #this deletes value at index 3
print(names)

names.sort() #sort the values in the list
print(names)
names.sort(reverse=True) #sort in descending order
print(names)
#Note: we cannot sort lists containing both numbers and strings
#Note: while sorting strings, uppercase letters come first
names.append('fluffy')
names.sort() #sorting happens in ASCII-betical order
print(names)
names.sort(key=str.lower) #sorts in true alphabetical order
print(names)