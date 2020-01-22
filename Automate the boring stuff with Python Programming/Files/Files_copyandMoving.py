# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 00:31:26 2020

@author: satye
"""

import shutil
#copy file to D
print(shutil.copy('C:\\Users\\satye.MSI\\Documents\\GitHub\\Python-Practice\\Automate the boring stuff with Python Programming\\Files\\hello.txt','D:'))
#copy and rename file to yollo
print(shutil.copy('C:\\Users\\satye.MSI\\Documents\\GitHub\\Python-Practice\\Automate the boring stuff with Python Programming\\Files\\hello.txt','D:\\yollo.txt'))

#copy all subfolders
shutil.copytree('C:\\Users\\satye.MSI\\Documents\\GitHub\\Python-Practice\\Automate the boring stuff with Python Programming\\Files','D:\\filesbackup')

#move file to different folder
shutil.move('D:\\yollo.txt','D:\\filesbackup')

#for removing files you need it to be completely empty
#print(os.rmdir('D:\\filesbackup'))

#rmtree can still remove the file
shutil.rmtree('D:\\filesbackup')

#send2trash is a safe version which sends files to recycle bin instead of permanently deleting them
import send2trash
send2trash.send2trash('D:\\hello.txt')