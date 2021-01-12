# File:    hailstone.py
# Started: by Dr. Gibson
# Author:  Kusum Sharma
# Date:    04/15/2019
# Section: 25
# E-mail:  ks17@umbc.edu
# Description:
#   This file contains python code that implements the
#   "flight" of a hailstone, following the HOTPO rules
#   (also known as the Collatz Conjecture), recursively

# NO CONSTANTS NEEDED, THE NUMBERS USED IN flight() ARE
#    PART OF A FORMULA/MATHEMATICAL CONJECTURE

############################################################
# flight() recursively calculates the path of a hailstone
# Input:   the height of the hailstone
# Output:  a recursive call, which at the end returns 
#          the number of "steps" taken for the
#          hailstone to reach a height of 1
def flight(height):
    
    #### BASE CASES:
    # if height is zero or lower, print out an "invalid" message and return 0
    if (height <= 0):
        print("Invalid height of", height)
        return 0
    
    # stops when it reachs height of 1 (the ground)
    elif height == 1:
        print("Height of", int(height))
        return 1

    #### RECURSIVE CASES:
    
    else:
        # finds odd number
        num = height % 2 
        
        # if the current height is even, divide it by 2
        if num == 0:
            print("Height of", int(height))
            evenHeight = flight(height / 2)
            newHeight = int(evenHeight)
            return newHeight + 1
        
           # if the current height is odd, multiply it by 3, then add 1
        elif num > 0:
            print("Height of", int(height))
            oddHeight = flight((height * 3) + 1)
            newHeight =int(oddHeight)
            return newHeight + 1

        
        
def main():
    
    print("Welcome to the Hailstone Simulator!")
    msg = "Please enter a height for the hailstone to start at: "
    startHeight = int(input(msg))
    if startHeight <= 0:
        steps = flight(startHeight)
    else:
        # recursive call goes here
        steps = flight(startHeight) - 1
    
    print("\nIt took", steps, "steps to hit the ground.")
    
    print("Thank you for using the Hailstone Simulator!\n")
    
main()
