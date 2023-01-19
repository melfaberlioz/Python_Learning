# Animal is-a object
# 'object' is a class
class Animal(object):
    pass


# Dog has-a object, bc class Animal is Child class
# since it has the name of another class in () -- (object)
# Child class
class Dog(Animal):

    def __init__(self, name):
        # ?
        self.name = name


# has-a relationship
class Cat(Animal):

    def __init__(self, name):
        # ?
        self.name = name


# is-a object since it has class named 'object in ()
class Person(object):

    def __init__(self, name):
        # ?
        self.name = name

        # person has-a pet of some kind
        self.pet = None


# has-a relationship
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary


# is-a object
class Fish(object):
    pass


# has-a object
class Salmon(Fish):
    pass


# has-a object
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog('Rover')

satan = Cat('Satan')

mary = Person('Mary')

# is-a
mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()