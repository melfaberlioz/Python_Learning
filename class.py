"""A CLASS is a user-defined blueprint or prototype
from which objects are created. Classes provide a means of
bundling (пакування) data and functionality together.
 Creating a new class creates a new type of object,
allowing instances (екземпляри) of that type to be made.

*************************

Class creates a user-defined datat structure, which holds its own
data members and member functions, which can be accessed and used
by creating an instance of that class.

**************************
CLASS OBJECTS

An OBJECTS are an instance of a CLASS. A class is like a blueprint
while an instance is a copy of the class with actual values.

***************************
An OBJECT CONSISTS OF:
- STATE: It's represented by the attributes of an object.
- BEHAVIOUR: Represented by the method of an object.
- IDENTITY: Gives a unique name to an object and enables one object
to interact with other objects.

** All the instances share the attributes and the behaviour of the
class. But the values of those attributes, i.e. the state are unique
for each object. A single class may have any number of instance.

"""

# Demonstrate instantiating a class


class Dog:
    # A simple class attribute
    attr1 = 'mammal'
    attr2 = 'dog'
    attr3 = 'Rodger'
    attr4 = 'cat'
    attr5 = 'Bary'

    # a sample method
    # creating a FUNCTION for class Dog
    def fun(self):
        print('I\'m a', self.attr1)
        print('I\'m a', self.attr2)
        print('I\'m a', self.attr3)
        print(" ", end=' \n  \n')

    def play(self):
        print('I\'m a', self.attr1)
        print('I\'m a', self.attr4)
        print('I\'m a', self.attr5)
        print(" ", end=' \n')


# Driver code
# Object instantiation
Rodger = Dog()
Bary = Dog()

# Accessing class attributes and method through objects
Rodger.fun()
Bary.play()

print('*' * 12)

# PYTHON OBJECTS
# An object is called an instance of a class.
# 'Bike' is a class then we can create objects like
# 'bike1' and 'bike2' from the class.

# create class
print(" ", end=' \n')


class Bike:
    name = ''
    gear = 0

# Create objects of class


bike1 = Bike()
# 'bike1' is the object of the class. Now, we can use this object
# to access the class attributes.
# We can use the . to access the attributes of a class.

# modify the name attribute
bike1.name = 'Mountain Bike'
# access the gear attribute
bike1.gear = 11
# Here, we have used 'bike1.name' and 'bike1.gear' to change
# and access the value of 'name' and 'gear' attribute.

print(f'Name: {bike1.name}, Gear: {bike1.gear}')
print(" ", end=' \n')
print('*' * 12)
print(" ", end=' \n')

# CREATING MULTIPLE OBJECTS OF CLASS
# define a class


class Employee:
    # define an attribute
    employee_id = 0

# create two objects of the Employee class


employee1 = Employee()
employee2 = Employee()

# access attributes using employee1
employee1.employeeID = 1001
print(f'Employee ID: {employee1.employeeID}')

# access attributes using employee2
employee2.employeeID = 1002
print(f'Employee ID: {employee2.employeeID}')

print(" ", end=' \n')
print('*' * 12)
print(" ", end=' \n')


class Cat:
    cat_weight = 0
    cat_age = 0


cat1 = Cat()
cat2 = Cat()

# access attributes
cat1.weight = 5
cat1.age = 4
print(f'Cat\'s weight is {cat1.weight} kg, and cat is {cat1.age} y.o.')

cat2.weight = 10
cat2.age = 9
print(f'Cat\'s weight is {cat2.weight} kg, and cat is {cat2.age} y.o.')
print(" ", end=' \n')
print('*' * 12)
print(" ", end=' \n')

# METHODS
# we can also define a function inside a Python class. A Python
# FUNCTION defined inside a class is called a METHOD.

# create a class


class Room:
    length = 0.0
    breadth = 0.0

    # create a function as a method to calculate ares
    def calc_area(self):
        # display string and the multiplication of length and breadth
        print('Area of room = ', self.length * self.breadth)

# create object of Room class


study_room = Room()
# assign values to all the attributes
study_room.length = 42.5
study_room.breadth = 30.8

# access method inside class
study_room.calc_area()
print(f'Cat\'s weight is {cat2.weight} kg, and cat is {cat2.age} y.o.')
print(" ", end=' \n')
print('*' * 12)
print(" ", end=' \n')


class Bedroom:
    wide = 0.0
    long = 0.0

    def area_bedroom(self):
        print('There\' s the are of the bedroom: ', self.long * self.wide)


bedroom1 = Bedroom()
bedroom2 = Bedroom()

bedroom1.long = 34.7
bedroom1.wide = 20.0

bedroom2.long = 45.6
bedroom2.wide = 34.5

bedroom1.area_bedroom()
bedroom2.area_bedroom()
print(" ", end=' \n')
print('*' * 12)
print(" ", end=' \n')

# CONSTRUCTOR
# Class constructor is the first piece of code to be executed when
# you create a new object of a class.
# The constructor can be used to put values in the member variables.
class Bike:
    # we can aso initialize values using the constructors
    # constructor function
    # '__init__()' is the constructor function that is called
    # whenever a new object of that class is instantiated.
    # The first parameter 'self' passes a reference to the instance of
    # the class itself.It's possible to add additional parameters. It
    # sends when a new object is to be created.
    def __init__(self, name = ""):
        # constructor above initializes the value of the 'name'
        # attribute.we have used the 'self.name' to refer to
        # the 'name' attribute of the 'bike1' object.
        self.name = name


bike1 = Bike('Mountain Bike')
# 'Mountain Bike' is passed to the 'name' parameter of '__init__()'
