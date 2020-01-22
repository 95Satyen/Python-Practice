# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 00:14:12 2020

@author: satye
"""
import os
print(os.getcwd)
helloFile = open('C:\\Users\\satye.MSI\\Documents\\GitHub\\Python-Practice\\Automate the boring stuff with Python Programming\\Files\\hello.txt')
content = helloFile.read()
print(content)
helloFile.close()

helloFile2 = open('C:\\Users\\satye.MSI\\Documents\\GitHub\\Python-Practice\\Automate the boring stuff with Python Programming\\Files\\hello.txt')
print(helloFile2.readlines()) #returns list of strings

#opening file in write mode
helloFile3 = open('C:\\Users\\satye.MSI\\Documents\\GitHub\\Python-Practice\\Automate the boring stuff with Python Programming\\Files\\hello.txt','w')

#opening file in append mode
#helloFile3 = open('C:\\Users\\satye.MSI\\Documents\\GitHub\\Python-Practice\\Automate the boring stuff with Python Programming\\Files\\hello.txt','a') #if file doesnt exist then create

helloFile3.write('Hello!!\nHi!')
helloFile3.close()

bf = open('C:\\Users\\satye.MSI\\Documents\\GitHub\\Python-Practice\\Automate the boring stuff with Python Programming\\Files\\hello.txt','a')
bf.write('\nNew lines!')
bf.close()

#store variables in binary shelve files
import shelve
shelfFile = shelve.open('mydata')
shelfFile['key'] = ['satyen','srinath','mehul','andy']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['key'])
shelfFile.close()
