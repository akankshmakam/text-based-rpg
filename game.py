import time

ansA=['yes','y','Y','Yes']
ansN=['no','n','N','No']
A=['A','a']
B=['b','B']
C=['C','c']
ansQ=['q','Q','quit','Quit']
ansR=['r','R','restart','Restart']
#weapons
sword=0
rock=0
torch=0
car_keys=1

def start():
 print('Welcome to the Adventure Game')
 print('Are you ready to play the game?\t (Yes(y)/No(n) \n you can always quit the game by typing Q/quit or restart the game by typing R/restart')
 time.sleep(1)
 choice=input('>>')
 if choice in ansN:
     print('Sad to hear you do not want to play our game')
     time.sleep(1)
     print('Game Over!')
 elif choice in ansA:
     print('Great choice! Game is loading...')
     time.sleep(2)
     opt_intro()
 elif choice in ansR:
     print('Restarting the game....')
     time.sleep(3)
     start()
 elif choice in ansQ:
     print('Quiting game....')
     time.sleep(1)
     print('Game Over!')
 else:
     print('You can choose only Yes/No')
     time.sleep(1)
     start()
    

def opt_intro():
    print('Great Choice!')
    time.sleep(1)
    print('Its your last day of work in the week and you get ready for a trip planned by you and your friends...')
    print('You take your car keys and get into the car and leaves your home...')
    time.sleep(3)
    print('After travelling a long distance alone to reach your the destination, your car stops suddenly in an open forest.')
    print('You get out the car taking the car keys and tries to find out what the problem is...')
    time.sleep(3)
    print('A wild wolf comes out of a bush and sees you and runs towards you')
    print('What would you do?')
    time.sleep(7)
    print('A: Get into the car, closes all windows and tries to escape from the car')
    print('B: Picks up a handful of rocks from the ground and throws a rock at the wolf')
    print('C: Starts running inside the forest')
    choice=input('>>')
    if choice in A:
        print('You try to start the car but it did not')
        print('The wolf breaks one of the window and kills you')
        time.sleep(1)
        print('Game Over!')
    elif choice in B:
        rock=6
        print('You picked up 6 rocks')
        opt_rock()
    elif choice in C:
        print('After running some far, you see a cave')
        opt_cave()
    elif choice in ansR:
        print('Restarting the game....')
        time.sleep(1)
        start()
    elif choice in ansQ:
        print('You quit the game')
        time.sleep(1)
        print('Game Over!')
    else:
        print('You chosed the wrong option and you were killed by the wolf')

def opt_rock():
    print('You picked 6 rocks and threw one at the wolf')
    rock=5
    time.sleep(1)
    print('The wolf is stunned for some seconds')
    print('The wolf starts running towards you again')
    print('What would you do?')
    time.sleep(1)
    print('A: Throws more rocks')
    print('B: Gets into the car and tries to escape')
    print('C: Starts running inside the jungle')
    choice=input('>>')
    if choice in A:
        print('The wolf dogged the rocks and killed you')
        time.sleep(1)
        
        print('Game Over!')
    elif choice in B:
        print('You try to start the car but it did not')
        print('The wolf breaks one of the window and kills you')
        time.sleep(1)
        print('Game Over!')
    elif choice in C:
        print('After running some far, you see a cave')
        time.sleep(1)
        opt_cave()
    else:
        print('Wrong option! The wolf killed you')
        time.sleep(1)
        print('Game Over!')

def opt_cave():
    print('Do you want to enter the cave?')
    choice=input('>>')
    if choice in ansA:
        print('You entered the cave!')
        time.sleep(1)
        print('Its too dark and you take out the torch from your pocket')
        print('You notice that you have dropped your car keys while running in the forest')
        car_keys=0
        torch=1
        print('You turn on the torch')
        time.sleep(1)
        print('You see a rusted sword on the ground..What would you do?')
        time.sleep(1)
        print('A: You pick up the sword and get ready to kill the wolf')
        print('B: Leaves the sword behind and gets out of the cave and starts running..')
        print('C: You hide inside the cave')
        choice=input('>>')
        if choice in A:
            print('The wolf jumped on you and you pierced the sword into the wolf and gets out of the cave')
            time.sleep('You see a small village after walking some distance...')
            time.sleep(1)
            print('Game loading...')
            time.sleep(2)
            opt_village()
        elif choice in B:
            print('You start running again you see a small village..')
            time.sleep(1)
            print('Game loading...')
            time.sleep(1)
            opt_village()
        elif choice in C:
            print('You hid in the dark')
            time.sleep(1)
            print('The wolf enters and smells you and you were killed by the wolf')
            time.sleep(1)
            print('Game Over!')
        elif choice in ansR:
            print('Restarting the game....')
            time.sleep(1)
            start()
        elif choice in ansQ:
            print('Game Over!')

    elif choice in ansN:
        print('You stood like a statue and the wolf smelled you and killed')
        time.sleep(1)
        print('Game Over!')
    elif choice in ansR:
        print('Restarting the game....')
        time.sleep(1)
        start()
    elif choice in ansQ:
        print('You quit the game..')
        time.sleep(1)
        print('Game Over!')
    else:
        print('You chosed the wrong option! You died')
        time.sleep(1)
        print('Game Over!')
def opt_village():
    print('Do you want to enter this village?')
    choice=input('>>')
    if choice in ansN:
        print('You start going back to the place where your car is there and meanwhile you find the car keys you dropped in the jungle and goes back home')
        time.sleep(2)
        print('Game Over!')
    elif choice in ansA:
        print('You go the village and takes rest for sometime')
        time.sleep(1)
        print('You start going back to the place where your car is there and meanwhile you find the car keys you dropped in the jungle and goes back home')
    elif choice in ansR:
        print('Restarting the game....')
        time.sleep(1)
        start()
    elif choice in ansQ:
        print('You quit the game..')
        time.sleep(1)
        print('Game Over!')    
    else:
        print('You start going back to the place where your car is there and meanwhile you find the car keys you dropped in the jungle and goes back home')
        time.sleep(1)
        print('Game Over!')



start()


