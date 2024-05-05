# Comments in Python

# Single line comment
# This is a single line comment
# This is another single line comment

# Multi-line comment
"""
This is a multi-line comment
This is another line of the multi-line comment
"""

# Comments can be used to explain what a piece of code does
# This function calculates the sum of two numbers
def add(num1, num2):
    return num1 + num2

# Comments can also be used to prevent a piece of code from running
# print("This code will not run")
# print("This code will not run either")

"""
Developers spend a lot of time writing code. So much time in fact that revisiting a piece of code that was written a couple of weeks ago 
may have little to no meaning to that developer, let alone any other developers that may be working on that same project. Code can get 
quite busy, and it can get unwieldy when people try to read it, whether it’s someone else's or if you come back to your code at a later 
stage. We can use code commenting, which will allow us to write human-readable explanations to our code. Comments will be ignored by the 
Python interpreter, meaning that we can add in as many comments as we need, without it affecting the speed or performance of our program.
We can write different types of comments. We have single-line comments and multiline comments. Multiline comments can take up as many lines
as you require. The comment itself is put between three opening double quotations and three closing double quotations. Generally speaking,
single-line comments are used to explain individual pieces of code, whereas the multi-line comments are used to describe a function, method,
class, or module. Ideally, we would use a multiline comment on every function, method, class, or module. The Python name for this is a docstring.
"""

# Runnable Example

from random import randint

# This is a one-line comment

"""
This is  multi-line comment.

We can spread this across as many lines as we need to
and it won't impact our computer program at all!!!
"""

def lottery_generator():
    """
    Appends ten random numbers to an empty list
    Returns the list
    """
    numbers = [] # Empty list to hold the numbers
    for number in range(0, 10):
		# randint() generates random integers
        numbers.append(randint(1, 50))
    return numbers

print(f"This weeks winning lottery numbers are {lottery_generator()}")

