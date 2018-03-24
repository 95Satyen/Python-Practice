print('How old are you?')
age = input()

try:
    if int(age) >= 18:
        print('You are permitted to drive')
    else:
        print('Sorry, you are not permitted to drive')
except ValueError:
    print('You did not enter a number.')
            
