# Function Naming Conventions

"""
1. Use descriptive names for functions
2. Use lowercase letters with underscores for function names
3. Avoid using single letters for function names
4. Avoid using reserved words for function names
5. Avoid using special characters for function names
6. Use the same naming convention for all variables
7. Use the same naming convention for all functions
8. Use the same naming convention for all classes
9. Use the same naming convention for all modules
10. Use the same naming convention for all packages
"""

# Example of a function name that follows the naming conventions:

student_data = [...]  # Replace [...] with the actual data
def calculate_student_average(student_data):
    total = 0
    for data in student_data:
        total += sum(data['subjects'])
    return total / len(student_data)

print(calculate_student_average(student_data))

# Example of a function name that does not follow the naming conventions:

s_d = [...]
def calc_stud_avg(s_d):
    total = 0
    for data in s_d:
        total += sum(data['s'])
    return total / len(s_d)

print(calc_stud_avg(s_d))

"""
The same rules for naming variables also apply to functions. When naming a function, try and give it a name that 
provides the reader with an idea of the purpose of the function.

A function within a class is known as a method. A method has the same naming conventions as a class. If you have a 
method in a class you don't wish to be public, then start its name with an underscore. This is just a convention 
for saying "Please don't touch" to other developers who are working on your code.

If you use a double underscore prefix (dunder) for an attribute in a method, then the attribute name will be altered, 
so it cannot be accessed by the regular methods. The attribute name is “mangled.”
"""

# Examples:
def divide(num, denom):
    return num / denom
    
def my_country(country):
    print(f"I am from {country}.")