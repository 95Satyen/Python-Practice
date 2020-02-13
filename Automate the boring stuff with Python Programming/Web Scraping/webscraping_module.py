# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 01:57:32 2020

@author: satye
"""

import bs4 #beautiful soup
import requests

res = requests.get('https://www.satyenamonkar.me/')
print(res.raise_for_status())
#bs4.BeautifulSoup(res.text)
soup = bs4.BeautifulSoup(res.text,'html.parser') #html.parser to remove warnings
#print(soup.select('#top > div > header > p'))
elem = soup.select('#top > div > header > p')
print(elem[0].text)
print(elem[0].text.strip()) #strip removes white spaces