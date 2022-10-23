import random
import time
x=0

while(x==0):
    pchoice = int(input("1 for Rock, 2 for Paper, 3 for Scissors?\n"))

    options=[1,2,3]
    bchoice = random.choice(options)

    #bchoice 1 = rock
    #bchoice 2 = paper
    #bchoice 3 = scissors

    if pchoice == 1:
        print("You chose rock!")

    elif pchoice == 2:
        print("You chose paper!")

    elif pchoice == 3:
        print("You chose scissors!")
        
    else:
        print("Invalid input")



    if bchoice == 1:
        print("Your opponent chose rock!")

    elif bchoice == 2:
        print("Your opponent chose paper!")

    elif bchoice == 3:
        print("Your opponent chose scissors!")

    

    x=3
    time.sleep(1)
    while(x>0):
        print(x)
        x-=1
        time.sleep(1)

    if ((pchoice == 1 and bchoice == 1) or (pchoice == 2 and bchoice == 2) or (pchoice == 3 and bchoice == 3)):
        print("It's a tie!")

    elif((pchoice == 1 and bchoice == 2) or (pchoice == 2 and bchoice == 3) or (pchoice == 3 and bchoice == 1)):
        print("You LOSE!")

    elif((pchoice == 1 and bchoice == 3) or (pchoice == 2 and bchoice == 1) or (pchoice == 3 and bchoice == 2)):
        print("You WIN!")


    again=int(input("Play again? If so... press 1 \n"))

    if (again != 1):
        x+=1


