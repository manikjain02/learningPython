# Write a program to add, read, update, delete, search record from a file.

import os
import ast

os.chdir("./Files")


def addRecord():
    file = open("record3.txt", "a+")
    empName = input("Enter Employee Name: ")
    empAge = int(input("Enter Employee Age: "))
    empSal = float(input("Enter Employee Salary: "))
    empDesig = input("Enter Employee Designation: ")
    elist = [empName, empAge, empSal, empDesig]
    file.write(str(elist) + "\n")
    file.close()


def showRecord():
    file = open("record3.txt")
    fileData = file.readlines()
    for xData in fileData:
        elist = ast.literal_eval(xData)
        print("Employee Name: ", elist[0])
        print("Employee Age: ", elist[1])
        print("Employee Salary: ", elist[2])
        print("Employee Designation: ", elist[3])
        print("-------------------------------------------")
    file.close()


def updateRecord(empName):
    ans = True
    with open("record3.txt") as file:
        edata = file.readlines()
    for data in edata:
        position = data.index(data)
        xdata = ast.literal_eval(data)
        if xdata[0] == empName:
            empSal = float(input("Enter New Salary: "))
            xdata[2] = empSal
            edata[position] = str(xdata) + "\n"
            print("Record Updated")
            ans = False
    with open("record3.txt", "w") as file:
        for xdata in edata:
            file.write(xdata)
    if ans:
        print("Record not updated due to no record")


def deleteRecord(empName):
    ans = True
    with open("record3.txt") as file:
        eData = file.readlines()
    for data in eData:
        position = eData.index(data)
        xdata = ast.literal_eval(data)
        if xdata[0] == empName:
            del eData[position]
            print("Record Deleted")
            ans = False
    with open("record3.txt", "w") as file:
        for xdata in eData:
            file.write(xdata)
    if ans:
        print("Record not found")


def searchRecord(empName):
    notFound = 0
    with open("record3.txt") as file:
        edata = file.readlines()
    for data in edata:
        xData = ast.literal_eval(data)
        if xData[0] == data:
            notFound = 1
            print("Employee Name: ", xData[0])
            print("Employee Age: ", xData[1])
            print("Employee Salary: ", xData[2])
            print("Employee Designation: ", xData[3])
            print("-------------------------------------------")
    if notFound == 0:
        print("Record not found")


ans = "y"
while ans == "y":
    print("1. Add record")
    print("2. Show record")
    print("3. Update record")
    print("4. Delete record")
    print("5. Search record")
    print("6. Exit")
    ch = int(input("Enter your choice... 1...6: "))
    if ch == 1:
        addRecord()
    elif ch == 2:
        showRecord()
    elif ch == 3:
        empName = input("Enter employee name for update: ")
        updateRecord(empName)
    elif ch == 4:
        empName = input("Enter employee name for delete: ")
        deleteRecord(empName)
    elif ch == 5:
        empName = input("Enter employee name to search: ")
        searchRecord(empName)
    elif ch == 6:
        exit()
    ans = input("Continue... y/n: ")
