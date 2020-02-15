# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 20:46:15 2020

@author: satye
"""
#Simple Mail Transfer Protocol to send email
import smtplib
conn = smtplib.SMTP('smtp.gmail.com',587) #creating connection object:domain name and port no
print(conn)
print(conn.ehlo())#to start connection: 250:response code and bytes object
conn.starttls()#to encrypt password
conn.login('95satyen@gmail.com','YouKn2w!')
conn.sendmail('95satyen@gmail.com','95satyen@gmail.com','Subject: hi... \n\nDear Satyen, \nHow are you')
conn.quit()
