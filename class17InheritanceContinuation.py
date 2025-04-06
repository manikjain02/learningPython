# WAP: in a comapany there are 5 staff working,
# Input their name, age, designation are in class 1
# Attendance, basic salary are in class 2
# Print name, age, designation, working days, salary of current month are in class 3


# class Employee:
#     def setInformation(self):
#         global name, age, designation
#         global no
#         na = []
#         ag = []
#         dg = []
#         no = int(input("Enter Number of Employees: "))
#         for i in range(no):
#             n = input("Enter name: ")
#             a = int(input("Enter age: "))
#             d = input("Enter Designation: ")
#             na.append(n)
#             ag.append(a)
#             dg.append(d)
#         name = na
#         age = ag
#         designation = dg


# class Attendance(Employee):
#     def setWorking(self):
#         global attendance, bsalary
#         nd = []
#         sa = []
#         for i in range(no):
#             nwd = int(input("Working Days: "))
#             bsal = int(input("Basic Salary: "))
#             nd.append(nwd)
#             sa.append(bsal)
#         attendance = nd
#         bsalary = sa


# class Final(Attendance):
#     def displayInormation(self):
#         for i in range(no):
#             print("-----------------------------------------------")
#             print("Employee Name: ", name[i])
#             print("Employee Age: ", age[i])
#             print("Employee designation: ", designation[i])
#             print("Basic Salary: ", bsalary[i])
#             print("Total Days: ", attendance[i])
#             nsal = bsalary[i] // 26 * attendance[i]
#             print("Net Salary: ", nsal)
#             print("-----------------------------------------------")


# obj = Final()
# obj.setInformation()
# obj.setWorking()
# obj.displayInormation()


# Multiple Inheritance:
# When we inherit more than one class in a single class


# class A1:
#     def __init__(self):
#         print("Constructor 1")
#         super().__init__()  # to call thee constructor of parent class

#     def oneD(self):
#         print("Hello 1")


# class B1:
#     def __init__(self):
#         print("Constructor 2")

#     def twoD(self):
#         print("Hello 2")


# class C1(A1, B1):
#     def __init__(self):
#         print("Constructor 3")
#         super().__init__()  # to call the constructor of parent class

#     def threeD(self):
#         print("Hello 3")


# obj = C1()
# obj.oneD()
# obj.twoD()
# obj.threeD()
