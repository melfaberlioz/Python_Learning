# Імпорт функції argv з паку sys
from sys import argv
# Оголошення variables
script, input_file = argv

# define the function 'print_all' with variable as 'f'
def print_all(f):
    # inside the function we define that the file should be
    # read when we call this function ('f' as a variable we
    # mark a file we want to read in the future using this
    # function.
    # empty () let us know that there's no parameters
    # for reading.
    print(f.read())


def rewind(f):
    # 'seek()' is used to change the position of the File Handle
    # to a given specific position. File Handle is like a
    # cursor,w hic defines from where the data has to be read or
    # written in the file.

    # 0 - [default] - argument means absolute file positioning;
    # 1 - sets the reference point at the current file position;
    # 2 - sets the reference point at the end of the file.
    # NOTE: reference point at current position(1)/ end of file(2)
    # cannot be set in text mode except when offset is equal to 0.
    f.seek(0)


# Function with variables 'line-count' & 'f'.
def print_a_line(line_count, f):
    # Function print 'line_count'.
    # .READLINE() is a method that returns one line from the file.
    # You can specified how many bytes from the line to return,
    # by using the size parameter ()

    # Call 'readline()' twice to return both the first and the
    # second line:
    # f = open("demofile.txt, "r")
    #        print(f.readline())
    #        print(f,readline())
    print(line_count, f.readline())


# open 'input_file' from 'current_file'
current_file = open(input_file)

print("First let's print the whole file:\n")
# Call the function 'print_all' that reads our file and displays it.
print_all(current_file)

print("Now let's rewind (перемотати назад), kind of like a tape.")
# Call the function that relocate File Handle in our file
# to the absolute file position.
rewind(current_file)

print("Let's print three lines: ")
# give a variable 'current_file' value.
current_line = 1
# Call the function 'print_a_line' that counts the lines we need
# (variable 'current_line" and returns the first line
# from the 'current_file' (we need to create this text file, by
# the way.
print_a_line(current_line, current_file)

# We form a new valiable using the previous one and add 1 to it's
# kind of default value (we define it in the line 60).
current_line = current_line +1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)