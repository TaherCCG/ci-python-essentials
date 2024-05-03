# Multiple Conditions (If/Elif/Else)

"""Python Multiple Conditions (If/Elif/Else)
In Python, you can use the if, elif, and else statements to handle multiple conditions.
The elif statement allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions is TRUE.
If none of the conditions are TRUE, the else block of code will be executed.

Syntax:
if condition1:
    # code block
elif condition2:
    # code block
else:
    # code block
"""


# Example 1: Check if a number is greater than, less than, or equal to 5
number = int(input("Please enter a number:"))

if number > 5:
    print(f"{number} is greater than 5")
elif number < 5:
    print(f"{number} is less than 5")
else:
    print(f"{number} is not greater than, or less than 5. Therefore, {number} must be equal to 5.")

# Example 2: Check if a number is positive, negative, or zero
number = int(input("Please enter a number:"))

if number > 0:
    print(f"{number} is a positive number")
elif number < 0:
    print(f"{number} is a negative number")
else:
    print(f"{number} is zero")

