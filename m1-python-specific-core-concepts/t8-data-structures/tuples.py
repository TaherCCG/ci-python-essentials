# Tuples

""" Tuples are similar to lists but they are immutable.
You can recognize tuples by their parentheses ( and ) that hold elements, separated by commas.
Tuples can contain any type of data, including other tuples.
You can create a tuple by placing elements inside parentheses, separated by commas.For example: 

my_tuple = (1, 2, 3, 4, 5)

Tuples are useful when you want to store a collection of items that should not be changed.
For example, you might use a tuple to store a set of coordinates that represent a point in 2D space.
You can access items in a tuple using indexing, just like with lists.
You can also use slicing to access a subset of items in a tuple.
Tuples support the same operations as lists, such as concatenation and repetition.
However, you cannot change the content of a tuple once it has been created.
You can convert a list to a tuple using the tuple() function, and vice versa using the list() function.
"""

# Runnable Example: Tuples in Python
print("Tuples in Python")
print()

empty = ()
singleton = 'hello',
tup = 12345, 54321, 'hello!' # packing two ints and a string in a tuple
print(empty)
print(singleton)
print(tup)
print(tup[1])
x, y, z = tup # unpacking tuple into variables
print(z)


"""
The above code snippet demonstrates how to create and work with tuples in Python.
It creates an empty tuple, a singleton tuple, and a tuple with three elements.
It then accesses an element in the tuple using indexing and unpacks the tuple into separate variables.
"""

