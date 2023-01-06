# The purpose of the functions:
# - They name pieces of code the way variables
# name stings and numbers;
# - They take arguments the way your script take 'argv';

# 'def' for "define" = creates a function.
# 'print_two' - give the function a name.
# '*args' - tell that we want *args, which is a lot
# like 'argv' parameter but for functions (and we can skip it (like in 'print_two_again')).
# The second line unpacks the arguments.

# * in '*args' tells Python to take all the arguments to the function and then
# put them in 'args' as a list.
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_one(arg1):
    print(f"arg1: {arg1}")


def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again('Zed', 'Shaw')
print_one('First!')
print_none()