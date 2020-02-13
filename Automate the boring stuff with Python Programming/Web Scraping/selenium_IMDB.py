# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:17:07 2020

@author: satye
"""
from selenium import webdriver
browser = webdriver.Edge()
browser.get('https://www.imdb.com/')
searchElem = browser.find_element_by_css_selector('#suggestion-search')
searchElem.send_keys('Parasite')
searchElem.submit()
searchElem.back()
browser.forward()
browser.refresh()
browser.quit()