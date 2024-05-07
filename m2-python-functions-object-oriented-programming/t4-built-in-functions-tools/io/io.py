# io 

"""
There are many basic in/out (I/O) functions in Python, with which some at least you are already familiar.
A print statement is the most basic output. You have also seen examples of taking input from a user with the 
input() function. These are, of course, only useful when using a command-line application where the input and 
output use the terminal. In real-world applications, you might also be reading from and writing to files on 
the computer where the code is running. We will cover this in more detail in an upcoming module.

In the runnable example, we have included a text file. The open() function is used to open this file and to let 
the computer know that this text file is currently in use by the main.py module. As we have assigned this to a 
variable f, we can then use the read() function to read the text and assign it to variable lines. We then use 
the close() function to close the file again. This is to ensure that other programs will be able to access it.
"""

# Runnable Example

f = open('source.txt')
lines = f.read()
f.close()
print(lines)

