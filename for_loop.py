"""
the 'for' loop is used to run a block of code for a certsin
number of times. It's used to iterate over any sequences such
as list, tuple, string, etc.
The SYNTAX of the 'for' loop is:
# for val in sequence:
'val' accesses each item of the sequence on each iteration.
Loop continues until we reach the last item in the sequence.
"""

# loop ove LIST
languages = ['Swift', 'Python', 'Go', 'JavaScript']
# access items of a list using for loop
for language in languages:
    print(language, end = " ")
"""
In the above example, we have created a list called 'languages'.
Initially, the value of 'language' is set to the first element of the
array,i.e. Swift, so the print statement inside the loop is executed.

'language' is updated with the next element of the array and the 
print statement is executed again. This way the loop runs until the 
last element of an array is accessed.
"""
