# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:41:35 2020

@author: satye
"""

import re

# ? : match preceding group zero or one times

#batRegex = re.compile(r'Batman | Batwoman')
batRegex = re.compile(r'Bat(wo)?man') #wo can appear 0 or 1 times in match
mo  = batRegex.search('The adventures of Batman')
print(mo.group())
mo1  = batRegex.search('The adventures of Batwoman')
print(mo1.group())
mo2  = batRegex.search('The adventures of Batwowoman')
print(mo2 == None)

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 315-234-2345')
print(mo.group())
mo1 = phoneRegex.search('My phone number is 234-2345')
print(mo1 == None) #cannot identify pattern if no area code

phoneRegex2 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex2.search('My phone number is 234-2345')
print(mo1.group())
#if we need ? as a part of our regex pattern use esacpe character \?

# * : match preceding group zero or more times

batRegex2 = re.compile(r'Bat(wo)*man') #wo can appear 0 or 1 times in match
mon  = batRegex2.search('The adventures of Batwowoman')
print(mon.group())

# +: match preceding group one or more times
batRegex3 = re.compile(r'Bat(wo)+man') #wo can appear 0 or 1 times in match
mon2  = batRegex3.search('The adventures of Batman')
print(mon2==None)

# Escape character match
es = re.compile(r'\*\+\?')
moes = es.search('5*+? escape')
print(moes.group())

# {x} : Exactly

rex = re.compile('(ha){3}')
morex = rex.search('He said "hahaha"')
print(morex.group())

#match 3 phone numbers in a row
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
print(phoneRegex.search('My numbers are 412-222-3452,123-2222,123-222-1234'))

# {x,y} : At least x, at most y
#rex = re.compile('(ha){3,5}')
rex = re.compile('(ha){3,}')#atmost any number
morex = rex.search('He said "hahahaha"')
print(morex.group())

#greedy matches: longest possible string
digitRegex = re.compile(r'(\d){3,5}')
print(digitRegex.search('1234567890')) #12345 : greedy match(max possible long string)
digitRegex = re.compile(r'(\d){3,5}?') #here ? is for non greedy match (different from any match)
print(digitRegex.search('1234567890'))
