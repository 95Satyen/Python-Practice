import random

print ('Hello. What is your name?')
name = input()

print('Hi '+ name +' guess a number between 1 & 20')
secretNumber = random.randint(1,20) #generates the random number between 1, 20

for guessesTaken in range (1, 7):
     print('Take a guess.')
     guess = int(input())
     if guess < secretNumber:
      print('The guess is too low')
     elif guess > secretNumber:
      print('The guess is too high')
     else :
      break

if(guess == int(secretNumber)):
 print('Your guess was correct in '+ str(guessesTaken) +' attempts')
else:
    print('Nope. I was thinking of :' + str(secretNumber))
