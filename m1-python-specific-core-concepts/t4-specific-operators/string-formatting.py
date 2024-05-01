# String Formatting
"""
String formatting provides a more powerful way to embed non-strings within strings. 
String formatting uses a string's format method to substitute a number of arguments in the string.

In addition to the use of the + operator, to append a string to the end of another string, we also 
have other ways of formatting a string.The more advanced form of doing string formatting is by using 
what are called; f-strings.

When formatting with f-strings, you would do the following:

f"{variable}"

It is also valid to use the capital letter F The only consideration required to use f-strings is your 
version of python, which needs to be version 3.6 or above.

In the example below, you will see that when using the f-string formatting methods, 
you do not need to convert the number to a string as python converts it for you.
"""

name = input("What's your name? ")
# Here we don't need age to be a number as we are not
# going to do any calculations with it so we don't need to wrap the
# input() in the str() method
age = input("What's your age: ")

# The Modern way of formatting a string
print(f"Hello {name}, you are {age} years old")

