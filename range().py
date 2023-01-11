"""the 'range()' function returns a sequence of numbers, in a given
range.
*** SYNTAX ***
Syntax: range(start, stop, step)
Parameter:
- start: [optional] start value of the sequence;
- stop: next value after the end value of the sequence;
- step: [optional] int value, denoting the difference
between any two numbers in the sequence."""

# print first 5 integers, using 'range()'
for i in range(5):
    # end = " " даж нам можливість виводити значення в рядок
    # з певним проміжком між цифрами (пробілом). Без цього
    # параметру функція print() дефолтно виведе значення у стовбчик.
    print(i, end = " ")
print()

"""range() allowa user to generate a series of numbers within a given range.

*** RANGE(START,STOP, STEP) ***
The user can choose not only where the series of numbers
will start and stop, but also how big the difference will be 
between one number and the next.
If the user doesn't provide a step, then range() will 
automatically behave as if the step is 1. """
for i in range(0, 10, 2):
    print(i, end = " ")
print()

"""  *** RANGE() USING NEGATIVE STEP ***  
If a user wants to decrement, then the user 
needs steps to be a negative number. """
# збільшити на -2
for i in range(25, 2, -2):
    print(i, end = " ")
print()


"""  *** RANGE() WITH FLOAT ***  
Python range() function doesn’t support the float numbers.
 user cannot use floating-point or non-integer numbers in any of 
 its argument. Users can use only integer numbers. """
# using a float number
for i in range(3.3):
    print(i)