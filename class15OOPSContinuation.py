# Python class have multiple types of object or variables
# 1. Local variables
# 2. Instance variables
# 3. Class or Static variables
# 4. Private variables
# 5. Public or Global variables
# 6. Protected variables (depticated)

# 1. Local variables: Those variables which are declared inside method or scope & cannot be accessed outside the method or scope.


# class Local:
#     def show(self):
#         name = input("Enter your name: ")
#         print("Hello", name)

#     def display(self):
#         print("Good Morning: ", name)


# obj = Local()
# obj.show()
# obj.display()  # NameError: name 'name' is not defined

# Instance Variables: Instance variables is declared with self.variable_name. It can be access throughout the class as well as outside the class also with reference by object. Instance variable are declared with every object. It means, it aquires memory for every object in a separate memory.


# class Instance:
#     def __init__(self, x, y):
#         self.x = x  # Instance variable
#         self.y = y  # Instance variable

#     def show(self):
#         k = self.x + self.y
#         print("Sum of x and y is: ", k)


# obj = Instance(10, 20)
# obj.show()
# print(
#     "x is: ", obj.x
# )  # Accessing instance variable outside the class with reference by object
# print(
#     "y is: ", obj.y
# )  # Accessing instance variable outside the class with reference by object


# 3. Class or Static Variables: Class or Static Variables declared inside class. It can be access by classname.variable_name. Static variable declared only once and all the object share memory of static variable.


# class Manik:
#     x = 10

#     def show(self):
#         self.x = 10
#         self.x += 1
#         print("x is: ", self.x)
#         Manik.x += 1
#         print("Static x is: ", Manik.x)


# obj1 = Manik()
# obj2 = Manik()
# obj3 = Manik()
# obj4 = Manik()
# obj1.show()
# obj2.show()
# obj3.show()
# obj4.show()


# 4. Private Variables: Private variables cannot be accessed outside the class. Private variables are declared with double underscore before variable name. Private may be local or instance both but it can't be accessed outside.


# class privateExample:
#     def show(self):
#         self.__name = "Manik Jain"
#         print("Hello", self.__name)

#     def display(self):
#         print("Good Morning", self.__name)


# obj = privateExample()
# obj.show()
# obj.display()  # AttributeError: 'privateExample' object has no attribute '__name'
# print(obj.__name)  # AttributeError: 'privateExample' object has no attribute '__name'

# Method Overloading: When we have more than one method of same name inside a class then it is known as method overloading. It is not supported in python. But we can achieve it by using default arguments or variable length arguments.


# class Example:
#     def __init__(self):
#         print("Constructor is called")

#     def __init__(self, name):
#         print("Welcome: ", name)


# obj = Example("Manik")

# When there is method overloading then the last method will be executed. It means the first method is overridden by the second method.
