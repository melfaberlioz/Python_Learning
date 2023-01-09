# A list is a collection of similar or different types of data.

# A list is created in Python by placing items inside [],
# separated by commas.

# A list with 3 integers
numbers = [1, 2, 5]
print(numbers)


# A list can have any number of items and they may be of
# different types(int, float, string, etc.).

# Empty list
my_list = []

# list with mixed data type
my_list = [1, 'Hello', 3.4]
print(my_list)


# Each item in a list is associated with a number.
# The number is known as a list index.
# We can access elements of an array using the index number
# (0, 1, 2, 3,...). The list index always starts with 0. Hence,
# the first element is presented at index 0, not 1.

languages = ['Python', 'Swift', 'C++']
# access item at index 0
print(languages[0])

# access item at index 2
print(languages[2])
print( )
print( )

print('*' * 20)
print('NEGATIVE INDEXING')
# The index of -1 refers to the last item, -2 to the
# second last item and so on.

languages = ['Python', 'Swift', 'C++']
# access item at index 2
print(languages[-1])

# access item at index 0
print(languages[-3])
print( )
print( )

print('*' * 20)
print('SLICING OF A LIST')
# It's possible to access a section of items from
# the list using the slicing operator ':', not just
# a single item.

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
# items from index 2 to index 4
print(my_list[2:5])

# items from index 5 to end
print(my_list[5:])

# items beginning to end
print(my_list[:])
print( )
print( )

print('*' * 20)
print('ADDING ELEMENTS')
print('Using append ()')
# The append() method adds an item at the end of the list.

numbers = [21, 34, 54, 12]

print('Before Append: ', numbers)

# using append method. We add 32 at the end of the array.
numbers.append(32)

print('After Append: ', numbers)

print('Using extend()')
# We use the extend() method to add all items of one
# list to another.

prime_numbers = [2, 3, 5]
print('List1: ', prime_numbers)

even_numbers = [4, 6, 8]
print('List2: ', even_numbers)

# join two lists
prime_numbers.extend(even_numbers)

print('List after append: ', prime_numbers)
print( )
print( )

print('*' * 20)
print('CHANGE LIST ITEMS')
# We can change items of a list by assigning new values using '=' operator.

languages = ['Python', 'Swift', 'C++']

# changing the third item to 'C'
languages[2] = 'C#'

print(languages)
print( )
print( )

print('*' * 20)
print('REMOVE AN ITEM FROM A LIST')
print("1) Using 'del()'")
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the 2nd item
del languages[2]
print(languages)

# deleting the last item
del languages[-1]
print(languages)

# deleting first two items
del languages[0:2]
print(languages)


print('2) Using remove()')
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# remove 'Python' from the list
languages.remove('Python')

print(languages)
