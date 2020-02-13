"""

************
*          *
*          *
*          *
************

"""

#def boxPrint (symbol, width, height):
#    print(symbol * width)
#    
#    for i in range(height-2):
#        print(symbol + (' ' * (width -2)) + symbol)
#        
#    print(symbol * width)

def boxPrint (symbol, width, height):
    
    if len(symbol) !=1:
        raise Exception('"symbol" needs to be a string of length 1 ')
    if (width<2) or (height<2):
        raise Exception('"width" and "height" must be greater than 2')
    print(symbol * width)
    
    for i in range(height-2):
        print(symbol + (' ' * (width -2)) + symbol)
        
    print(symbol * width)

        
boxPrint('*',15,5)
boxPrint('|',12,6)

#Doesn't work with 2 strings as we wanted to

#boxPrint('**',12,6)

#boxPrint('*',1,1)

import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('error_log.txt','a')#open in append mode
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written error_log.txt')
    
assert False,'This is the error message'    