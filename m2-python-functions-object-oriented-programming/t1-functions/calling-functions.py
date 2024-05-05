# Calling a function

# Define a function that prints a message to the console
def greet():
    print("Hello, World!")

# Call the function
greet()
# Output: Hello, World!

"""
A function is a block of code that only runs when it is called. Calling a function is executing the code. When you defined a function, 
you used the def keyword but to call it you simply use the function name followed by parentheses. You can pass information into the 
function as arguments inside the parentheses separated by commas. A parameter is the variable listed in the parentheses when the function 
is defined, and the argument is the value you pass into the function parentheses when it is called. You have to supply the same number of 
arguments as there are parameters. A function can be called by another function or even by itself.
"""

"""Python functions must be declared and defined before they are called.
Note that both functions, in this case, are themselves calling other functions.
This is a common pattern in programming, where you have a main function that calls other functions to perform specific tasks.
This is a good way to organize your code and make it more readable and maintainable.
"""

# 2. This function runs for the name and age function calls
def get_user_input(prompt):
    return input(prompt)

# 4. This function runs twice
def print_out_to_console(value_to_be_printed):
    print(value_to_be_printed)

# 1. name and age are the first two function calls to run sequentially
name = get_user_input("Input your name:")
age = get_user_input("Input your age:")

# 3. Then function calls run sequentially
print_out_to_console(f"Your name is {name}")
print_out_to_console(f"You are {age} years old")
