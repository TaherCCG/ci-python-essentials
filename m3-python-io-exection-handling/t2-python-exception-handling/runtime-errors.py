# Runtime Errors

"""
Python error messages are called exceptions. When an error occurs, an exception is raised. All exceptions are instances of a class
BaseException. The exceptions can be generated either by the interpreter while running the code or by functions in the code. As a 
developer, you can raise these exceptions to deal with errors caused by incorrect user input, for example. There are many specific 
exceptions in Python; for example, ZeroDivisionError raised when the second argument of a division or modulo operation is zero. 
However, if an error does not fall into one of these specific categories, a RuntimeError will be raised. The associated string will
explain what has gone wrong.


In the runnable example, the code will print text to the terminal if 1 or 2 is entered. However, what happens if a user enters another
number or a string instead? In the else, we have used the keyword raise to raise a RuntimeError exception if this happens. A RuntimeError 
is posted in the terminal, but it is not particularly informative. Also, our program has still crashed. In the next units, we see how to 
handle these errors without crashing the program and how to get a more informative error message.

"""

# Runnable Example

def choices(n):
    if n == 1:
        print("First item chosen")
    elif n == 2:
        print("Second item chosen")
    else:
        raise RuntimeError

choices(3)
