# Else & Finally Statements

"""
The try-except has an optional else clause. This is placed after all of the except clauses and deals with any code that must be
executed in the case where the try clause does not raise an exception. The code placed in the try block should only be the code 
where you are anticipating the exception. Any other code that should run along with it should be placed in the else block.
There is an additional optional clause finally, which is the last clause to run. It runs whether or not an exception has been raised.
It is intended for any ‘clean-up’ code that must run regardless of whether an exception was caught or not.

else finally
In the runnable example, we have a function that opens a text file, counts the lines and prints the opening line of the file. 
The try block catches if a file does not exist and the except block deals with the error so that the program does not crash.
The else block deals with the code that should run in the case of no error (the file exists). The finally block runs whether 
or not the file exists. Here it just lets the user know that the function has complete. Note that it runs after the try,
except and else blocks.

"""

# Runnable Example

def linecount(filename):
    """
    Counts the lines in a text file.
    Prints the opening line of a text file. 
    """
    try:
        f = open(filename, 'r')
        s = f.readlines()
    except OSError as e:
        # OSError exception is used as it deals with system errors such as I/O errors
        # OSError returns an error code (errno) and message (strerror)
        errno, strerror = e.args
        print(f"There is an I/O error number, {errno}: {strerror}.")
    else:
        # This is the code that does the line counting
        print(f'{filename} is {len(s)} line long.')
        print(f"The opening line of {filename} is '{s[0]}'")
        f.close()
    finally:
        # This will print whether the line count has been successful or not
        print(f'Finished with {filename}.')
    
linecount('gulliver.txt')
print("\n")
linecount('swift.txt')


"""
As you are already aware when using IO, you always should close the file when you are finished working on it. As this is such an
important issue, Python has included a with statement to deal with it. Behind the scenes, it is in effect a type of try-finally statement.

f = open(filename)
try:
    # My Code
finally:
    f.close()
    
In reality, what is happening is that special methods __enter__ and __exit__ are used.

f = open()
f.__enter__()
try:
    # My Code
finally:
    f.__exit__()
    
You do not need to type any of this code. Just use the with statement as follows.

with open(filename) as f:
    #My Code
As you can see we have refactored the code to use this syntax. No explicit file close statement is required.

"""

# Runnable Example 2
print("Example 2:\n")

def linecount(filename):
    """
    Counts the lines in a text file.
    Prints the opening line of a text file. 
    """
    try:
        with open(filename, 'r') as f:
            s = f.readlines()
    except OSError as e:
        errno, strerror = e.args
        print(f"There is an I/O error number, {errno}: {strerror}.")
    else:

        print(f'{filename} is {len(s)} line long.')
        print(f"The opening line of {filename} is '{s[0]}'")
    finally:
        print(f'Finished with {filename}.')
        
linecount('gulliver.txt')
print("\n")
linecount('swift.txt')

