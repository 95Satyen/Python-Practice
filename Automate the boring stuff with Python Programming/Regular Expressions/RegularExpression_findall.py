# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 23:25:06 2020

@author: satye
"""

import re
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

resume = '''Sofia Flores
Miami, FL • 123-456-7891
sflores@email.com

SUMMARY
Detail-oriented Accountant with 3 years of experience performing accurate work at a quick and efficient pace to service the needs of clients.

EDUCATION
Northwest Vermont University
Aug '10 - May '14
Bachelor of Science in Accounting

EXPERIENCE
Crane & Jenkins, Accountant
Feb '15 - Current
Review detailed financial statements and plan audits
Responsible for monthly reconciliation of cash accounts
Prepare and monitor budget, as well as provide analysis compared to department expense reports
Prepare weekly, bi-weekly, and monthly payroll journal entries
Recommend solutions to complex accounting functions
Contact No: 123-345-1234
Tradelot, Accountant
Current - Current
Developed and maintained positive relationships with clients
Handled sensitive information in discrete and careful manner
Applied payments to merchant accounts and updated billing info
Performed monthly bank reconciliations to various cash accounts
Prepared, reviewed, and analyzed quarterly and annual financial statements to present to executives
SKILLS
Certified Public Accountant (CPA) License
QuickBooks
FRx Reporting
Contract Negotiations
Reconciliations
Variance Analysis '''
print(phoneRegex.findall(resume)) #grouped findall gives list of tuples
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(resume)) #gives complete and split groups

#digitRegex = re.compile(r'/d')
digitRegex = re.compile(r'0|1|2|3|4|5|6|7|8|9')

#character classes
lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming'
xmaxRegex = re.compile(r'\d+\s\w+')#pattern with one or more digits followed by a space and one or more words
print(xmaxRegex.findall(lyrics))
#xmaxRegex2 = re.compile(r'\d+\s\w+\s\w+\s\w+')#pattern with one or more digits followed by a space and one or more words
#print(xmaxRegex2.findall(lyrics))
#find vowel combinations
vowelRegex = re.compile(r'[aeiouAEIOU]')#all vowels in string
print(vowelRegex.findall('Robocop eats baby food.'))
#find double vowel combination
vowelRegex2 = re.compile(r'[aeiouAEIOU]{2}')
print(vowelRegex2.findall('Robocop eats baby food.'))
#negative character class
vowelRegex3 = re.compile(r'[^aeiouAEIOU]') #all but vowels
print(vowelRegex3.findall('Robocop eats baby food.'))