#!/usr/bin/env python3

import random

print("Think of a number between 1 to 100")
MinNumber = 1
MaxNumber = 100
count = 0

while True:

    RandomNumber = random.randrange(MinNumber, MaxNumber)
    Answer = input("My guess is {}\n1. Too High 2. Too Low 3. That's my number!: ".format(RandomNumber))

    ## Too High
    if Answer == "1":
        MaxNumber = RandomNumber

    ## Too Low
    elif Answer == "2":
        MinNumber = RandomNumber

    elif Answer == "3":
        print("Congrats, you won!")
        print("The program took {} times to guess the correct answer".format(count))
        break

    count = count + 1
