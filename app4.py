# Lists to store results
squares = [] 
even_numbers = []
upper_case_names = []

# a. Append the squares of numbers from 1 to 5 using a for loop.
for num in range(1, 6):
    squares.append(num ** 2)

# b. Append the even numbers from 2 to 10 (inclusive) using a for loop.
for num in range(2, 11, 2):
    even_numbers.append(num)

# Given list of people from Exercise 3
people = [
    {"name": "Bob", "age": 35, "city": "Cityville"},
    {"name": "Charlie", "age": 27, "city": "Townsville"},
    {"name": "Diana", "age": 30, "city": "Villagetown"},
    {"name": "Eve", "age": 25, "city": "Metrocity"}
]

# c. Create a list of names in uppercase from the list of people.
for person in people:
    upper_case_names.append(person["name"].upper())

# Print the results
print("Squares:", squares)
print("Even Numbers:", even_numbers)
print("Upper Case Names:", upper_case_names)
