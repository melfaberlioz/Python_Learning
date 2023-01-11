people = 30
cars = 700
trucks = 50

""" 
The 'if' statement lets yo run a block of code only if a certain condition
is met.
The 'elif' statement lets you run a block of code only if another
condition is met.
The 'else' statement lets you run a block of code only if no other
condition is met."""

# Створюємо алгоритм.
# Умова буде виконуватися, або коли машин більше за людей, або
# коли машин більше за вантажівок.
if cars > people or cars > trucks:
    print("We should take the cars.")
# If the previous statement was wrong, then this condition will be executed:
# only if cars < people.
elif cars < people:
    print('We should not take the cars.')
# If previous statements are wrong, then this last statement will
# be executed.
else:
    print("We can't decide.")

if trucks > cars:
    print('That\'s too many trucks.')
elif trucks < cars:
    print('Maybe we could take the trucks.')
else:
    print('We still can\'t decide.')

if people < trucks and cars >= people:
    print('Alright, let\'s just take the trucks.')
else:
    print('Fine, let\'s stay home.')
