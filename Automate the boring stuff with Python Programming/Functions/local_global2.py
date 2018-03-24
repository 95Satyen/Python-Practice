
#code in a local scope can access global variable
def spam():
    print(eggs)

eggs= 55
spam()
