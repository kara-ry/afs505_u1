# This imports the function argv to get the file name
from sys import argv

script, filename = argv
# This opens the file (that was set to filename above) and creates a file object
txt = open(filename) 

# This inserts the file name into the sentence then prints the object (contents) of the file
print(f"Here's your file {filename}:")
print(txt.read())

# This prints the string followed by a place to input (type) a file name in
# print("Type the filename again:")
# file_again = input("> ")

# This then opens the file you typed in and creats a file object
# txt_again = open(file_again)

# This then prints the contents of the file
# print(txt_again.read())
