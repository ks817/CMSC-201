# File:        queryPoke.py
# Started by:  Chetra Mo (chet2@umbc.edu)
# Updated by:  Dr. Gibson (k.gibson)
# Author:      Kusum Sharma
# Date:        04/29/2019
# Section:     25
# E-mail:      ks17@umbc.edu
# Description:
#   This file contains python code that allows a user to "query" 
#   all first generation Pokemon that have a certain move
#   (entered in by the user) through use of a dictionary.

SENTINEL = "STOP"

#-------------------------------------------------------------------------
# createPokeDex() generates a dictionary containing every first generation
#                 pokemon, with their move list as the value
# Input:          ifp;     a file pointer to the text file containing the
#                          pokemon and their four different moves
# Output:         pokeDex; dictionary of pokemon : move list
#--------------------------------------------------------------------------
def createPokeDex(ifp):
    # initialize empty dictionary
    pokeDex = {}

    info = ifp.readlines()
    ifp.close()

    # loop through entire file and add the (key:value) pairs to the dictionary
    for i in range(len( info )):
        
        infoList = info[i].split()
        nameList = infoList[0]
        moves = infoList[1:]
        pokeDex[nameList] = moves

        #################################################################
        # assign list of values to key (AKA, assign moveset to Pokemon) #
        # HINT: this will be multiple lines of code -- probably 3 - 5   #
        # (try list slicing to separate out the pieces you need!)       #
        #################################################################



    return pokeDex


#-------------------------------------------------------------------------
# checkMoveExists() checks how many Pokemon know the moves from the move list
#                   entered in by the user
# Input:            pokeDex;  a dict with keys=Pokemon and values=moveset
#                   pkmnMove; a string of the move to look for
# Output:           total;    an integer, how many pokemon know that move
#--------------------------------------------------------------------------
def checkMoveExists(pokeDex, pkmnMove):
    total = 0 # total number of pkmn that know ALL the moves from pkmnMoveList
    
    # list of pokemon keys
    # TODO : finish this line of code
    poKeys = list(pokeDex.keys())

    # for loop that checks each pokemon in the dict
    # TODO: complete this for loop statement
    for i in range(len(poKeys)):

        # if a Pokemon has that move, print out the info and increment count
        # TODO: complete this if statement
        if pkmnMove in pokeDex[poKeys[i]]:
            
            # TODO : complete this print statement
            print(">> You have a", poKeys[i], "that knows", pkmnMove)
            total += 1

    return total



def main():
    # read in the pokedex file
    inputFile = open("pokedex.txt")

    # run createPokeDex() to generate the dictionary
    pokeDex = createPokeDex(inputFile)

    # print greeting
    print("   Hello, and welcome to your Pokemon Storage System!")
    print("   Would you like to search your box for all Pokemon")
    print("   that possess a specified move?\n")

    msg = "Please enter a move (type '" + SENTINEL + "' to finish): "
    moveRequest = input(msg)

    
    # keep asking for move to check until they want to exit
    while (moveRequest != SENTINEL):

        ####################################################
        # write the line of code to call checkMoveExists() #
        ####################################################
        countPoke = checkMoveExists(pokeDex, moveRequest)

        # TODO : complete the lines of code below
        if countPoke == 0:

            print("You do not have any Pokemon that know", moveRequest)
        else:
            print("You have", countPoke, "Pokemon that know", moveRequest)

        # get next move request
        moveRequest = input(msg)

    print("Shutting Down...")
    inputFile.close()


main()
