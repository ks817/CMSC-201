

def main():
    askDes = input("What is your favorite dessert? ")

    if askDes == "pie":
        askFlavor = input("What is your favorite flavor? ")
        if (askFlavor != "apple") and (askFlavor != "sweet potato"):
            print(askFlavor, "is interesting flavor.")
        else:
            print("That is the correct answer! ")

    elif askDes == "ice cream":
        askScoops = int(input("How many scoops do you usually get? "))
        if askScoops >= 3:
            print("That's quite a lot of ice cream! ")
        elif askScoops == 1 or askScoops == 2:
            print("That's a normal amount of ice cream.")
        elif askScoops <= 0:
            print("Add a few more scoops!")

    else:
        print("Sounds Yummy!")
            
main()
