
## The lines below will create variables and set a value
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90 

## The lines below will do math with the variables created and create new variables

cars_not_driven = cars - drivers 
cars_driven = drivers 
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven 

## The lines below will print the values calcuated within a sentence explaining the value

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
