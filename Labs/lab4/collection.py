

def main():
    numBeanie = int(input("How many beanie babies would you like to enter? "))
    while numBeanie <= 0:
        numBeanie = int(input("How many beanie babies would you like to enter or type Q? "))
        
    count = 1
    babyValue = input("Enter a beanie baby value: ")
    actualMax = babyValue
    actualMin = babyValue
    while numBeanie > count:
        babyValue = input("Enterr a beanie baby value: ")
        if babyValue < actualMin:
            actualMin = babyValue
            
        if babyValue > actualMax:
            actualMax = babyValue
        count +=1
        
    print("The least valuable beanie baby was worth", actualMin)
    print("The most valuable beanie was", actualMax, "such value!")


main()
