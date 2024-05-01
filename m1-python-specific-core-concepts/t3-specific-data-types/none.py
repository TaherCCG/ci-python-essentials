# None

""" 
None is a special constant in Python that represents the absence of a value or a null value. 
It is an object of its own datatype, the NoneType. We cannot create multiple None objects but can assign it to variables. 
These variables will be equal to one another. We must take special care that None does not imply False, 0, or an empty list, dictionary, string etc. 
For example:
"""

a = 1
a = None
print(a)

def donothing():
    b = 0

print(donothing())


# None is a falsy value, but when cast to a boolean it evaluates to False.

# The None object is returned by any function that doesn't explicitly return anything else.

# For example, the print() function in Python 3 returns None:

x = print("hello")
print()
print(x)