# Inheritance:
# - Inheritance is a way to form new classes using classes that have already been defined.
# - The new class is called the derived class or child class.
# - The class from which it inherits is called the base class or parent class.
# - The derived class inherits all the attributes and methods of the base class.
# - The derived class can also have additional attributes and methods.
# Python Supports 4 Types of Inheritance:
# 1. Single Inheritance: A derived class inherits from a single base class.
# 2. Multiple Inheritance: A derived class inherits from multiple base classes.
# 3. Multilevel Inheritance: A derived class inherits from a base class, which in turn inherits from another base class.
# 4. Hybrid Inheritance: Multiple derived classes inherit from a single base class.


# Single Inheritance
# class Parent:
#     def showParent(self):
#         print("This is the Parent class")
#         self.name = "Manik Jain"


# class Child(Parent):
#     def display(self):
#         print("This is the Child class")
#         print("Name:", self.name)

#     def show(self):
#         print("Good Morning")


# obj = Child()
# obj.showParent()
# obj.show()
# obj.display()


# MultiLevel Inheritance
# class A:
#     def __init__(self):
#         print("Class A Constructor")

#     def add(self, x, y):
#         k = x + y
#         return k


# class B(A):
#     def __init__(self):
#         print("Class B Constructor")
#         super().__init__()  # Call the constructor of the parent class

#     def sub(self, x, y):
#         k = x - y
#         return k


# class C(B):
#     def __init__(self):
#         print("Class C Constructor")
#         super().__init__()  # Call the constructor of the parent class

#     def mul(self, x, y):
#         k = x * y
#         return k


# obj = C()
# print(obj.add(10, 20))
# print(obj.sub(20, 10))
# print(obj.mul(10, 20))


# Global Variable
# Global variables are not declared & assigned, only give them name by global keyword. It can access anywhere in the class as well as inherited.


# class Student:
#     def getAdmission(self):
#         global name, age
#         name = input("Enter Student Name: ")
#         age = int(input("Enter Student Age: "))


# class Attendance(Student):
#     def showData(self):
#         print("Student Name:", name)
#         print("Student Age:", age)


# obj = Attendance()
# obj.getAdmission()
# obj.showData()
