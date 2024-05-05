# Variable Naming Conventions

"""
1. Use descriptive names for variables
2. Use lowercase letters with underscores for variable names
3. Avoid using single letters for variable names
4. Avoid using reserved words for variable names
5. Avoid using special characters for variable names
6. Use the same naming convention for all variables
7. Use the same naming convention for all functions
8. Use the same naming convention for all classes
9. Use the same naming convention for all modules
10. Use the same naming convention for all packages
"""

# Example of a variable name that follows the naming conventions:

student_data = [
    {
        'name': 'John Smith',
        'email': '',
        'subjects': ['Math', 'Psychology', 'Physics', 'Chemistry', 'Biology']
    },
    {
        'name': 'Mary Jones',
        'email': '',
        'subjects': ['Fine Art', 'Music', 'Biology', 'Geography', 'Politics']
    }
]

print(student_data)

# Example of a variable name that does not follow the naming conventions:

s_d = [
    {
        'n': 'John Smith',
        'e': '',
        's': ['Math', 'Psychology', 'Physics', 'Chemistry', 'Biology']
    },
    {
        'n': 'Mary Jones',
        'e': '',
        's': ['Fine Art', 'Music', 'Biology', 'Geography', 'Politics']
    }
]

print(s_d)

"""
Python is quite forgiving when it comes to naming. However, there are suggested style rules that you should follow. 
Variable names should be lowercase and if including multiple words, should use underscores as separators. 
Giving a variable a name that explains its purpose is encouraged. Where the meaning is obvious, you can use a single 
letter variable name. There is a convention where you prefix a global variable with an underscore if you are using it in a 
module imported into another module. There is no constant in Python unlike the const in JavaScript, so if you have a 
variable you do not want to be changed, then use capital letters to denote this. Generally, it is a bad idea to use lowercase L, 
uppercase O and uppercase I for single-character names as they are easily confused by eye with other characters.
"""

# Examples
count = 0
first_name = "Brian"
greeting = "Hello, World!"
PI = 3.14159
