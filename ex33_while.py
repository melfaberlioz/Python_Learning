i = 0
# create an empty list
numbers = []
# create a variable for while loop, using input
n = int(input('>>> '))


# convert while loop to a function
def sth(i, numbers):
    while i < n:
        print(f"At the top i is {i}")
        # adding to the empty list a new number (i)
        numbers.append(i)

        i += 2
        print("Number now: ", numbers)
        print(f"At the bottom i is {i}")


sth(i, numbers)

print("The numbers: ")

for num in numbers:
     print(num)
