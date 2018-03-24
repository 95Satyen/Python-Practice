print('Sum', end='')
print('mation')

def sum(a,b):
    return a+b

print('Enter x and y')
x = input()
y = input()
print('Enter String or Number')
value=input()
if(bool(value)==True):
 print(sum(int(x),int(y)))
else:
 print(sum(x,y))
