# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 02:47:35 2020

@author: satye
"""

import pyautogui

#pyautogui.click(100,100);pyautogui.typewrite('Hello World!')
#pyautogui.click(200,100);pyautogui.typewrite('Hello World!',interval=0.2)
#pyautogui.click(200,100);pyautogui.typewrite(['a','b','left','left','X','Y'],interval=0.1)
print(pyautogui.KEYBOARD_KEYS)#different keyboardkeys
pyautogui.press('f1') #press single keys: keyboard shorcuts
pyautogui.hotkey('ctrl','O')