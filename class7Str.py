# Strings
# string is a sequence of characters
# string is immutable
# string is enclosed in single quotes or double quotes
# string is enclosed in triple quotes for multi-line strings
# string is indexed from 0 to n-1
# string is sliced using [start:end:step]
# string is concatenated using +
# string is repeated using *
# string is checked for membership using in
# string is formatted using % operator
# string is formatted using format method
# string is formatted using f-string
# string is formatted using template strings
# string is formatted using string interpolation
# string is formatted using string concatenation

# name = "manik jain"
# print(name)
# print(type(name))

# print(name.capitalize()) # Manik jain
# print(name.title())  # Manik Jain
# print(name.upper())  # MANIK JAIN
# print(name.lower())  # manik jain
# print(name.split())  # ['manik', 'jain']
# name1 = "manik,jain"
# print(name1.split(","))  # ['manik', 'jain']
# print(name[0])  # m
# print(name[1])  # a
# name1 = name.split()
# print(name1[0]) # manik
# print(name1[0][1]) # a

# WAP to take string as input and print its initials in capital and last name

# name = input("Enter your name: ")
# name1 = name.split()
# length = len(name1)
# newName = ""
# for i in range(length - 1):
#     newName += name1[i][0] + " "
# newName += name1[length - 1]
# print(newName.title())


# name = "manik"
# print(name.isdigit()) # False

# name = "123"
# print(name.isdigit())  # True

# name = "manik"
# print(name.isalpha())  # True

# name = "manik123"
# print(name.isalpha())  # False

# name = "manik123"
# print(name.isalnum())  # True

# name = "Manik Jain"
# print(name.casefold())  # manik jain

# name = "Manik"
# print(name.center(20))

# name = "Manik"
# print(name.center(10, "*"))  # ***Manik***

# name = "      Manik      "
# print(name)
# print(name.strip())  # Manik
# print(name.lstrip())  # Manik
# print(name.rstrip())  #       Manik

# name = "Manik"
# # print(name.encode())
# encodedString = name.encode()
# print(encodedString)
# decodedString = encodedString.decode()
# print(decodedString)

# name = "Manik"
# print(name.endswith("k"))  # True

# name = "Manik"
# print(name.startswith("M"))  # True

# name = "Manik"
# print(name.endswith("a"))  # False

# li = [
#     "Yogita",
#     "Manik",
#     "Madhuri",
#     "Udit",
#     "Jatin",
#     "ram",
#     "shyam",
#     "mohan",
#     "sohan",
#     "rohan",
# ]
# for name in li:
#     if name.startswith("M") or name.startswith("m"):
#         print(name)  # Manik, Madhuri, Mohan

# name = "Manik"
# print(name.find("a"))  # 1

# name = "Manik Jain"
# print(name.replace("a", "A"))  # MAnik JAin

# name = "Manik Jain"
# print(f"{name} is a good")

# name = "Manik Jain"
# designation = "Software Developer"
# print("{} is a good, he is {}".format(name, designation))

# name = "Manik Jain"
# designation = "Software Developer"
# print("{0} is a good, he is {1}".format(name, designation))

# name = "Yogita Yadav"
# appearance = "So cute"
# print("{name} is a good, she is {appearance}".format(name=name, appearance=appearance))

# name = "Yogita Yadav"
# appearance = "So cute"
# print(f"{name} is a good, she is {appearance}")
