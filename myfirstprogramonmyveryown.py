#choose your own adventure fantasy game
import random,sys, time

print('Choose a number between 1 and 4, or q to quit program')   #Character selection using while loop and if statements
while True:
    playerSelection = input()
    if playerSelection == 'q':
        sys.exit()
    if playerSelection == '1':
        print('You are a Cleric of Damascia')
    if playerSelection == '2':
        print('You are the last of the Dragon Tamers')
    if playerSelection == '3':
        print('You are a White Knight of the Rose Order')
    if playerSelection == '4':
        print('You are a Mage of the Eternal Order')
    break

def questClericA():        #definitions of what the Cleric will do and a call stack for fun
    print('Damascia, your hometown, is in the middle of a horrifying plague. Go there and quell the outbreak')
        #here i want a time delay of 0.2s before the next print function
    #make this a new definition and call it in the questCharachter defintion for a call stack. call it itemList()    print('Best to choose your equipment before you head out')
    print('(make a tic tac toe box on paper and write this down, because its the only time youll see it!)')
def questClericB():
    print('A group of wandering nomads asks you to train them to become Clerics')
    print('Give them the strength they need')
def questClericC():
    print('The Horrid Witch has been devouring children by the dozen!')
    print('Kill it! Kill it! Kill it!!!!')
print('What type of quest would you like to go on today? (select A, B, or C: any other key quits program)')   #Quest selection
while playerSelection=='1':
    print('A: Save a village from a plague...')
    print('B: Teach a group of wayward souls the True Path')
    print('C: Defeat the Horrid Witch of Squalid Lagoon')
    questSelect = input()
    if questSelect == 'A':
        questClericA()
    if questSelect == 'B':
        questClericB()
    if questSelect == 'C':
        questClericC()
    break
while playerSelection=='2':
    questSelect = input()
    if questSelect == 'A':
        print('Save a sacrificial victim..')
    if questSelect == 'B':
        print('Sacrifice a victim!')
    if questSelect == 'C':
        print('Try and catch a dragon!')
    break
while playerSelection=='3':
    questSelect = input()
    if questSelect == 'A':
        print('Save The Princess..')
    if questSelect == 'B':
        print('Escort a troupe through bandit land')
    if questSelect == 'C':
        print('Become the Kings Sacrificial Vessel')
    break
while playerSelection=='4':
    questSelect = input()
    if questSelect == 'A':
        print('Initiate the unwilling')
    if questSelect == 'B':
        print('Destroy the chains that bind you')
    if questSelect == 'C':
        print('Break off and start a new enclave')
    break

#def calltoContinue():
#    print('Press C when you are ready')
#    input()
#    if input() == 'C':
#        print('Lets go')
#    else:
#        print('Press C when you are ready please')

#calltoContinue()
