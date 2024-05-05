# Reserved Keywords

"""
Keywords are reserved words in Python. That means they cannot be used as ordinary identifiers like a variable, function, method or class name. 
They have a specific meaning and purpose within Python and cannot be used for anything other than that purpose.
"""

# Python has a set of reserved keywords that cannot be used as variable names, function names, or any other identifiers.

# Here is a list of reserved keywords in Python:

# False      class      finally    is         return
# None       continue   for        lambda     try
# True       def        from       nonlocal   while
# and        del        global     not        with
# as         elif       if         or         yield
# assert     else       import     pass
# break      except     in         raise

# You can use the dir() function to get a list of all the reserved keywords in Python.
print(" dir builtins")
print(dir(__builtins__))
print()
# You can also use the keyword module to get a list of all the reserved keywords in Python.


print("keyword.kwlist")
import keyword

print(keyword.kwlist)

print()
print("keyword.iskeyword")
# You can use the iskeyword() function to check if a string is a reserved keyword in Python.

print(keyword.iskeyword("for")) # True
print(keyword.iskeyword("hello")) # False

"""
If using a keyword in a name cannot be avoided, then you can append a single trailing underscore. 
However, it is better to find a synonym for the keyword and use that instead.
"""

