# List Methods in Python

"""
Lists in Python have several built-in methods that you can use to modify and manipulate lists.

Here are some of the most commonly used list methods:

Method	                            |       Description
=======================================================================================================
list.append(x)	                    |   Add an item to the end of the list.
list.extend(list)	                |   Extend the list by appending another list.
list.insert(i, x)	                |   Insert an item at a given position. The first argument is the index of the element before which to insert
list.remove(x)	                    |   Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
list.pop(i)	                        |   Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
list.clear()	                    |   Remove all items from the list.
list.index(x, start, end)	        |   Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.The optional arguments start and end are interpreted as in the slice notation.
list.count(x)	                    |   Return the number of times x appears in the list.
list.sort(key=None, reverse=False)	|   Sort the items of the list in place
list.reverse()	                    |   Reverse the elements of the list in place.
list.copy()	                        |   Return a copy of the list. Equivalent to a[:].
"""


# Runnable Example: List Methods in Python
print("List Methods in Python")
print()

menu = ['eggs', 'bacon', 'spam', 'spam']
print(menu)
print(menu.count('spam'))
print(menu.count('eggs'))
print(menu.index('eggs'))
print(menu.reverse())
print(menu)
print(menu.append('lobster thermidor'))
print(menu)
print(menu.sort())
print(menu)
print(menu.pop())
print(menu)