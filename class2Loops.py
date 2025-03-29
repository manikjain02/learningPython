# for Loop

# 1. when only one number is given in range then it will start from 0 and go till that number - 1

# for i in range(10):
#     print(i)

# 2. when two numbers are given in range then it will start from first number and go till second number - 1

# for i in range(0, 10):
#     print(i)

# 3. when three numbers are given in range then it will start from first number and go till second number - 1 with step of third number

# for i in range(0, 10, 2):
#     print(i)


# While Loop

# i=0
# while i<10:
#     print(i)
#     i+=1


# Nested Loop

# for i in range(5):  #outer loop
#     for j in range(5): #inner loop
#         print(i*j)


# end: this is used to print the output in same line

# for i in range(5):
#     for j in range(5):
#         print(i*j, end=" ")

# print(): this is used to print the output in new line

# for i in range(5):
#     for j in range(5):
#         print(i*j, end=" ")
#     print()

# if-else
# points to remember: else is optional, else will be executed when if condition is false

# a = 10
# b = 20
# if(a > b):
#     print(a, "is greater")
# else:
#     print(b, "is greater")


# if-elif-else
# points to remember: else is optional, else will be executed and we can have multiple elif

# a=10
# b=20
# c=30
# if(a>b and a>c):
#     print(a,"is greater")
# elif(b>a and b>c):
#     print(b,"is greater")
# else:
#     print(c,"is greater")


# Taking user input

# input = input("Enter a number: ")
# print(input)
# print(type(input))

# type casting because input is always string by default

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print(number, "is Even")
# else:
#     print(number, "is Odd")

# break: it is used to break the loop

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# continue: it is used to skip the current iteration

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# pass: it is used to do nothing

# for i in range(10):
#     if i == 5:
#         pass
#     print(i)
