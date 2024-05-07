# Try & Except Statements

"""
In the last example, we handled the error by telling the user that they had not entered a number. No exception, however, was raised 
so there is no record of the error. As a developer, you might want to record the incidence of this error, so perhaps you can improve 
your UX. In a case where it is not user data entry but a file, you might want to record how many data points are bad. To do this, you
can raise an exception in the except block.

If we return to the previous example, we have added ValueError to the except statement. This is one of the built-in exceptions in Python.
It is more specific than RuntimeError, and we have used it as we know in this case, an inappropriate value input causes an error. If you 
run the code now, you will see the exception is raised, and the except code block is run.


while True:
    try:
        x = int(input('Enter a number.'))
        print(f'Number is {x}')
    except ValueError:
        print('Not a number')


Run this code
In some cases, you may anticipate more than one type of error. Python allows you to have multiple except statements. In the runnable 
example, we have three except blocks. If more than one is valid, the first exception raised is the one you’ll see. Here we check for
division by zero and an inappropriate value entered. Try both to see what happens. If another error occurs that the first two except
blocks don’t catch then the third block catches it. To test this, you can provoke an error by trying ctrl-c in the terminal.
"""

# Runnable Example:

while True:
    try:
        a = int(input("Please enter an integer as the numerator: "))
        b = int(input("Please enter an integer as the denominator: "))
        print(a / b)
    except ZeroDivisionError:
        print("Please enter a valid denominator.")
    except ValueError:
        print("Both values have to be integers.")
    except Exception:
        print('Another error has occurred')