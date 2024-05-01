# Converting Between Data Types

""" 
There are several built-in functions in Python that can be used to convert between data types.

int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)

float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)

str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals


Some of the more common type conversions are in the table below.

Function	What it converts
=========|===================
int()	    Converts to an integer
float()	    Converts to a floating-point number
hex()	    Converts a number to a hexadecimal string
oct()	    Converts a number to a octal string
tuple()	    Converts to a tuple
set()	    Converts to a set
list()	    Converts to a list
dict()	    Converts a tuple into a dictionary
str()	    Converts a number into a string

"""

# Runnable Example 1:
print("Runnable Example 1: ")
first_number = input("Input your first number:")
second_number = input("Input your second number:")

print(first_number + second_number)

print("\n")

# Runnable Example 2:
print("Runnable Example 2: int()")

first_number = int(input("Input your first number:"))
second_number = int(input("Input your second number:"))

print(first_number + second_number)

print("\n")


# Runnable Example 3:
print("Runnable Example 3: float()")
first_number = float(input("Input your first number:"))
second_number = float(input("Input your second number:"))

print(first_number + second_number)
print("\n")

# Runnable Example 4:
print("Runnable Example 4: str()")
first_number = str(input("Input your first number:"))
second_number = str(input("Input your second number:"))

print(first_number + second_number + "\n")


# Runnable Example 5:
# This will throw an error because you cannot concatenate a string and an integer

"""
print("Runnable Example 5: ")
my_number = 5
my_string = "5"

print(my_string + my_number)
"""

"""
Python is a strongly typed language. Therefore if we wanted to concatenate an int to a string, we would not be able to do so. 
In a language like JavaScript, which is a weakly typed language, we would be able to concatenate a number to a string.

console.log(5+'6')
56

Lets take a look at an example of this in Python. If we wanted to concatenate an int to a string, 
then we first need to convert our int to a string; otherwise, Python will error and say: TypeError: can only concatenate str (not "int") to str.

In the example below, you will need to use the str() type conversion on my_number. Run the code and then make the change."""

print("Runnable Example 5: ")
my_number = str(5)
my_string = "5"

print(my_string + my_number)