# OOPS: Object Oriented Programming System
# There are five pillars of OOPS:
# 1. class
# 2. object
# 3. Polymorphism
# 4. Encapsulation
# 5. Inheritance
# python is a pure object oriented programming language. That means it has classes and objects.
# class is a blueprint of an object. Class is a definition of an object. Class does not have any memory & we cannot see and feel the real things.
# Object is a real world entity. Object has state and behavior. Object has memory. Object is an instance of a class.
# Polymorphism: poly: more than one, morphism: functionality. Polymorphism means more than one functionality. Polymorphism is a feature of OOPS that allows us to use the same name for different functions. It is a way to perform a single action in different forms.
# Polymorphism are further divided into two types:
# 1. Overloading: Also known as early binding or compile time polymorphism. It is a feature of OOPS that allows us to use the same name for different functions with different number of arguments or different types of arguments. It is done at compile time.
# 2. Overriding: Also known as late binding or run time polymorphism. In case of inheritance, when parent class & child class both have same signature & arguement, then it is called overriding.

# self: self is a reference to the current instance of the class. It is used to access variables that belong to the class. It is used to access the attributes and methods of the class in python. It is a convention to use self as the first parameter of the method. It is not a keyword in python. We can use any name instead of self but it is a convention to use self.


# class Abc:
#     def show(self):
#         print("Hello from Abc class")


# obj = Abc()  # object creation
# obj.show()  # calling method of class Abc

# Constructor: Constructor is a special method that is automatically called when an object is created. Constructor is used to initialize the attributes of the class. Constructor has same name as class name. Constructor does not have any return type. Constructor is used to create an object of the class. Constructor is used to initialize the attributes of the class. Constructor is used to allocate memory for the object. Constructor is used to set default values for the attributes of the class. Constructor is used to set initial values for the attributes of the class.

# There are 3 types of constructors:
# 1. Default Constructor
# 2. Argumented Constructor / Parameterized Constructor
# 3. Zero Argument Constructor / Non Parameterized Constructor

# Destructor: Is used to destroy the memory which are allocated for the object.


# class Animal:
#     def __init__(self):
#         print("Hello from constructor of Animal class")

#     def show(self, name):
#         print("Welcome: ", name)


# obj = Animal()  # object creation
# obj.show("Tiger")  # calling method of class Animal


# class Human:
#     def __init__(self, name):
#         print("Welcome: ", name)

#     def add(self, a, b):
#         print("Total", a + b)


# hu = Human("Manik")
# hu.add(10, 20)


# class Human:
#     def __init__(self, name):
#         print("Welcome: ", name)

#     def add(self, a, b):
#         print("Total", a + b)

#     def __del__(self):
#         print("Destructor called")


# hu = Human("Manik")
# hu.add(10, 20)
