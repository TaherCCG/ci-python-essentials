# Python For Loops

""" Python For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
"""

# Example 1
print("Example 1: ")
languages = ["HTML", "CSS", "JavaScript"]
for language in languages:
    print(language)

# Example 2
print("Example 2: ")
for character in "Python":
    print(character)

# Example 3
print("Example 3: ")
for x in range(6):
    print(x)

# Example 4
print("Example 4: ")
for x in range(2, 6):
    print(x)

# Example 5
print("Example 5: ")
for x in range(2, 30, 3):
    print(x)


# Range() Function
""" To loop through a set of code a specified number of times, we can use the range() function,
that returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
and ends at a specified number."""

# Example 6
print("Example 6: ")
for x in range(6):
    print(x)

# len() Function
""" To loop through a set of code a specified number of times, we can use the range() function,
that returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
and ends at a specified number."""


# Runnable Example
print("Runnable Example: ")

foods = ['bacon', 'sausage', 'egg', 'spam']

for ind in range(len(foods)):
	# In this example only the index is iterated over not the value
    print(ind, foods[ind])
print(foods)
# In this case we need to calculate the length of the foods collection
# Then we generate a range of integers equal to that length
# Then we iterate over that range of integers
