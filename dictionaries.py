"""Dictionary stores elements in key/value pairs.
KEYS are unique identifiers that are associated with
each VALUE."""

# If we want to store information about countries and their capitals,
# we can create a dictionary with country names as KEYS
# and capitals as VALUES
# Create a dictionary named 'capita_city'
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

"""CHANGE VALUE of DIctionary
We can also use [] to change the value associated with 
a particular key"""
student_id = {111: "Eric", 112: 'Stan', 113: "Butters"}

