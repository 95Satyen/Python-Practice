# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 04:53:46 2020

@author: satye
"""

#text = 'this is satyen's code' #need escape character to handle 's

text = 'this is satyen\'s code'

text2 = ' Hi!\n How are you?\n I\'m fine.'
print(text2)
print(r'Hey Satyen\'s friends') #raw string prints forward slashes in escape characters

text3 = """Hey Satyen's friends,
Happy New Year.
Sincerely, 
Satyen.""" #multiline strings begin and end with tripple quotes and can span multiple lines
print(text3)

spam = 'hello world'

print('hello' in spam) #in is case sensitive
spam[1:3]
spam[-1]