# Returning Data to a User

"""
In a command-line Python, program output can be given in several ways. One example is simple statements. An expression statement can be 
used to compute and write a value. You will also have seen statements in the terminal when an error occurs. These are assertion and raise
statements. We will see more of those in the upcoming error handling units. In the io unit, you saw that output could also write to a file. 
We will cover this in more detail in an upcoming unit. The most frequently used output you have seen is the print function. This allows you
to output data in a human-readable format.

Let’s look at fancier ways to format our output. The most basic output is a statement. In this case, we have a simple one-line expression 
(10 + 20) which is assigned to a variable i. When we print this to the console it is considered to be a statement.

Formatted string literals are a way to improve the human readability of the output. We have assigned a string to variable language and an 
integer to variable version. With string literals, we can pass these values directly to the print statement with no need to convert data types.
This can also be done with expressions. The value of pi from the math library is expressed within the print statement. A format specifier can 
be included after the colon. In this case, the value is rounded to two significant figures. If instead of a format specifier an integer is 
placed after the colon, the field will be set to a minimum character value equal to the integer value. Here we have chosen 25 to take into 
account the longest string.

When including a non-keyboard character such as the pound sterling, it can be done by using the chr() and the Unicode value (163 in this case).

"""

# Runnable Example

import math

i = 10 + 20
print(i)
language = "Python"
version = 3
print(f'We are using {language}{version}')
# Here the format specifier .2f is used to truncate at 2 decimal places
print(f'The value of pi to 2 decimal places is {math.pi:.2f}')
# The currency symbol for pounds sterling has Unicode character number 163
pound = chr(163)
tabulate = {'Egg & Spam': 1, 'Egg, Bacon & Spam': 1.5, 'Egg, Bacon Sausage & Spam': 2, }
# Loops over a dictionary of menu items as keys and prices as values
for item, price in tabulate.items():
    # The format specifiers here denote a minimum width of 25 and 5 characters
    print(f'{item:25} - {pound}{price:5}')


"""
This runnable example includes expressions within the formatted string literals. Additionally, the newline (\n) is used to add a new 
line after the second print statement. This also helps make the output easier to read.
"""

# Runnable Example 2

for number in range(99, 0, -1):
    line_one = f"{number} bottle(s) of beer on the wall. {number} bottle(s) of beer"
    line_two = f"Take one down, pass it around. {number-1} bottle(s) of beer on the wall\n"

    print(line_one)
    print(line_two)
