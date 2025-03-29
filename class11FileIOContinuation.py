# Write a program to write, read and search a name from a file.

# import os

# os.chdir("./Files")


# def enterRecord():
#     file = open("record1.txt", "a+")
#     name = input("Enter Name: ") + "\n"
#     file.write(name)
#     file.close()


# def showRecord():
#     file = open("record1.txt", "r")
#     fileData = file.readlines()
#     for xName in fileData:
#         print(xName, end="")
#     file.close()


# def searchRecord(data):
#     flag = 0
#     file = open("record1.txt")
#     fileData = file.readlines()
#     for xName in fileData:
#         if xName == data:
#             print("Name Found: ", xName)
#             flag = 1
#     if flag == 0:
#         print("Name not found")


# ans = "y"
# while ans == "y":
#     print("1. Save data")
#     print("2. Show data")
#     print("3. Search Data")
#     print("4. Exit")
#     ch = int(input("Enter your choice 1...4: "))
#     if ch == 1:
#         enterRecord()
#     elif ch == 2:
#         showRecord()
#     elif ch == 3:
#         name = input("Enter record you want to search: ") + "\n"
#         searchRecord(name)
#     elif ch == 4:
#         exit()
#     ans = input("Continue... y/n: ")

# ast: Abstract Syntax Tree
# emp = ["Manik", "Madhuri", "Yogita"]
# print(emp)
# print(type(emp))
# semp = str(emp)
# print(semp)
# print(type(semp))

# import ast

# emp = ["Manik", "Madhuri", "Yogita"]
# print(emp)
# print(type(emp))
# semp = str(emp)
# cemp = ast.literal_eval(semp)
# print(cemp)
# print(type(cemp))

# Write a program to add record in a file

# import os

# os.chdir("./Files")
# with open("record2.txt", "a+") as file:
#     empno = int(input("Enter Employee No: "))
#     empname = input("Enter Employee Name: ")
#     empsal = float(input("Enter Employee Salary: "))
#     elist = [empno, empname, empsal]
#     file.write(str(elist) + "\n")

# Write a proogram to read record from a file
# import os
# import ast

# os.chdir("./Files")
# with open("record2.txt", "r") as file:
#     fileData = file.readlines()
# for xData in fileData:
#     elist = ast.literal_eval(xData)
#     print("Employee No: ", elist[0])
#     print("Employee Name: ", elist[1])
#     print("Employee Salary: ", elist[2])
#     print("---------------------------------------")
