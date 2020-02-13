# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:59:05 2020

@author: satye
"""

import requests
#requests.get stores a response object
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)

print('length of text: %s' %(len(res.text)))
print(res.text[:200])
print(res.raise_for_status())

#badRes = requests.get('https://www.satyenamonkar.me/text.txt')
#print(badRes.raise_for_status()) #good to test whether program holds incase wrong url
#print(badRes.text[:20])

#downloading files from website url(without login)
playFile = open('data.txt','wb') #write binary data: for maintaing unicode
for chunk in res.iter_content(100000): #returns chunks of the content through each itteration, 1000 bytes per iteration
    playFile.write(chunk)
    
playFile.close()
    