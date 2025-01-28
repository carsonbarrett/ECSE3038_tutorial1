# Given the following dictionary representing a person:
person = {
    "name": "Alice",
    "age": 28,
    "city": "Wonderland"
}

# a. Print the persons name
# b. Add a new key-value pair to represent the person's
#     occupation (e.g "engineer").
# c. Update the person's age to 29.
# Remove the "city" key from the dictionary.
# e. Print the keys of the modified dictionary.

print(person["name"])
person["occupation"] = "Dj"
person["age"] = "30"
del person["city"]
print(person)
