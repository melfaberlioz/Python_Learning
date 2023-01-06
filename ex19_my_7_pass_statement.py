# 'function' definitions cannot be empty, but if you
# for some reason have a 'function definition with no content,
# put in the 'pass' statement to avois getting an error

def myfunction():
    pass


# Recursion
# is a common mathematical concept where a function calls itself.
# The benefit of meaning that you can loop through data to reach a result.

# Program to print the fibonacci series up to k_terms.

# Recursive function
def recursive_fibonacci(k):
    if k <= 1:
        return k
    else:
        return(recursive_fibonacci(k-1) + recursive_fibonacci(k-2))


k_terms = 10

# Check if the number of item is valid
if k_terms <= 0:
    print("Invalid input! Please input a positive value.")
else:
    print("Fibonacci series: ")
for i in range(k_terms):
    print(recursive_fibonacci(i))



# 'def' with 'input'
# Task:
# Define a function smaller_num that takes in two
# numbers to determine and return the smaller number of the two.
def smaller_num(x, y):
    if x > y:
        # Here we use 'return' to assigne the value to a variable,
        # so when we 'return' something from a function, we have
        # something to use in 'result' on 51 line.
        return y
    else:
        return x


x = input("Enter first number: ")
y = input("Enter second number: ")
result = smaller_num(x,y)
print('The smaller number between ' + str(x) + ' and '
      + str(y) + ' is ' + str(result))
