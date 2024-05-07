# Reading Data From a User

"""
When working with computers, we use what is called an interface to interact with the computer. We’re all familiar with working 
with Graphical User Interface (GUI). The GUI is where we execute applications from our Desktop, opening folders from My Computer, 
creating Documents in Microsoft Office, and browsing the web with Chrome or Firefox. While we’re working with Python, and providing 
output to a user, we’re using the Command Line Interface or CLI. This interface is text-based, as opposed to the graphics-based 
interface we’re all used to seeing, but just remember that all we’re doing is taking input and outputting information to the user.

With that in mind, let’s take a look at how we can receive some input from a user. For this, we’ll need to use the input function. 
The input function takes a string as an argument. This is the prompt the user will see. The input function stops the running of the 
program and waits for the user to enter data in the command line and press return. Whatever the user inputs is converted to a string. 
Therefore if you need it as a number, you need to convert it.

"""

# Runnable Example

username = input("Type in your name and press return: ")
# The programme will remain stopped until you respond to this prompt with some text and press the return key
# As the value type that is received from an input is a string
# We need to convert it to a number to be able to use it on line 7
# We can do this by wrapping the input inside the int() method
age = int(input("Please enter your age: "))

days = 365 * age
# days is a number
# To concatenate it to the string we have to convert it to a String
# Notice below we do this like: str(days)
print("Hello " + username + ", you have been alive for at least " + str(days) + " days")