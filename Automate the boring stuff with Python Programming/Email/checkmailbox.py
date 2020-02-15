# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 02:04:42 2020

@author: satye
"""
#checking mail on mailbox
import imapclient #old library
conn = imapclient.IMAPClient('imap.gmail.com',ssl=True)#domain name,keyword arg as sll encryption
conn.login('95satyen@gmail.com','check')
conn.select_folder('INBOX', readonly=True)#keep read only access
UIDs = conn.search(['SINCE 20-Aug-2019'])
rawMessage = conn.fetch([47474],['BODY[]','FLAGS'])

import pyzmail
message = pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])
message.get_subject()
message.get_address('from')
message.get_address('to')
message.get_address('bcc')
message.text_part #check if email has only text part 
message.html_part == None
message.text_part.get_payload().decode('UTF-8')
message.text_part.charset == None


conn.list_folders()
UIDs = conn.search(['ON 15-Feb-2020'])
UIDs
conn.delete_messages(UIDs)