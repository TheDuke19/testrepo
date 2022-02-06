#this is a guess the number game.
import random
secretNumber = random.randint(1,200)
print('I am thinking of a number between 1 and 200.')

#Ask the player to guess 6 times
for guessesTaken in range(1,7):
    print('Take a guess. You have 6 attempts.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #This condition is the correct guess!

if guess == secretNumber:
    print('Fuck yeah, you got it in '+str(guessesTaken) +' guesses!')
else:
    print('Nah, your wrong, Iiii was thinking of the number ' +str(secretNumber) +' for reals...')
