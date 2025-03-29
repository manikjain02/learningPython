# JSON: JavaScript Object Notation
# JSON is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is language independent but uses conventions that are familiar to programmers of the C family of languages, which includes C, C++, C#, Java, JavaScript, Perl, Python, and many others. These properties make JSON an ideal data interchange language.
# JSON is built on two structures:
# 1. A collection of name/value pairs (often called an object, dictionary, or hash table in various languages).
# 2. An ordered list of values (often called an array, vector, list, or sequence in various languages).
# JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C family of languages. These properties make JSON an ideal data interchange language.
# JSON is a language-independent data format. It was derived from JavaScript, but many modern programming languages include code to generate and parse JSON-format data. JSON is often used for serializing and transmitting structured data over a network connection in a process known as serialization.
# JSON is a common data format with diverse uses in electronic data interchange, including that of web applications with servers. It is also used for configuration files and for data storage.
# JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C family of languages. These properties make JSON an ideal data interchange language.

# Serialization: The process of converting an object into a format that can be easily stored or transmitted and reconstructed later. In Python, this is often done using the `json` module, which can convert Python objects into JSON strings and vice versa.
# Deserialization: The process of converting a serialized format (like JSON) back into an object. In Python, this is done using the `json` module to parse JSON strings and convert them back into Python objects.

# json.dumps(): json.dumps is used to convert a normal dictionary to a JSON.
# json.dump(): json.dump is used to store data in a JSON file.
# json.loads(): json.loads is used to convert a JSON string to a dictionary.
# json.load(): json.load is used to read a JSON file and convert it to a dictionary.

# import json

# student = {
#     "name": "Manik Jain",
#     "age": 25,
#     "rollno": 2452566882,
#     "phoneNumber": 9667133266,
# }
# # serializing the student dictionary to a JSON string
# json_object = json.dumps(student)
# # printing the JSON string
# print(json_object)
# print(type(json_object))  # <class 'str'>

# import json
# import os

# os.chdir("./Files")

# student = {
#     "name": "Manik Jain",
#     "age": 25,
#     "rollno": 2452566882,
#     "phoneNumber": 9667133266,
# }
# # write the json serialized data to a file
# with open("manik.json", "a+") as file:
#     json.dump(student, file)

# better approach is that first we have to serialize the data and then write it to a file

# import json
# import os

# os.chdir("./Files")
# with open("manik.json") as file:
#     fileData = json.load(file)
# print(fileData)
# print(type(fileData))  # <class 'dict'>

# CSV: Comma Separated Values
# CSV is a simple file format used to store tabular data, such as a spreadsheet or database.
# Each line of the file is a data record. Each record consists of one or more fields, separated by commas. The first line of the file may contain the names of the fields.
# CSV files can be created and read by many programs, including Microsoft Excel, Google Sheets, and programming languages like Python, R, and Java.
# CSV files are often used for data exchange between different applications, as they are easy to read and write, and can be opened in a variety of programs.

# DictWriter: A class in the `csv` module that allows you to write dictionaries to a CSV file. Each dictionary represents a row in the CSV file, with the keys as the column headers and the values as the data for each column.
# writerow(): A method of the `csv.writer` and `csv.DictWriter` classes that writes a single row to the CSV file. In the case of `DictWriter`, it takes a dictionary as an argument, where the keys correspond to the column headers defined when creating the `DictWriter` object.
# writerows(): A method of the `csv.writer` and `csv.DictWriter` classes that writes multiple rows to the CSV file. In the case of `DictWriter`, it takes a list of dictionaries as an argument, where each dictionary represents a row in the CSV file.
# writeheader(): A method of the `csv.DictWriter` class that writes the header row to the CSV file. The header row contains the column names defined when creating the `DictWriter` object.
# DictReader: A class in the `csv` module that allows you to read CSV files as dictionaries. Each row in the CSV file is represented as a dictionary, where the keys are the column headers and the values are the data for each column.
# reader(): A method of the `csv.reader` and `csv.DictReader` classes that reads the contents of a CSV file. In the case of `DictReader`, it returns an iterator that yields dictionaries for each row in the CSV file, where the keys are the column headers and the values are the data for each column.

# import csv
# import os

# os.chdir("./Files")
# data = [
#     {
#         "name": "Madhuri Yadav",
#         "age": 19,
#         "city": "Faridabad",
#         "phoneNumber": "8700620912",
#     },
#     {
#         "name": "Manik Jain",
#         "age": 25,
#         "city": "Faridabad",
#         "phoneNumber": "9667133266",
#     },
#     {
#         "name": "Yogita Yadav",
#         "age": 23,
#         "city": "Faridabad",
#         "phoneNumber": "8285647858",
#     },
# ]

# with open("manik.csv", "w", newline="") as file:
#     fieldName = ["name", "age", "city", "phoneNumber"]
#     writer = csv.DictWriter(file, fieldnames=fieldName)
#     writer.writeheader()  # write the header
#     writer.writerows(data)  # write the data

# Read data the csv file

# import csv
# import os

# os.chdir("./Files")
# with open("manik.csv", "r") as file:
#     csvFile = csv.reader(file)
#     for lines in csvFile:
#         print(lines)
