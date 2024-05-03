# Ternary Operator
""" 
Teranary operator is a conditional operator that provides a shorter syntax for if else statement.
Syntax: variable = value1 if condition else value2

a if c else b
"""

# Example 1: Check if my_boolean is True or False and assign the value to my_string variable.
my_boolean = False

my_string = "Hello" if my_boolean else "World"

print(my_string)


# Example 2: Check if a number is equal to 5
number = 5

result = "Number is equal to 5" if number == 5 else "Number is not equal to 5"

print(result)


# Example 3: Check if a number is even or odd
number = 10

result = "Even" if number % 2 == 0 else "Odd"

print(result)
