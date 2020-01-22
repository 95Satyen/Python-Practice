# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:28:57 2020

@author: satye
"""

name = 'satyen'
place = 'Goa'
time = '6 pm'
food = 'fish'

s= 'Hello '+name+ ' you are invited to a party at '+ place + ' at ' + time +'.\nPlease bring '+ food + '.'
print(s) 

#using string formater
print('Hello %s, you are invited to a party at %s at %s. \nPlease bring %s.' % (name,place,time,food))