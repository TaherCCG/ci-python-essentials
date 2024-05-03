# List Slicing & Indexing in Python

"""
Lists in Python support indexing and slicing. Indexing allows you to access individual items in a list, while slicing allows 
you to access a subset of items in a list.
"""

# Runnable Example 1: Indexing
print("List Indexing in Python")
print()
fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
# As lists are zero-indexed index 0 is the first element
print(fruits[0])
# Using an index of -1 gives the last element. Negative indexing counts from the right
print(fruits[-1])
print(fruits[2])
print(fruits[-3])

# Runnable Example 2: Slicing
print("List Slicing in Python")
print()
# Slicing allows you to access a subset of items in a list. You can specify a range of indexes separated by a colon.
fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
print(fruits[0:2])
print(fruits[2:4])
print(fruits[:2])

#Runnable Example 3: Slicing with Step Index
print("List Slicing with Step Index in Python")
print()
# You can also specify a step index to skip items in the list. The step index is specified after the second colon.
fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
print(fruits[0:4:2])
print(fruits[::2])
print(fruits[1::2])
print(fruits[::-1])



