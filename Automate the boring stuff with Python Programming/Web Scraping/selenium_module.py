# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:02:48 2020

@author: satye
"""

from selenium import webdriver
browser = webdriver.Edge()
browser.get('https://automatetheboringstuff.com')
elem = browser.find_element_by_css_selector('body > div.main > div > h1')
print(elem)
elem.click()
elem2 = browser.find_elements_by_css_selector('p')#returns list of objects
print(len(elem2))