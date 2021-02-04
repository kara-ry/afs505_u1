# ask the user if they like dogs or cats better 

print("""What do you like better? Cats or dogs?
Enter 1 for Dogs, 2 for Cats.
Choose wisely.""")

# Let users set value 
animal = input("> ")

# create if/else 
if animal == "1":
    print("Good choice!")
    print("Should I get another dog?")
    print("1 for yes, 2 for no")

    newdog = input("> ")

    if newdog == "1":
        print("Correct again!")
        print("I should always get more dogs")
    elif newdog == "2":
        print("Boooooooo")

elif animal == "2":
    print("Wrong") 
    

