# uses argv to get a filename.
from sys import argv
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")

# call a function on 'txt' named 'read'. What i get
# back from 'open' is a 'file'. You give a file a command
# by using . (dot), the name of the command, and parameters
# just like with 'open' and 'input'.
# txt.read()  says. "Hey, 'txt'! Do your read command with no
# parameters!"
print(txt.read())
txt.close()
print("Your file was successfully closed")

print("Type the filename again: ")

# input потрібен для того, щоб можна було ввести назву
# необхідного фалу повторно.
file_again = input ("> ")

# цією змінною викликаємо повторне відкриття файлу
# за рахунок повторного написання назви файлу.
txt_again = open(file_again)

# Просимо функцію прочитати наш файл і вивести його на екран.
print(txt_again.read())

# function to close the file
txt_again.close()
print("File was closed successfully.")
