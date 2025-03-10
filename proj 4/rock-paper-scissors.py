import random
import sys
print("ROCK, PAPER, SCISSORS")
wins = 0
loss = 0
ties = 0
while True:#game loop
    print("%s wins, %s loss, %s ties" % (wins, loss, ties))
    while True: #input loop
        print("enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
        playermove = input()
        if playermove == 'q':
            sys.exit()
        if playermove == 'r' or playermove == 'p' or playermove == 's':
            break
        print("type r, p, s or q")
    #display what the player chose
    if playermove == 'p':
        print("Paper versus...")
    elif playermove == 'r':
        print("Rock versus...")
    elif playermove == 's':
        print("Scissors versus...")
    #display what the computer chose
    randomnum = random.randint(1,3)
    if randomnum == 1:
        computermove = 'r'
        print("Rock")
    elif randomnum == 2:
        computermove = 'p'
        print("paper")
    elif randomnum == 3:
        computermove = 's'
        print("scissors")

    if playermove == computermove:
        print("its arr tie")
        ties += 1
    elif playermove == 'r' and computermove == "s":
        print("you win")
        wins += 1
    elif playermove == 'r' and computermove == "p":
        print("you loose")
        loss += 1
    elif playermove == 'p' and computermove == "s":
        print("you loose")
        loss += 1
    elif playermove == 'p' and computermove == "r":
        print("you win")
        wins += 1
    elif playermove == 's' and computermove == "r":
        print("you loose")
        loss += 1
    elif playermove == 's' and computermove == "p":
        print("you win")
        wins += 1