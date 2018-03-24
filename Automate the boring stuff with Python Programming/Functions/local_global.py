eggs = 5
#local scopes from one function cannot access local scopes
#from another
def spam():
     eggs =100 
     bacon()
     print('local value for spam: '+ str(eggs))

def bacon() :
     eggs = 0  #local variable to bacon 

spam()

print('global value: '+ str(eggs))
