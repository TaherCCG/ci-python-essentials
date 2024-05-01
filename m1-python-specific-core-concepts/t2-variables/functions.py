"""
Description: Functions in Python
Functions in Python are blocks of code that are designed to do one job.
Functions are used to organize code into reusable blocks.
Functions in Python are defined using the def keyword.
Functions in Python can take arguments and return values.
Functions in Python can be called by their name followed by parentheses.
Functions in Python can be defined to take arguments.
Functions in Python can be defined to return values.
"""

# Functions in Python with default arguments
def print_message():
    print("Hello World!")

print_message()

# Functions in Python with arguments
def print_name(name):
    print(f"Hello {name}!")
    
print_name("John")


# Functions in Python with return values
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print(result)

# Functions in Python with multiple return values
def get_name_and_age():
    name = "John"
    age = 25
    return name, age

name, age = get_name_and_age()
print(name)
print(age)




