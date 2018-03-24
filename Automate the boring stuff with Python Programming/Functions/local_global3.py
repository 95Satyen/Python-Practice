def spam():
    global eggs
    eggs= 'yo!'
    print(eggs)

eggs= 55
spam()
print(eggs)
