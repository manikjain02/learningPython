# List
# li = []
# print(li)
# print(type(li))

# mli = list()
# print(mli)
# print(type(mli))

# li = ["a", 1, 2, 3.5, True]
# print(li)

# methods to access the elements of the list
# li = ["a", 1, 2, 3.5, True]
# print(li[0])

# 3 methods to add elements to the list
# append() - adds element at the end of the list
# insert() - adds element at the specified index
# extend() - adds elements of the list

# li = ["a", 1, 2, 3.5, True]
# append()
# li.append("b")
# print(li)

# insert()
# li.insert(1, "c")
# print(li)

# extend()
# li.extend([1, 2, 3])
# print(li)

# 3 methods to remove elements from the list
# remove() - removes the first occurence of the element
# pop() - removes the element at the specified index or from the end of the list
# clear() - removes all the elements

# li = ["a", 1, 2, 3.5, True, "b", 1, 2, 3]
# remove()
# li.remove(1)
# print(li)

# pop()
# li.pop(5)
# print(li)
# li.pop()
# print(li)

# clear()
# li.clear()
# print(li)


# universal functions
# del - deletes the element at the specified index
# len - returns the number of elements in the list
# min - returns the minimum element in the list, only for numbers
# max - returns the maximum element in the list, only for numbers
# sum - returns the sum of the elements in the list
# sorted - returns the new sorted list, does not change the original list

# li = [1, 2, 3.5, 1, 2, 3]
# del
# del li[3]
# print(li)

# len
# print(len(li))

# min
# print(min(li))

# max
# print(max(li))

# sum
# print(sum(li))

# sorted
# print(sorted(li))

# sort() - sorts the list in ascending order
# li = [1, 2, 3.5, 1, 2, 3]
# li.sort()
# print(li)

# count() - returns the number of occurences of the element

# c1 = li.count(1)
# print(c1)

# index() - returns the index of the first occurence of the element
# i = li.index(1)
# print(i)

# copy() - returns the shallow copy of the list and does not refer to the same memory location
li = [1, 2, 3.5, 1, 2, 3]
# cli = li.copy()
# print(cli)
# print(li)
# cli.append(4)
# print(cli)
# print(li)

# cli = li refering to the same memory location
# print(cli)
# print(li)
# cli.append(4)
# print(cli)
# print(li)

# li.reverse()
# print(li)

# add element to the list if it does not exist in the list
# if it exists, print the message that the number already exists in the list

# definedList = [10, 20, 30, 40, 50]
# userDefinedInput = int(input('Enter Number: '))
# if(userDefinedInput in definedList):
#     print('Number already exists in the list')
# else:
#     definedList.append(userDefinedInput)
# print(definedList)

# count the given element in the list without using count() method
# definedList = [1, 2, 1, 3, 4, 5, 6, 1, 2, 5, 1, 1, 4, 1, 90]
# userInput = int(input("Enter Number: "))
# count = 0
# for i in definedList:
#     if i == userInput:
#         count += 1
# print(count)

# reverse the list without using reverse() method
# definedList = [10, 20, 30, 40, 50]
# length = 0
# rli = list()
# for i in definedList:
#     length += 1
# for i in range(length - 1, -1, -1):
#     rli.append(definedList[i])
# print(rli)

# Comprehension in lists
# to reduce the number of lines of code

# li = [1, 2, 3, 4, 5]
# for i in li:
#     if i % 2 == 0:
#         print(i)

# li = [1, 2, 3, 4, 5]
# even = [i for i in li if i % 2 == 0]
# print(even)
