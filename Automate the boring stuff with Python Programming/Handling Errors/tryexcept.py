def division(divisor):
    try:
        return 5 / divisor
    except ZeroDivisionError:
        print('Error: you tried to divide by zero')

print(division(1))
print(division(0))
