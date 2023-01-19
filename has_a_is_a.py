"""HAS-A
Be using the class names or by creating an object we can
access the member of one class inside another class.
A class that references to one or more objects of other classes
as an Instance variable.
"""


class Engine:
    # engine specific functionality
    ...
    ...


class Car:
    e = Engine()
    e.method1()
    e.method2()
    ...
    ...
# class Car has-a Engine class reference

# **** **** **** ****

class Employee:

    # constructor for initialization
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    # this function make our new instances do sth.
    # and here it's an algorithm. So this future class
    # will print all this information we write below.
    def emp_data(self):
        print('Name of Employee: ', self.name)
        print('Age of Employee: ', self.age)


# new class, where we initiate address, salary and create
# an empty object for Employee class to use it here.
class Data:
    # In this class we have has-a relationship? because
    # here is an object 'self.emp_obj' as an Employee class
    # but recreated to object.
    def __init__(self, address, salary, emp_obj):
        self.address - address
        self.salary = salary

        # creating object of Employee class
        # We are creating objects inside the constructor
        # so whenever we'll call any method or variable
        # of class 'Employee' we must use self keyword.
        # We can replace "self.emp_obj" to "Employee", but
        # by using the class name Employee we can access
        # only that static method or variable of the Employee class.
        self.emp_obj

    # instance method new instances will use to do sth.
    def display(self):

        # calling Employee class(as 'emp_obj') using emp_data() method
        self.emp_obj.emp.data()
        print('Address of Employee: ', self.address)
        print('Salary of Employee: ', self.salary)


# creating Employee class object to присвоїти нове значення
# до об'єкту, використовуючи клас Employee as a blueprint.
emp = Employee('Ronil', 20)

# passing obj. of Emp. class during creation of Data class object
data = Data('Indore', 25000, emp)

# call Data class instance method
data.display()

# **** **** **** ****


class A:
    # initialization of new objects
    def __init__(self):
        print('Class - A Constructor')

    # creating a function for this new objects
    def m1(self):
        print('M1 method of class - A.')


class B:
    # has-a relationship, bc here we create object
    # of class A inside the class B and calling inside
    # this function a function from class A -- m1
    def __init_(self):
        print('Class - B Constructor.')

    # instance method
    def m2(self):

        # creating object of class A inside
        # B class instance method
        obj = A()

        # calling m1() method of class-A
        obj.m1()
        print("M2 method of Class - B.")


# creating object of class-B
obj = B()

# calling B class m2() method
obj.m2()


# **** **** **** ****

"""IS-A 
(Inheritance)
Inheritance is a mechanism that allows us to
inherit all the properties from another class.
The class from which the properties and functionalities 
are utilized is called the PARENT CLASS (or Base Class).
The class which uses the properties from another class
is called as CHILD CLASS (oe Deriver Class). 
"""


# Parent class
class Parent:

    # parent class method
    def m1(self):
        print('Parent Class Method called...')


# child class inheriting parent class
class Child(Parent):

    # child class constructor
    def __init__(self):
        print('Child Class object created...')

    # child class method
    def m2(self):
        print('Child Class Method called...')


# creating object of child class
obj = Child()

# calling parent class m1() method
obj.m1()

# calling child class m2() method
obj.m2()



