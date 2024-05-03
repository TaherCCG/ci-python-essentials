# Lists in Python

"""
Lists are ordered collections of items. They are mutable, which means that you can change their content without changing their identity. 
You can recognize lists by their square brackets [ and ] that hold elements, separated by commas.

Lists can contain any type of data, including other lists.

Lists are similar to arrays in other programming languages, but they have some additional functionality that makes them more versatile.

You can create a list by placing elements inside square brackets, separated by commas. For example:

my_list = [1, 2, 3, 4, 5]
"""

# Runnable Example: Lists in Python

fruits = ['apple', 'orange', 'banana', 'pear', 'plum']

# Print all fruits
for fruit in fruits:
    print(fruit)

print()

# Get an item located in a list
second_item = fruits[1]
print(second_item)
print()

# Add an item to the list
fruits.append('cherries')
print(fruits)
print()

# Reverse the list
fruits.reverse()
print(fruits)

# Sort the list alphabetically:
fruits.sort()
print(fruits)
