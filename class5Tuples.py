# Tuples are read-only lists
# Tuples are defined by parentheses or tuple() function
# Tuples are indexed by integers
# Tuples are ordered
# Tuples are immutable
# Tuples are faster than lists
# Tuples are used to protect data
# Tuples are used to return multiple values from a function
# Tuples are used to pass multiple values to a function
# Tuples are used to unpack values
# Tuples are used to format strings

# t = ()
# print(type(t))

# t = tuple()
# print(type(t))

# t = (1, 2, 3)
# print(t)

# t = (1, 2, 3)
# print(t[0])

# count() method returns the number of times a specified value occurs in a tuple
# t = (1, 2, 3)
# print(t.count(1))

# index() method returns the index of the first occurrence of the specified value
# t = (1, 2, 3)
# print(t.index(1))

# Slicing
# Slicing is used to get a range of elements from a tuple
# t = (1, 2, 3, 4, 5)
# print(t[:3])          #this will return (1, 2, 3) starts from 0 and ends at n-1

# t = (1, 2, 3, 4, 5)
# print(t[1:3])  # this will return (2, 3) starts from 1 and ends at n-1


# t = (1, 2, 3, 4, 5)
# print(t[3:])  # this will return (4, 5) starts from 3 and ends at n-1

# t = (1, 2, 3, 4, 5)
# print(t[::2])  # this will return (1, 3, 5) starts from 0 and ends at n-1 with step 2

# t = (1, 2, 3, 4, 5)
# print(
#     t[::-1]
# )  # this will return (5, 4, 3, 2, 1) starts from n-1 and ends at 0 with step -1

# t = (1, 2, 3, 4, 5)
# print(t[3:0:-1])  # this will return (4, 3, 2) starts from 3 and ends at 0 with step -1

# t = (1, 2, 3, 4, 5)
# print(t[-4:])  # this will return (2, 3, 4, 5) starts from 1 and ends at n-1

# t = (1, 2, 3, 4, 5)
# print(t[::])  # this will return (1, 2, 3, 4, 5) starts from 0 and ends at n-1
