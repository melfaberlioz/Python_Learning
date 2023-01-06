# If you don't know how many arguments that'll be
# passed into your function, add "*" before the parameter
# name in the function definition.

def my_function(*kids):
    print("The youngest child is " + kids[2])
#     The value in [] define on which place the youngest brother is.
# So, [0] is Email, [1] is Tobias, [2] is Linus. If we give
# the number bigger than people we write, we'll have Error.


my_function("Email", "Tobias", "Linus")