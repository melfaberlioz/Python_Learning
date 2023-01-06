# ex13_parameners_unpacking_variables.py
from sys import argv
script, first, second, third = argv

print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)

# Таким чином, використовуючи input i argv ми змогли розширити
# можливості і отримати інпут від користувача. Єдине питання виникає в тому,
# чому аргументів лишається 3, коли рядків 4, і воно не видає помилку
# надання невірної кількості значень.
input("Your fourth variable is... ")

