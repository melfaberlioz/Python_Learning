# Animal is-a object
class Animal(object):
    pass


# Dog is-a object (we can access the member of jne class inside
# another -- ('Animal') --
# Child class
class Dog(Animal):

    def __init__(self, name):
        # has-a object
        self.name = name


# is-a relationship
# Child class
class Cat(Animal):

    def __init__(self, name):
        # ?
        self.name = name


class Person(object):

    def __init__(self, name):
        # ?
        self.name = name

        # person has-a pet of some kind
        self.pet = None


# is-a relationship
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary


# is-a object
class Fish(object):
    pass


# is-a object
class Salmon(Fish):
    pass


# is-a object
class Halibut(Fish):
    pass


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