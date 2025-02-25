# File:    decoder.py
# Started: by Dr. Gibson
# Author:  Kusum Sharma
# Date:    03/25/2019
# Section: 25
# E-mail:  ks17@umbc.edu
# Description:
#   This file contains python code that uses a function to 
#   pull out the uppercase letters from a list of strings
#   to decode a secret message.


######################################################################
# decode() decodes a message by extracting all of the 
#          lowercase letters to reveal the hidden meaning
# Input:   msgList; a list of strings
# Output:  secret;  a string containing the hidden message
def decode(msgList):
    secret = ""


    index = 0
    while len(msgList) > index:
        count = 0
        while count < len(msgList[index]):
            if (msgList[index][count]) == (msgList[index][count].lower()) :
                secret += msgList[index][count]
            count += 1
        
        index += 1
        count = 0
    return secret

def main():
    # message lists
    msg1 = ["THIs", "LIFe", "cANNOT", "rEALLY", "Be", "tRUE"]
    msg2 = ["WONdERING", "HoW", "gOOD", "SCOREs", "CaN", "REGULArLY", \
                "Be", "MANAgED", "YoU", "SHoULD", "STUdY"]
    msg3 = ["ThE", "DoG", "OCCUpIES", "HeR", "DAILy", "THoUGHTS", "THROuGH", \
            "WhICH", "aLL", "DAYdREAMS", "aRE", "gENERATED", "FrOM", "EVeN", \
            "aMONG", "tHE", "bEST", "FrIENDS", "THeY", "aRE", "kNOWN"]

    # calling the decode function for each
    ans1 = decode(msg1)
    ans2 = decode(msg2)
    ans3 = decode(msg3)

    # printing out the secret messages
    print("Message 1's secret was:")
    print(ans1)
    print()

    print("Message 2's secret was:")
    print(ans2)
    print()

    print("Message 3's secret was:")
    print(ans3)
    print()



main()

