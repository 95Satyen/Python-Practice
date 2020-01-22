# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:11:28 2020

@author: satye
"""

import re

message = 'Call me 315-403-4522 tomorrow, or at 315-403-5555'

#Regex string often use \backslashes(like \d), so they are often raw strings: r'\d'
#re.compile creates a regex object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #r stands for raw string, \d for digit
matchObject = phoneNumRegex.search(message) #search for pattern: phoneNumRegex in text: message (first occurance)
#matchObject.group() #shows actual text
print(matchObject.group()) #prints first occurance of pattern
matchObject2 = phoneNumRegex.findall(message)
print(matchObject2) #prints list of occurances
