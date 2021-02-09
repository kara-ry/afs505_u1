all_numbers = []
i= 0
def number_formula(i, number):
    if i < number:
          print(f"At the top i is {i}")
          all_numbers.append(i)
          print("Numbers now: ", all_numbers)
          i=i+1
          print(f"At the bottom i is {i}")
          return number_formula(i, number)
given_number = 6
list_of_numbers = number_formula(i, given_number)
print("The numbers:", all_numbers)
