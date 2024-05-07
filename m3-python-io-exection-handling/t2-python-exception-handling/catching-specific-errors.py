# Catching Specific Errors

"""
In addition to the basic RuntimeError, you have seen the use of ValueError and ZeroDivisionError. These are more specific exceptions 
provided by Python. When writing your code, it is essential to think about what possible errors might happen and how to handle them. 
It is a good idea to test your code as you go. What happens when you enter incorrect values for your function arguments, for example?
Using more specific exceptions can make it quicker to debug what has gone wrong with your code. When you raise an exception, you can 
include a string of text to provide information pertinent to your code.

If we return to the previous example, we see that multiple specific exceptions can be included in one except block if they are added to 
a tuple in the except statement."""

while True:
    try:
        a = int(input("Please enter an integer as the numerator: "))
        b = int(input("Please enter an integer as the denominator: "))
        print(a / b)
    except (ZeroDivisionError, ValueError):
        print('An error has occurred')
        


"""
try:
    for i in range(5, -5, -1):
        if i < 0:
            raise Exception('Integers must be positive.')
        else:
            print(i)
except:
    x = [1, 2, 3,"hello"]
    for item in x:
        if not type(item) is int:
            raise TypeError("Only integers are allowed")
        else:
            print(item)
"""