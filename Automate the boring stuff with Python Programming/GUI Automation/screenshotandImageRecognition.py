# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 02:58:31 2020

@author: satye
"""
import pyautogui

#Page Screenshot
#pyautogui.screenshot()
#pyautogui.screenshot('c:\\screenshot.png') #storing location of screenshot

#Image Recognition
print(pyautogui.locateOnScreen('C:\\Users\\satye.MSI\\Documents\\GitHub\\Python-Practice\\Automate the boring stuff with Python Programming\\GUI Automation\\5KEY.png')) #if cannot find on screen or overlap: None answer
#pyautogui.locateCenterOnScreen('C:\\Users\\satye.MSI\\Documents\\GitHub\\Python-Practice\\Automate the boring stuff with Python Programming\\GUI Automation\\5KEY.png')
pyautogui.moveTo((932,336),duration=1)
pyautogui.click((932,336))
