# Set is a collection of unique elements
# Set is unordered
# Set is mutable
# Set is iterable
# Set is unindexed
# Set is enclosed in curly braces {}
# Set is created using set() function
# Set is created using set comprehension

# mset = set()
# print(type(mset))

cset = {1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 9, 10}
# print(cset)

# add element to set: add() adds only one element at a time
# cset.add(11)
# print(cset)

# update elements to set: update() adds multiple elements at a time
# cset.update([12, 13, 14, 15])
# print(cset)

# remove element from set: remove() removes the element from the set if it is present otherwise it will throw an error
# cset.remove(1)
# print(cset)

# error will be thrown if the element is not present in the set
# cset.remove(15)
# print(cset)

# discard() removes the element from the set if it is present otherwise it will not throw an error
# cset.discard(15)
# print(cset)

# pop() removes the first element from the set
# cset.pop()
# print(cset)

# clear() removes all the elements from the set
# cset.clear()
# print(cset)

s1 = {1, 3, 6, 8, 10, 11, 17, 19, 20}
s2 = {1, 2, 3, 4, 5, 6, 32, 11, 28, 26}

# union() returns all the elements from both the sets
# print(s1.union(s2))

# intersection() returns the common elements from both the sets
# print(s1.intersection(s2))

# difference() returns the elements which are present in the first set but not in the second set
# print(s1.difference(s2))

# symmetric_difference() returns the elements which are not common in both the sets
# print(s1.symmetric_difference(s2))

# intersection_update() updates the first set with the common elements from both the sets
# s1.intersection_update(s2)
# print(s1)

# difference_update() updates the first set with the elements which are present in the first set but not in the second set
# s1.difference_update(s2)
# print(s1)

# symmetric_difference_update() updates the first set with the elements which are not common in both the sets
# s1.symmetric_difference_update(s2)
# print(s1)

# superset and subset
# issuperset() returns True if the first set contains all the elements of second set
# s3 = {1, 2, 3, 4, 5, 6, 32, 11, 28, 26, 17, 19, 20}
# print(s3.issuperset(s2))

# issubset() returns True if the second set contains all the elements of first set
# s3 = {1, 3, 6, 8, 10}
# print(s3.issubset(s1))

# how to convert list to set
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l1)
# s4 = set(l1)
# print(s4)

# WAP to add duplicate elements to the set and print the set
# l1 = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 9, 10]
# s3 = set()
# s4 = set()
# for i in l1:
#     if i not in s3:
#         s3.add(i)
#     else:
#         s4.add(i)
# print(s3)
# print(s4)

# frozenset is immutable set and it is created using frozenset() function
# we can't add or remove elements from frozenset
# we can't update the elements of frozenset
# we can't use set operations on frozenset
# we can't use set comprehension on frozenset

# fset = frozenset()
# print(type(fset))

# fset = {1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 9, 10}
# print(fset)
