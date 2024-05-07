# Catching Generic Errors With “as”

"""
The built-in exceptions contain information about the error. Up till now, we have just displayed the exception in the terminal. 
The exception object includes the error message and also additional arguments.

In this example, we have passed the UnicodeError exception to a variable e. Then we have access to the various attributes.

def encode_name(name):
    try:
        name = name.encode('ascii')
    except UnicodeError as e:
        print(f'The name {e.object} has a character at position {e.start} that cannot be encoded in {e.encoding} due to {e.reason}')
    return name
    
encode_name('Stéfan')
Run this code
In the runnable example below there is no file book.txt, so the except block runs. The exception OSError is passed to variable e, 
so we have access to the arguments. The OSError exception is for operating system errors such as file not found. Then we pass the 
arguments to a tuple with variable names errno and strerror. These are the numeric error code and corresponding error message 
respectively. We could also have used the filename argument, for example.

"""

# Runnable Example

try:
    f = open('book.txt')
    s = f.readline()
except OSError as e:
    errno, strerror = e.args
    print(f"There is an I/O error number, {errno}: {strerror}.")
