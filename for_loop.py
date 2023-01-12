"""
the 'for' loop is used to run a block of code for a certsin
number of times. It's used to iterate over any sequences such
as list, tuple, string, etc.
The SYNTAX of the 'for' loop is:
# for val in sequence:
'val' accesses each item of the sequence on each iteration.
Loop continues until we reach the last item in the sequence.
"""

# loop over LIST
languages = ['Swift', 'Python', 'Go', 'JavaScript']
# access items of a list using for loop
for language in languages:
    print(language, end = " ")

print(' \n ')

"""
In the above example, we have created a list called 'languages'.
Initially, the value of 'language' is set to the first element of the
array,i.e. Swift, so the print statement inside the loop is executed.

'language' is updated with the next element of the array and the 
print statement is executed again. This way the loop runs until the 
last element of an array is accessed.
"""

# for-loop with 'range()'.
# we define a range of values:
values = range (4)

# iterate from i = 0 to i = 3:
for i in values:
    print(i)
print(' \n ')



# for-loop with ELSE:
"""The ELSE is executed when the loop is finished."""
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print('No items left.\n \n ')
""" The ELSE block will not execute if the for-loop is stopped by 
a 'break' statement"""


# NESTED for-loop
"""When we have a for-loop inside another for-loop, 
it's called a nested for-loop."""
words = ['Apple', 'Banana', 'Car']
for word in words:
    print('The following lobes will print each letters of ' + word)
    for letter in word:
        print(letter)
    print(' \n ')

# BREAK statement with for loop
"""The BREAK statement is used to exit the for loop prematurely.
It's used to break the for loop when a specific condition is met.

Let’s say we have a list of numbers and we want to check if a number 
is present or not. We can iterate over the list of numbers and 
if the number is found, break out of the loop because we don’t need
to keep iterating over the remaining elements.
"""
nums = [1, 2, 3, 4, 5, 6]
n = 2

found = False
for num in nums:
    if n == num:
        found = True
        break

print(f'List contains {n}: {found}')
print(" \n ")

# The CONTINUE statement with for loop
"""We can use CONTINUE statements inside a for loop
to skip the execution of the for loop bode for a specific
condition.

Let’s say we have a list of numbers and we want to print
the sum of positive numbers. We can use the continue 
statements to skip the for loop for negative numbers.
"""
nums = [1, 2, -3, 4, -5, 6]
sum_positives = 0

for num in nums:
    if num < 0:
        continue
    sum_positives += num

print(f'Sum of Positive Numbers: {sum_positives} \n \n ')