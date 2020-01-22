# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 03:06:47 2020

@author: satye
"""
import re
beginsWithHiRegex = re.compile(r'^Hi')#^is for begins with
print(beginsWithHiRegex.search('Hi, how are you'))
print(beginsWithHiRegex.search('he said "Hi"'))#no match as hi not in start

endsWithWorldRegex = re.compile(r'world$')
print(endsWithWorldRegex.search('Hello world'))
print(endsWithWorldRegex.search('my world is here'))

entireTextRegex = re.compile(r'^\d+$')#string has to begin and end with just digits
print(entireTextRegex.search('123425'))
print(entireTextRegex.search('123x425'))

# .:anything except new line
atRegex = re.compile(r'.ad')
print(atRegex.findall('I am mad and sad about the bad things'))
atRegex2 = re.compile(r'.{1,2}ad')#words with at with 1 or 2 chars preceeding(before)
print(atRegex2.findall('I am mad and sad about the bad things'))

#Regex to find firt name, last name group from text
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') #Greedy
print(nameRegex.findall('First Name: Satyen Last Name: Amonkar'))
#nameRegex2 = re.compile(r'First Name: (.*?) Last Name: (.*?)') #Non Greedy
#print(nameRegex2.findall('First Name: Satyen Last Name: Amonkar'))

serve = '<this is a test> for you.>'
nongreedy = re.compile(r'<(.*?)>') #to find all content between <>
print(nongreedy.findall(serve))
greedy = re.compile(r'<(.*)>') #to find all content between <>
print(greedy.findall(serve))

#dotstar only finds num,char not new lines
dotStar = re.compile(r'.*')
text = 'this is it. \nyou can do it. \n you did it :)'
print(dotStar.search(text))
#DOTALL takes care of this
dotStar2 = re.compile(r'.*',re.DOTALL)
print(dotStar2.search(text))
#handling case insensitive matching
vowelRegex = re.compile(r'[aeiou]',re.I)
print(vowelRegex.findall('Hi, you knOw that this is It!'))


