# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:05:00 2020

@author: satye
"""

import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') #for displaying here
logging.basicConfig(filename='logfile.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# logging.disable(logging.CRITICAL) #disables printing of logs

logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s)')
    total = 1
    #for i in range(1,n + 1):
    for i in range(n + 1):
        total *=i
        logging.debug('i is %s, total is %s' %(i,total))
    logging.info('Return value is %s' %(total))
    return total
print('Output %s' %(factorial(5)))

facttest = 5*4*3*2*1
if(factorial(5)!=facttest):
    logging.critical('Expected output %s' %(5*4*3*2*1))

logging.debug('End of program')