# File System
# There are 3 types of file modes
# 'r' - Read - Opens a file for reading (default mode)
# 'w' - Write - Opens a file for writing, creates a new file if it does not exist or truncates the file if it exists
# 'a' - Append - Opens a file for appending, creates a new file if it does not exist
# 'r+' - Read and Write - Opens a file for reading and writing, creates a new file if it does not exist
# 'w+' - Write and Read - Opens a file for writing and reading, creates a new file if it does not exist or truncates the file if it exists
# 'a+' - Append and Read - Opens a file for appending and reading, creates a new file if it does not exist

# How to create a file (conventional method)
# file_object = open('file_name', 'mode: 'r' or 'w' or 'a' or 'r+' or 'w+' or 'a+')

# another way to create a file
# with open('file_name', 'mode: 'r' or 'w' or 'a' or 'r+' or 'w+' or 'a+') as file_object:

# How to write to a file
# file_object.write('string')
# file_object.writelines(['string1', 'string2', 'string3'])

# How to read from a file
# file_object.read() - reads the entire file
# file_object.readline() - reads a single line from the file
# file_object.readlines() - reads all lines from the file and returns a list of lines

# How to close a file
# file_object.close()
# How to delete a file
# os.remove('file_name')
# How to rename a file
# os.rename('old_file_name', 'new_file_name')
# How to check if a file exists
# os.path.exists('file_name')
# How to get the size of a file
# os.path.getsize('file_name')
# How to get the current working directory
# os.getcwd()
# How to change the current working directory
# os.chdir('directory_name')
# How to create a directory
# os.mkdir('directory_name')
# How to remove a directory
# os.rmdir('directory_name')
# How to list all files and directories in a directory
# os.listdir('directory_name')

# import os

# os.chdir("./Files")
# file = open("manik1.txt", "w")
# file.write("Hello World")
# file.close()

# import os

# os.chdir("./Files")
# with open("manik.txt", "w") as file:
#     file.write("Manik is a good boy\n")

# import os

# os.chdir("./Files")
# file = open("manik.txt", "a")
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# file.write("Name: " + name + "\n")
# file.write("Age: " + age + "\n")
# file.close()

# Read the file

# import os

# os.chdir("./Files")
# file = open("manik2.txt", "r")
# print(file.read(10))  # reads the first 10 characters
# print(file.read(10))  # reads the next 10 characters
# print(file.read())  # reads the rest of the file
# file.close()

# readline() method: reads a single line from the file
# import os

# os.chdir("./Files")
# file = open("manik2.txt", "r")
# print(file.readline())  # reads the first line
# print(file.readline())  # reads the second line
# print(file.readline())  # reads the third line
# print(file.readline())  # reads the fourth line
# file.close()

# readlines() method: reads all lines from the file and returns a list of lines
# import os

# os.chdir("./Files")
# file = open("manik2.txt", "r")
# # print(file.readlines())  # reads all lines and returns a list of lines
# data = file.readlines()
# print(data)  # prints the list of lines
# file.close()

# seek() method: moves the cursor to a specific position in the file
# import os

# os.chdir("./Files")
# file = open("manik2.txt", "r")
# print(file.read(10))  # reads the first 10 characters
# file.seek(0)  # moves the cursor to the beginning of the file
# print(file.read(10))  # reads the first 10 characters again
# file.seek(5)  # moves the cursor to the 5th position
# print(file.read(10))  # reads the next 10 characters
# file.close()

# tell() method: returns the current position of the cursor in the file
# import os

# os.chdir("./Files")
# file = open("manik2.txt", "r")
# print(file.tell())  # returns the current position of the cursor
# print(file.read(10))  # reads the first 10 characters
# file.close()

# Question: We have to add multiple data record
# import os

# os.chdir("./Files")
# file = open("record.txt", "a+")
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# salary = float(input("Enter your salary: "))
# designation = input("Enter your designation: ")
# elist = [name, age, salary, designation]
# file.write(str(elist) + "\n")
# file.close()
