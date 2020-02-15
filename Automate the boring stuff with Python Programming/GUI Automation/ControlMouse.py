# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 02:26:39 2020

@author: satye
"""

import pyautogui
print(pyautogui.size()) #screen resolution
width, height = pyautogui.size()
print(pyautogui.position())#position of mouse
pyautogui.moveTo(10,10)
pyautogui.moveTo(10,10,duration=2)#duration for movement
pyautogui.moveRel(200,0)#move mouse relatively to current position
pyautogui.moveRel(0,-100)
print(pyautogui.position())#for current mouse position
pyautogui.click(804,0)
pyautogui.rightClick()