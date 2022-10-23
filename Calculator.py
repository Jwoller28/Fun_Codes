# Calculator

import time

def addition ():
    print("Addition")
    n = float(input("Enter the first number: "))
    t = 0 #Total number enter
    addi = 0

    while n != 0:
        addi = addi + n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))

    return [addi,t]

def subtraction ():
    print("Subtraction")
    n = float(input("Enter the first number: "))
    n = -n
    t = 0 #Total number enter
    subt = 0

    while n != 0:
        subt = subt - n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))

    return [subt,t]

def multiplication ():
    print("Multiplication")
    n = float(input("Enter the first number (0 to calculate): "))
    t = 0 #Total number enter
    mult = 1

    while n != 0:
        mult = mult * n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    
    return [mult,t]

def division ():
    print("Division")
    n = float(input("Enter the first number: "))
    t = 0 #Total number enter
    divi = n
    n = 1

    while n != 0:
        divi = divi / n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    
    return [divi,t]

def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans,t]

# main...
firstTime = 0
while True:
    
    if(firstTime != 0):
        time.sleep(5)
    firstTime = 1

    list = []
    print(" Enter 'a' for addition")
    print(" Enter 's' for substraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'd' for division")
    print(" Enter 'v' for average")
    print(" Enter 'q' for quit")
    c = input(" ")

    if c != 'q':
        if c == 'a':
            list = addition()
            print("Ans = ", list[0], " total inputs ",list[1])

        elif c == 's':
            list = subtraction()
            print("Ans = ", list[0], " total inputs ",list[1])

        elif c == 'm':
            list = multiplication()
            print("Ans = ", list[0], " total inputs ",list[1])

        elif c == 'd':
            list = division()
            print("Ans = ", list[0], " total inputs ", list[1])

        elif c == 'v':
            list = average()
            print("Ans = ", list[0], " total inputs ",list[1])

        else:
            print ("Sorry, invilid character")

    else:
        break