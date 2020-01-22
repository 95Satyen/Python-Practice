# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 00:55:34 2020

@author: satye
"""

import os
for folderName, subfolders, filenames in os.walk('C:\\Users\\satye.MSI\\Documents\\GitHub\\Python-Practice\\Automate the boring stuff with Python Programming'):
    print('The folder is',folderName)
    print('The subfolders in ',folderName,'are: ',str(subfolders))
    print('The filenames in ',folderName,'are: ',str(filenames))
    print()
    
    for subfolder in subfolders:
        if 'fish' in subfolder:
            os.rmdir(subfolder)
            print('rm dir on',subfolder)