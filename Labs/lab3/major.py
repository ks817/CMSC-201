# File:        lab3.py
# Author:      Kusum Sharma
# Date:        02/11/2019
# Section:     25
# E-mail:      ks17@umbc.edu
# Description: This program contains a python code that
#              o
#              o 

def main():
    
    major =  input("Please enter your major: ")
    if major == "CMSC" or major == "CMPE":
        print("You need to earn at least a B for CMSC 201 to count.")
    else:
        print("You need to earn at least a C for CMSC 201 to count.")

main()
