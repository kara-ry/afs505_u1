name = 'Zed A. Shaw'
age = 35
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

heightcm = height * 2.54
weightinkg = weight * 0.453592

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

print(f"He's {heightcm} cm tall.")
print(f"He's {weightinkg} kg heavy.")

# This line is tricky, try to get it exactly right 
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
