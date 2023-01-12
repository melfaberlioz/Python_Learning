"""
WHILE loop will keep executing the code block under it as long
as a boolean expression is True. And when the condition becomes
False, the line immediately after the loop in the program is executed.
"""
# Program to display numbers from 1 to 5

# initialize the variable
i = 1
n = 5

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i += 1
print(" \n ")

# WHILE loop to display game level
current_level = 0
final_level = 5

game_completed = True

while current_level <= final_level:
    if game_completed:
        print('You have passed level', current_level)
        current_level += 1

print("Level Ends \n \n ")


# while loop with ELSE
# The ELSE part is executed after the 'counter' in the
# while loop evaluates to 'False'.
counter = 0

while counter < 3:
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else\n \n ')


# FOR vs WHILE loops
# the FOR loop is usually used when the number of
# iteration is known.

# this loop is iterated 4 times (0 to 3)
for i in range(4):
    print(i)
print(' \n \n')

# and WHILE loop is usually ised when the number of
# iterations are unknown.


# Just an example:
n = int(input(">>> "))
lenght = 0
while n > 0:
    n //= 10
    # this is equivalent to n = n // 10
    lenght += 1
print(lenght)