# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:21:27 2020

@author: satye
"""

import re

# 1. finding number
#phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#mo = phoneNumRegex.search('My number is 315-493-2341')
#print(mo.group())

#2. Splitting area code from number
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 315-493-2341')
print(mo.group())
print(mo.group(1))
print(mo.group(2))

#3. regex to match literal parenthesis '()' in the regex string
phoneNumRegex2 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d')
mo2 = phoneNumRegex2.search('My number is (315) 493-2341')
print(mo2.group())

# pipes can be used to identify multiple possibilities

batRegex = re.compile(r'Bat(man|mobile|copter|man)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1)) # to identify which suffix was found
