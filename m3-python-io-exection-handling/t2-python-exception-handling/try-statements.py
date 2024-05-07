# Try Statements

"""
In the previous unit, we saw that we could raise an error when a user does something unexpected. However, the program still crashed. 
It is better to catch and handle these exceptions in such a way that your application continues to run. Python has a try block in which 
you put code where you anticipate an error could occur. Often this is where you foresee an issue caused by a users input or corrupt
data in a file. The program runs any code after the try statement in the usual manner. However, if an error occurs rather than raise an 
exception in the terminal, it runs code in a following except block. After the except statement, you write the code for what you want 
to do in cases where an error occurs. If this is user input, it might just be a message to the user that the data was invalid and please 
try again. If it is data from a file, then you might just skip the bad data points and carry on. In summary, the try block allows you to
test a code block for errors.

In the runnable example, we have asked the user for a number. 
This code block is wrapped in a try block and runs exactly as though the try block was not there as long as the user enters numbers.
However, if the user enters a letter, for example, there is an error, and the except block code is run. 
In this case, we just print ‘Not a number’, but crucially the code keeps running and asks the user for input again. 
The error is caught and handled. This is a simple example, but in more complex programs, you can catch and handle many different 
types of errors. We will see more examples of this in the next units.
"""

# Runnable Example

while True:
    try:
        x = int(input('Enter a number.'))
        print(f'Number is {x}')
    except ValueError:
        print('Not a number')