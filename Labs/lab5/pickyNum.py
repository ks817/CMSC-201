# File:        pickyNum.py
# Created by:  Dr. Gibson (k.gibson)
# Author:      Kusum Sharma
# Date:        02/25/2018
# Section:     25
# E-mail:      ks17@umbc.edu
# Description:
#   This file contains python code that helps choose
#   a number to statisfy your very picky friend.

def main():

    print("You have a friend who is very picky about their numbers.  They've")
    print("asked you to choose a number that meets certain requirements, but")
    print("you're a lazy computer scientist, so you decided to code a program")
    print("that will check it for you, instead of thinking about it too hard.")
    print("")
    print("The requirements are that the number satisfy the following:")
    print("     positive (greater than zero), less than 1000, ")
    print("     divisible by 4, end in an 8, NOT end in a 2")
    
    numValid = False

    while not numValid:
        num = int(input("Please enter your number: "))
        numValid = True
        divideFour = num % 4
        endsEight = num % 10
        
        if num <= 0:
            numValid = False
            print("The number must be greater than zero.")

        if num >= 1000:
            numValid = False
            print("The number must be less than 1000.")

        if divideFour != 0:
            numValid = False
            print("The number must be divisible by 4.")

        if endsEight != 8:
            numValid = False
            print("The number must end in an 8.")

        if endsEight == 2:
            numValid = False
            print("The number must NOT end in a 2.")
            
        # The different conditionals should go here.  Don't forget
        # to tell the user EVERYTHING that was wrong with their
        # number, and to update the value of the Boolean flag!


    
    print("Congrats!  Your friend accepts the number", num)


main()
