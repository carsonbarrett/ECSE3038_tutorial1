# a. Create a list of dictionaries, where each dictionary represents a person.
people = [
    {"name": "Bob", "age": 35, "city": "Cityville"},
    {"name": "Charlie", "age": 27, "city": "Townsville"},
    {"name": "Diana", "age": 42, "city": "Villagetown"}
]

# b. Print the name of the second person in the list.
# c. Update the age of the third person to 30.
# d. Add a new person to the list.
# e. Print the list after the modifications.

print("Second Person:" , people[1] ["name"])
people[2]["age"] = 30
people.append({"name": "Eve", "age": 25, "city": "Metrocity"})
print("Updated list of people:")
for person in people:
    print(person)

    