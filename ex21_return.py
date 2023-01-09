def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions.")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age},\nHeight: {height},\nWeight: {weight},\nIQ: {iq}")

print('Here is a puzzle')

what = add(age, substract(height, multiply(weight, divide (iq, 2))))
what_2 = age + (height - (weight * (iq / 2)))

print("That becomes: ", what, what_2, "\nCan you do it by hand?")

print('*'*10)
print('Another way to count: simple formula and functions: ')
formula = divide(weight, add(age, multiply(height, 3)))

print(f"Here is a result: {formula}")