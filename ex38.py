# Create a variable named 'ten_things'
ten_things = 'Apples Oranges Crows Telephone Light Sugar'

print('Wait there are not 10 things in that list. Let\'s fix that.')

# create variable to split the 'ten_things' with (' ')
stuff = ten_things.split(' ')
# Create list named 'more_stuff'
more_stuff = ['Day', 'Nights', 'Song', 'Frisbee',
              'Corn', 'Banana', 'Girl', 'Boy']

# while loop where we say that length of the splited variable
# 'stuff' isn't equal to 10
while len(stuff) != 10:
    # new variable where we remove an item from the list 'more_stuff'
    # using pop() method
    next_one = more_stuff.pop()
    print('Adding: ', next_one)
    # here we add things "from next_one" to the 'stuff' using
    # append() function
    stuff.append(next_one)
    # here we print out the result of our loop
    print(f"There are {len(stuff)} items now.")

print('There we go: ', stuff)

print("Let's do some more things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(" ".join(stuff))
print('#'.join(stuff[3:5]))