# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:33:29 2020

@author: satye
"""

import webbrowser,sys, pyperclip
#webbrowser.open('https://www.satyenamonkar.me/') #opens website

sys.argv

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open()