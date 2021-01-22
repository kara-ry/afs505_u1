
# Creates a string variable with 4 locations to insert word, numbers, etc. into 
formatter = "{} {} {} {}"

# These add various things to the empty locations in the formatter string
print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
))
	
