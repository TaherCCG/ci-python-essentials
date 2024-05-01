# Incrementing & Decrementing

"""The ways these operators work is by combining the arithmetic operator with the = assignment operator, 
as in the image to the left. We can use these operators for some shorthand operations.

The += is used to increment a variable by adding a value and reassigning the result to the variable.

The same syntax is used for subtraction, multiplication, division, exponent, modulo and floor division.

see below for the full list of assignment operators.

Addition AND  +=
Subtraction AND  -=
Multiplication AND  *=
Division AND  /=
Exponent AND  **=
Modulo AND  %=
Floor Division AND  //=
Bitwise AND  &=
Bitwise OR  |=
Bitwise XOR  ^=
Bitwise right shift  >>=
Bitwise left shift  <<=
"""

"""Incrementing
incrementing means to increase the value of a variable by a certain amount."""
print("Incrementing")
x = 5
x += 1
print(x)  # Output: 6

"""Decrementing
decrementing means to decrease the value of a variable by a certain amount."""
print("Decrementing")
x = 5
x -= 1
print(x)  # Output: 4

"""Multiplication
Multiplication is the process of adding a number to itself a certain number of times."""
print("Multiplication")
x = 5
x *= 2
print(x)  # Output: 10

"""Division
Division is the process of dividing a number by another number."""
print("Division")
x = 5
x /= 2
print(x)  # Output: 2.5

"""Exponent
Exponentiation is the process of raising a number to a power."""
print("Exponent")
x = 5
x **= 2
print(x)  # Output: 25

"""Modulo
Modulo is the process of finding the remainder of a division operation."""
print("Modulo")
x = 5
x %= 2
print(x)  # Output: 1

"""Floor Division
Floor division is the process of dividing a number by another number and rounding down to the nearest whole number."""
print("Floor Division")
x = 5
x //= 2
print(x)  # Output: 2

"""Bitwise AND
Bitwise AND is the process of performing a bitwise AND operation on two numbers. 
The result is a number that has a 1 in each position where both numbers have a 1."""
print("Bitwise AND")
x = 5
x &= 2
print(x)  # Output: 0

"""Bitwise OR
Bitwise OR is the process of performing a bitwise OR operation on two numbers."""
print("Bitwise OR")
x = 5
x |= 2
print(x)  # Output: 7

"""Bitwise XOR
Bitwise XOR is the process of performing a bitwise XOR operation on two numbers."""
print("Bitwise XOR")
x = 5
x ^= 2
print(x)  # Output: 7

"""Bitwise right shift
Bitwise right shift is the process of shifting the bits of a number to the right by a certain number of positions.
"""
print("Bitwise right shift")
x = 5
x >>= 2
print(x)  # Output: 1

"""Bitwise left shift
Bitwise left shift is the process of shifting the bits of a number to the left by a certain number of positions."""
print("Bitwise left shift")
x = 5
x <<= 2
print(x)  # Output: 20


# Runnable example:
variable_one = "hello "
variable_two = "world"

variable_one += variable_two
print(variable_one)
print(variable_two)

x = 2
x *= 3
print(x)