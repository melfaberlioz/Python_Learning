#If we call the function without argument,
# it uses default value.

def my_function(country = "Norway"):
    print('I am from ' + country)

my_function("Sweden")
my_function('India')
# Here we have no value, so it will be executed using
# default value "Norway".
my_function()
my_function('Brazil')