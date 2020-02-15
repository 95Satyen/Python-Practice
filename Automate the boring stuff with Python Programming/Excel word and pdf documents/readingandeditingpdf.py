# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:08:43 2020

@author: satye
"""

import PyPDF2
import os
os.chdir('C:\\Users\\satye.MSI\\Documents\\GitHub\\Resume is LIT')
pdfFile = open('Resume DA0402019.pdf','rb') #rb for read in binary mode
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages) #checks number of pages
page = reader.getPage(0)#get first page of pdf 
print(page.extractText())
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText)


#################################
#combining files  
pdf1File = open('Resume DA0402019.pdf','rb')
pdf2File = open('Resume DA01292019.pdf','rb')
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)
writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)
for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)
    
outputFile= open('combinedresume.pdf','wb') #write binary files
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()