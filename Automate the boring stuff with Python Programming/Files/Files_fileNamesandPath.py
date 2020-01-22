# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:38:59 2020

@author: satye
"""


print('\\')
print('c:\\spam\\eggs.png')#we need double \\ as \ requires wildcard
location= '\\'.join(['C:','folder1','folder2','folder3','file.png'])
print(location) #This will only work for windows

#for all operating systems use OS library
import os
location2= os.path.join('C:','folder1','folder2','folder3','file.png')
print(location2) #the slashes will automatically be adjusted based on os(mac,windows, etc)
print(os.sep)#separator used

print(os.getcwd())#current working directory

os.chdir('C:\\') #update current working directory
print(os.getcwd()) #new wordking directory
print('Absolute file path:',location2)
print('\nRelative file path:','file.png')

#Relative path: '.\' for this folder, '..\' for parent folder
os.chdir('C:\\Users\\satye.MSI\\Documents\\GitHub\\Python-Practice\\Automate the boring stuff with Python Programming\\Files')
#converting relative file path to absolute file path 
print(os.path.abspath('spam.png'))#shows absolute path 
print(os.path.abspath('..\\..\\file.png')) #file present in parent's parent folder

print(os.path.isabs('..\..\file.png'))
print(os.path.isabs('c:\\folder\\folder'))

print(os.path.relpath('C:\\Users\\satye.MSI\\Documents\\GitHub\\Python-Practice\\Automate the boring stuff with Python Programming\\Files','C:\\Users\\satye.MSI'))

#extracting directory part of path
print(os.path.dirname('c:\\spam\\eggs.png'))
#extracting last file or folder
print(os.path.basename('c:\\spam\\eggs.png'))

print(os.path.exists('c:\\spam\\eggs.png'))
print(os.path.isfile('c:\\spam\\eggs.png'))
print(os.path.isdir('c:\\spam'))

print(os.path.getsize('C:\\Users\\satye.MSI\\Documents\\GitHub\\Python-Practice\\Automate the boring stuff with Python Programming\\Files\\Files_fileNamesandPath.py')) #size of file

print(os.listdir('C:\\Users\\satye.MSI\\Documents\\GitHub'))


totalSize = 0

for filename in os.listdir('C:\\Users\\satye.MSI\\Documents\\GitHub'):
    if not os.path.isfile(os.path.join('C:\\Users\\satye.MSI\\Documents\\GitHub', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\satye.MSI\\Documents\\GitHub', filename))

print(totalSize)

os.makedirs('c:\\delicious\\walnut\waffles') #creates folders in directory
