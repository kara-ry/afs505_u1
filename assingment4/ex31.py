# Print out first question using triple quotes for multiple lines
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

# Give user option in input and set door variable 
door = input("> ")

# Create if/else with print options dependent on the input for users who origionally picked 1
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input(">")  # allow user to specify value for bear

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.") # Insert the value of bear into this statement if bear doesn't equal 1 or 2
        print("Bear runs away.")

# Create if/else with print options if user picked option 2 for the first question

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")    # Allow user to set value of insanity 

    if insanity == "1" or insanity == "2": # if a user inputs 1 or 2, print these two lines
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:  # If the user inputs anything but 1 or 2, print these two lines
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

# If a user inputs something other than 1 or 2 to the origional question, print this statement
else:  
    print("You stumble around and fall on a knife and die. Good job!")
