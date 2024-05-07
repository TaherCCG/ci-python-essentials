# os

"""
The os library provides a way of using the operating system (os) functionality. The operating system is the software that interfaces 
between the hardware and user on a computer. Common operating systems would be Windows, macOS, Linux or iOS. A frequent use for this 
would be accessing the environment variables. Every computer has a set of environment variables listing information on how the machine 
is set up. Examples of this would be the directory structure of the home directory or the computers users profile.


In the runnable example, we use the get current working directory function getcwd() to find the directory in which the python file is 
located. We can also list the files or directories listdir() within a directory.
"""

# Runnable example:

import os

print(os.getcwd())
print(os.listdir('/home/user'))
