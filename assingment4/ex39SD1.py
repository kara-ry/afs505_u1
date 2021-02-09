# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Washington': 'WA',
    'California': 'CA',
    'Idaho': 'ID',
    'Montana': 'MT'
}

# create a basic set of states and some cities in them 
cities = {
    'CA': 'San Francisco',
    'OR': 'Portland',
    'WA': 'Pullman'
}

# add some more cities 
cities['ID'] = 'Moscow'
cities['MT'] = 'Missoula'

# print out some cities 
print('-' * 10)
print("WA State has: ", cities['WA'])
print("OR State has; ", cities['OR'])

# print some states
print('-' * 10)
print("Washington has: ", cities[states['Washington']])
print("Montana has: ", cities[states['Montana']])

# print every state abbreviation 
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state 
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time 
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}") 




