# Hybrid Inheritance
# Mixture of inheritance is known as Hybrid inheritance


# class CEO:
#     def ceoMethod(self):
#         print("Hello I am the CEO")


# class Manager(CEO):
#     def managerMethod(self):
#         print("Hello I am the Manager")


# class Employee1(Manager):
#     def employee1Method(self):
#         print("Hi I am Madhuri Yadav")


# class Employee2(Employee1, CEO):
#     def employee2Method(self):
#         print("Hi I am Manik Jain")


# obj = Employee2()
# obj.managerMethod()
# obj.ceoMethod()
# obj.employee2Method()
# obj.employee1Method()


# Encapsulation
# Hiding the methods and properties


# class Employee:
#     def __init__(self):
#         self.__name = "Madhuri"

#     def setName(self, name):
#         print("Name value are assigned")
#         self.__name = name

#     def getName(self):
#         print("Name value are returned")
#         return self.__name

#     pname = property(getName, setName)


# emp = Employee()
# emp.pname = "Maddhuri Yadav"
# print(emp.pname)


# Abstraction
# Partial implementation of method, it means it is only declared not defined. Whenever we can inherit abstract class then it is mandatory to define abstract method.
# Abstract method cannot instantiated, it means we cannot create object.
# We have a module named abc

# from abc import ABC, abstractmethod


# class AbstractMethod(ABC):
#     @abstractmethod
#     def add(self):
#         pass

#     @abstractmethod
#     def greet(self, name):
#         pass

#     def display(self):
#         print("Hiii")


# class Demo(AbstractMethod):
#     def add(self):
#         print("Now I am not abstracted")

#     def greet(self, name):
#         print("Welcome", name)

#     def show(self):
#         print("Madhuri is the best")


# ob = Demo()
# ob.add()
# ob.display()
# ob.show()
# ob.greet("Manik Jain")


# Exception Handling
# Exception is abnormal condition that occurs during execution of program


# class abc:
#     def division(self):
#         k = 10 / 0
#         print(k)


# on = abc()
# on.division()
