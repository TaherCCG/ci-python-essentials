# Class Naming Conventions

"""
1. Use descriptive names for classes
2. Use CamelCase for class names
3. Avoid using single letters for class names
4. Avoid using reserved words for class names
5. Avoid using special characters for class names
6. Use the same naming convention for all variables
7. Use the same naming convention for all functions
8. Use the same naming convention for all classes
9. Use the same naming convention for all modules
10. Use the same naming convention for all packages
"""

# Example of a class name that follows the naming conventions:

class Student:
    def __init__(self, name, email, subjects):
        self.name = name
        self.email = email
        self.subjects = subjects

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Subjects: {self.subjects}"
    
# Example of a class name that does not follow the naming conventions:

class s:
    def __init__(self, n, e, s):
        self.n = n
        self.e = e
        self.s = s

    def __str__(self):
        return f"Name: {self.n}, Email: {self.e}, Subjects: {self.s}"


"""
When naming a class, try and give it a name that gives the reader an idea of the purpose of the class. Class names should have 
their first character capitalised.  If the class name is made up of multiple words, then each word should have its first letter
capitalised. This is known as CamelCase. The same rules apply to class names as they do to function names. 
"""



