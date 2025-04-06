# For handling single exception

# class Abc:
#     def calculate(self, x, y):
#         try:
#             k = x / y
#             print(k)
#         except ZeroDivisionError as e:
#             print(e)


# ob = Abc()
# ob.calculate(20, 3)
# ob.calculate(20, 0)
# print("Show must go on")

# For handling multiple exception


# class Abc:
#     def show(self):
#         names = ["Madhuri Yadav", "Manik Jain", "Yogita Yadav", "Madnik"]
#         try:
#             # k = 10 / 2
#             k = 10 / 0
#             print(k)
#             for name in range(5):
#                 print(names[name])
#         # except (ZeroDivisionError, IndexError) as e:
#         except Exception as e:
#             print(e)


# ob = Abc()
# ob.show()

# Use of finally


# class Abc:
#     def show(self):
#         names = ["Madhuri Yadav", "Manik Jain", "Yogita Yadav", "Madnik"]
#         try:
#             # k = 10 / 2
#             k = 10 / 0
#             print(k)
#             for name in range(5):
#                 print(names[name])
#         # except (ZeroDivisionError, IndexError) as e:
#         except Exception as e:
#             print(e)
#         finally:
#             print("Must execute this line")


# ob = Abc()
# ob.show()

# User defined exceptions


# class MyException(Exception):
#     def __init__(self, age, message="Age must be between 18 and 60"):
#         self.age = age
#         self.message = message
#         super().__init__(self.message)

#     def __str__(self):
#         return f"{self.message}. Provided age: {self.age}"


# class Demo:
#     def set_age(self, age):
#         if age < 18 or age > 60:
#             raise MyException(age)
#         print(f"Age is set to {age}")

#     def show(self):
#         try:
#             self.set_age(17)
#         except MyException as e:
#             print(f"Invalid age: {e.age}. {e.message}")


# ob = Demo()
# ob.show()
