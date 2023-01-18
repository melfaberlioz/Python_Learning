"""Dictionary stores elements in key/value pairs.
KEYS are unique identifiers that are associated with
each VALUE."""

# If we want to store information about countries and their capitals,
# we can create a dictionary with country names as KEYS
# and capitals as VALUES
# Create a dictionary named 'capital_city'
capital_city = {
    "Nepal": "Kathmandu",
    "Italy": "Rome",
    "England": "London"
}
# NB: keys and values both are of string type.
# We can also have it of different data types.
print(capital_city)

print(' \n **** **** **** \n ')

# dictionary with keys and values of different data type.
numbers = {
    1: 'One',
    2: 'Two',
    3: "Three"
}
print(numbers)

print(' \n **** **** **** \n ')

""" ADD ELEMENTS to a dictionary
We can add elements to a dictionary using the name of 
the dictionary with [] """
capital_city = {
    "Nepal": "Kathmandu",
    "Italy": "Rome",
    "England": "London"
}
print("Initial Dictionary: ", capital_city)

# add new value and key to created dictionary
capital_city['Japan'] = 'Tokyo'

print('Updated Dictionary: ', capital_city)

print(' \n **** **** **** \n ')

"""CHANGE VALUE of Dictionary
We can also use [] to change the value associated with 
a particular key"""
student_id = {111: "Eric", 112: 'Kyle', 113: "Butters"}
print('Initial Dictionary: ', student_id)

#change the value of the key [112]
student_id[112] = 'Stan'

print('Updated Dictionary: ', student_id)

print(' \n **** **** **** \n ')

"""ACCESSING ELEMENTS form Dictionary
We use the keys to access their corresponding values."""
# print Eric
print(student_id[111])
# print Butter
print(student_id[113])

print(' \n **** **** **** \n ')

"""REMOVING ELEMENTS
we use del statement to remove an element form the dictionary"""
print("Initial Dictionary: ", student_id)

del student_id[111]

print('Updated Dictionary: ', student_id)

print(' \n **** **** **** \n ')

"""DICTIONARY MEMBERSHIP TEST
We can test if a key is in a dictionary or not using the keyword
in.
MEMBERSHIP TEST IS ONLY FOR THE KEYS AND NOT FOR THE VALUES!"""
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: True
print(1 in squares)
print(2 not in squares)

print(' \n **** **** **** \n ')

"""ITERATING Though a Dictionary
we can iterate through each key in a dictionary using a for loop"""
for i in squares:
    print(squares[i])
# we have iterated through each key in the 'squares' dictionary
# using the for loop

print(' \n **** **** **** \n ')

"""BUILT-IN FUNCTION dict()
Dictionary can also be created be the built-in function 'dict()'.
An empty dictionary can be created by just placing to curly braces {}."""
# Creating an empty Dictionary
Dict = { }
print('Empty Dictionary: ', Dict)

# Creating Dictionary with 'dict()' method
Dict = dict({1: 'Greek', 2: ' For', 3: 'Greeks'})
print('\nDictionary with the use of dict():', Dict)

print(' \n **** **** **** \n ')

"""NESTED DICTIONARY"""
Dict = {1: 'Greek', 2: ' For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Greeks'}}
print(Dict)