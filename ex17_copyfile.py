from sys import argv
# 'exists' returns 'True' if a file exist, based on its name in a string as an argument.
# It returns 'False' if not.
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

in_file = open(from_file)

# 'indata' is a variable through which we can count
# bytes in 'in_file'. 'in_file' is the same as 'from_file'
# so the file, from which we'll make a copy, so it's an 'ex17_text.txt'
indata = in_file.read()
# if we get rid of '.read()' in the previous line, the code
# isn't executed, so it's an important part - to read file
# to let the program know how many bytes it consists.

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# 'w' is a string
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

# It's important to close the file due to the following
# reasons:
# - The file won't be auto closed. It performs a garbage
# collecting.
# - It can slow down the program. More space's crammed with open things.
#
out_file.close()
in_file.close()