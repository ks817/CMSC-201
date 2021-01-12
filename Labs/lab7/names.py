# File:        names.py
# Started:     by Brianna Richardson (& Dr. Gibson)
# Author:      Kusum Sharma
# Date:        03/11/2018
# Section:     25
# E-mail:      ks17@umbc.edu
# Description: This file contains python code that uses functions to allow 
#              a user to get information about a list of names entered.

MIN_NAME = 3
SENTINEL = "-1"

###################################################################
# printList() prints out a list, showing the index of each element
# Input:      theList; a list of any types of variables
# Output:     None
def printList(theList):
    #---------------------------------------------------------#
    # your function to print the list (indexes too) goes here #
    #---------------------------------------------------------#

    index = 0
    while index < len(theList):
        print("At index", index, "the name is", "/", theList[index], "/" )
        index +=1


######################################################################
# printMinStr() prints the string with the minimum length from a list
# Input:        theList; a list of strings
# Output:       None
def printMinStr(theList):
    #---------------------------------------------------------------#
    # your function to find and print the shortest string goes here #
    #---------------------------------------------------------------#

    index = 0
    minName = theList[index]
    while index < len(theList):
        if len(minName) > len(theList[index]):
            minName = theList[index]
        index +=1

    print("The shortest string in the list is",minName)
               
######################################################################
# printMaxStr() prints the string with the maximum length from a list
# Input:        theList; a list of strings
# Output:       None
def printMaxStr(theList):
    #--------------------------------------------------------------#
    # your function to find and print the longest string goes here #
    #--------------------------------------------------------------#

    index = 0
    #set max and min
    maxName = theList[index]
    while index < len(theList):
        if len(maxName) < len(theList[index]):
            maxName = theList[index]
        index +=1
    print("The longest string in the list is", maxName)


def main():
    nameList = []

    msg = "Enter a name (or " + SENTINEL + " to quit): "

    name = input(msg)

    # ask the user for names until they choose to exit
    while(name != SENTINEL):
        # check beforehand, so we only save valid names
        nameList.append(name)
        name = input(msg)

        
    printList(nameList)
    printMinStr(nameList)
    printMaxStr(nameList)

    # call the print function
    #------------------------------------------------------#
    # your code to call the function printList() goes here #
    #------------------------------------------------------#

    # print out the minimum and maximum length names
    #-------------------------------------------#
    #  your code to call the two functions for  #
    # printMinStr() and printMaxStr() goes here #
    #-------------------------------------------#

main()
