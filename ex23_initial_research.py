import sys
script, input_encoding, error = sys.argv

# defines a function and gives them variables such as
# 'language_file', 'encoding', and 'errors'.
def main(language_file, encoding, errors):
    # the function reads one line from the 'ex23_language.txt' file.
    line = language_file.readline()

    # Using if-statement we test whether 'line' has something
    # in it. The 'readline()' function will return an empty
    # string when it reaches the end of the file and 'if line'
    # simply tests for thins empty string. As long as 'readline'
    # gives us something, this'll be true, and the code under (line 18 -24)
    # will run. When this is false, Python will skip these lines.
    if line:
        # Call a separate function to do the actual printing of this line.
        print_line(line, encoding, errors)
        # Call function 'main' inside 'main'(inside 'main' because 'line' is
        # a part of function 'main' (line 6-8)). Calling this function at the
        # end of itself would jump back to the top and run it again. That
        # would be like a loop.
        # if-statement above keeps this function from looping forever.
        return main(language_file, encoding, errors)


# Defines function which does the actual encoding of each line from the
# 'ex23_language.txt' file.
def print_line(line, encoding, errors):
    # видалення завершального \n у рядку.
    next_lang = line.strip()
    # receive the language from the 'ex23_language.txt' file and 'encode'
    # it into the raw bytes. The 'next_lang' variable is a string, so
    # to get the raw bytes I must call '.encode()' on it to encode strings.
    # I pass to 'encode()' the encoding I want and how to handle errors.
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # Show the inverse of line 36 by creating a 'cooked_string' variable from
    # the 'raw_bytes'.
    # 'raw_bytes' is bytes, so I call '.decode()' on it to get a Python string.
    # This string should be the same as the 'next_lang' variable.
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    # Print lines 36-41 both out to show what they look like
    print(raw_bytes, "<=====>", cooked_string)
#     "raw" bytes it's numerical bytes Python uses to store the
# string.
# These 'raw' bytes are then displayed 'cooked' on the right,
# so you can see the real characters in your terminal.
# You specify this with b'' to tell Python you're working with "raw" bytes.


# i'm done defining functions, so now I want to open the
# 'ex23_language.txt' file.
languages = open('ex23_language.txt', encoding='utf-8')

# Run the 'main' function.
main(languages, input_encoding, error)
