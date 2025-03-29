# kwargs
# def show(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# show(name="John", age=30, city="New York")


# def display(name, **age):
#     print("Name:", name)
#     for key, value in age.items():
#         print(f"{key}: {value}")


# display("Manik", n1=25, n2=30, n3=35)


# def display(*no, **name):
#     t = 0
#     for x in no:
#         t = t + x
#     print("Total:", t)
#     for key, value in name.items():
#         print(f"{key}: {value}")


# display(10, 20, 30, n1="John", n2="Doe", n3="Smith")

# Recursive function
# Recursion is a process in which a function calls itself directly or indirectly
# The function that calls itself is called a recursive function
# The recursion continues until a base condition is met
# The base condition is the condition that stops the recursion
# The base condition is also called the terminating condition


# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)


# print("Factorial of 5 is", fact(5))


# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(10))  # Output: 55

# Closure function
# A closure is a function that remembers the values of the variables in its enclosing lexical scope even if they are not present in memory
# A closure is a nested function that has access to the variables in its enclosing scope even after the outer function has finished executing


# def fun(name):
#     def show(age):
#         print(f"Name: {name}, Age: {age}")

#     return show


# # The outer function returns the inner function
# # The inner function is a closure
# # The inner function has access to the variables in the outer function
# # The outer function is called first, the inner function is called later

# b1 = fun("Manik")
# b1(25)
