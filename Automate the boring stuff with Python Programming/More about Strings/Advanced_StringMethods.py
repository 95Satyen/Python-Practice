# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 06:21:02 2020

@author: satye
"""

spam = 'Hello World!'
print(spam.upper())
print(spam.lower())
#answer = input()
answer = 'hi'
print(answer.lower())
print('Lower Case:',answer.islower())
print('Upper Case:',answer.isupper())
alphabets ="satyen"
print('Alphabet:',alphabets.isalpha()) #only alphabets, no number or space
title = "This Is It!"#only first letter of each word in caps
print('Title: ', title.istitle())

print("Begins with Hello:",spam.startswith("Hello"))
print("Ends with World!:",spam.endswith("World!"))

#print(','.join(['cats','bats','rats']))
#print(' '.join(['cats','bats','rats'])) #joins multiple strings using separator
print('\n'.join(['cats','bats','rats']))

print(spam.split('o')) #breaks string into list using separator
'Hello'.rjust(10) #right justify
print('Hello'.rjust(10,'*'))
print(len('Hello'.ljust(2))) #left justify
'Hello'.center(10)
spam2 = 'Hello'.rjust(10)
print(spam2)
print(spam2.strip()) #strips whitespace from string
spam2.lstrip()
spam2.rstrip()

print('SpamSpamBaconSpamEggsSpamSpam'.strip('ampS'))
print('Satyen not cool!'.replace('not','is'))

#import pyperclip
#pyperclip.copy('Helloooo!!') #copy paste strings in clipboard