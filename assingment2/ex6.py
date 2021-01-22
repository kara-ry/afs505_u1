# Create a variable named types_of_people to value of 10
types_of_people = 10
# Create a variable x that is a string 
x = f"There are {types_of_people} types of people."

# Create variables binary and do_not that are strings
binary = "binary"
do_not = "don't"

# Create a string variable that contains variables binary and do_not created before 
y = f"Those who know {binary} and those who {do_not}."

# Print srings x and y to the console 
print(x)
print(y)

# Print the string variables after : of statement 
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Create variable hilarious and set it equal to False 
hilarious = False

# Creates a string variable that includes a location for an additional variable. Creates string within string 
joke_evaluation = "Isn't that joke so funny?! {}"

# Prints the string joke_evalution with the vairbale hilarious after. Creates string within string
print(joke_evaluation.format(hilarious))

# Creates 2 string variables w and e
w = "This is the left side of..."
e = "a string with a right side."

# Adds string variable e to the end of string variable w
print(w + e)
