# The import Statement

"""
When you create a Python program, you split your code up into different files to avoid repetition. 
These files are known as modules. We touched on this in the Frameworks, Modules And Libraries unit. 
Python allows you to import entire modules or individual functions, classes or variables into other modules.

Python has built-in modules that we can import from as well. We do this with the import statement. 
The import statement is used to import modules in Python. 
The import statement is the most common way of including external modules in Python. 
Once the module is imported, you can use the functions and classes defined in the module.


In the runnable example, we have a division function in a divide.py module. Click on the Files button to see the 
other files. In main.py, we have imported the division function from the divide.py module, which allows us to use 
the division function using the division() syntax directly. However, we do not have access to the mod function 
unless we also add a from divide import mod statement in main.py.

To avoid this, we could have used import divide to import the whole module and then used divide.division or divide.mod directly.
"""

# Runnable example: (the-import-statement.py) (divide.py is in same folder as this file see divide for code)

from divide import division, mod

print(mod(4, 6))
print(division(4, 2))

