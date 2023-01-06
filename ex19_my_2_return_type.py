# define function.
# 'a' is a variable we use to have result.
def find_square(a):
    # пишемо саму функцію. ** означає піднесення до 2 степеня.
    result = a ** 2
    # A Python function may or may not return a value.
    # If we want our function to return some value to a function call,
    # we use the 'return' statement.
    # Here, we are returning the variable 'result' to the function call.
    return result
# The 'return' statement also denotes that the function has ended.
# Any code after return is not executed.

# Виклик функції
square = find_square(3)

# Виведення на екран обчислене значення 'square'.
# The same as print(f"Square: {square}")
print('Square: ', square)