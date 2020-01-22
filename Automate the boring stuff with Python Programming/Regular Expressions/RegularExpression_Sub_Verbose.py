# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 10:25:59 2020

@author: satye
"""

import re
Regnames = re.compile(r'Agent \w+') #agent names re object
print(Regnames.findall('Agent James gave the secret documents to Agent Rocky'))

#we need to find and substitute agent names
print(Regnames.sub('****','Agent James gave the secret documents to Agent Rocky'))

#we need to give acronym only of agent
Regnames2 = re.compile(r'Agent (\w)\w*')# one word char and 0 or more word char
print(Regnames2.findall('Agent James gave the secret documents to Agent Rocky'))
print(Regnames2.sub(r'Agent \1****','Agent James gave the secret documents to Agent Rocky'))#\1 is first letter from found

#verbose strings: makes more readable, pattern need not be shown in one line(doesnt consider enter as new line)
re.compile(r'''
(\d\d\d-)|     # area code (without parens, with dash)
(\(\d\d\d\))
\d\d\d     #first 3 digits
-
\d\d\d\d   #last 4 digits
''', re.VERBOSE) #can also write comments in between

re.compile(r'''
(\d\d\d-)|     # area code (without parens, with dash)
(\(\d\d\d\))
\d\d\d     #first 3 digits
-
\d\d\d\d   #last 4 digits
''', re.VERBOSE | re.IGNORECASE | re.DOTALL) #multiple options