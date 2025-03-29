# Dictionary
# Dictionary is a collection of key-value pairs
# Dictionary is mutable
# Dictionary is unordered
# Dictionary is indexed
# Dictionary is represented by {}
# Dictionary is created by dict() constructor
# Dictionary is created by {key:value} pairs
# Dictionary keys are unique
# Dictionary values are not unique
# Dictionary keys are immutable
# Dictionary values are mutable
# Dictionary values can be any data structure
# Dictionary values can be another dictionary

# Create a dictionary
# d = dict()
# print(type(d))

# d = {}
# print(type(d))

# d = {1: "one", 2: "two", 3: "three"}
# print(d)

# adding key-value pairs
# d = {}
# d[1] = "one"
# print(d)

# d[2] = "two"
# print(d)

# update key-value pairs
# d = {}
# d[1] = "one"
# d[2] = "two"
# print(d)
# d[1] = "ONE"
# print(d)

# delete key-value pairs
# pop() method deletes the key-value pair and returns the value
# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# x = d.pop(2)
# print(x)

# popitem() method deletes the last key-value pair and returns the key-value pair in a tuple
# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# x = d.popitem()
# print(x)

# del statement deletes the key-value pair
# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# del d[2]
# print(d)

# items() method returns the key-value pairs in a list of tuples
# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# x = d.items()
# print(x)

# keys() method returns the keys in a list
# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# x = d.keys()
# print(x)

# values() method returns the values in a list
# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# x = d.values()
# print(x)

# clear() method deletes all the key-value pairs
# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# d.clear()
# print(d)

# update() method adds the dictionary with another dictionary
# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# d1 = {4: "four", 5: "five"}
# d.update(d1)
# print(d)

# update() method updates the dictionary with key-value pairs
# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# d.update({1: "ONE", 4: "four"})
# print(d)

# copy() method copies the dictionary
# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# d1 = d.copy()
# print(d1)
# d1[1] = "ONE"
# print(d1)
# print(d)

# setdefault() method returns the value of the key
# if the key is not present, it adds the key-value pair
# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# x = d.setdefault(1)
# print(x)

# x = d.setdefault(4, "four")
# print(x)
# print(d)
