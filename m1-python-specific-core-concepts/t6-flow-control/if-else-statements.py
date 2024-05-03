# If-Else Statements

""" Python If-Else Statements
If-Else statements are used to execute a block of code based on a condition. 
If the condition is true, the code inside the if block will be executed. 
If the condition is false, the code inside the else block will be executed.

Syntax:
if condition:
    # code block
else:
    # code block
"""

# Example 1: Check if a number is equal to 5
number = int(input("Please enter a number:"))

if number == 5:
    print(f"{number} is equal to 5")
else:
    print(f"{number} is not equal to 5")


# Example 2: Check if a number is even or odd
number = int(input("Please enter a number:"))

if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
    
