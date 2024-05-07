# os.path()

"""
Within the os library, there is a module named path. This allows you to manipulate the pathnames on the operating system of the computer
on which you are running the code. This is useful when saving data to the local operating system. If you remember back to the CSS Essentials
lessons getting the correct relative or absolute pathname was vital in linking files. The os.path() methods allow you to dynamically create
path names so you can connect to files on the operating system and save files where you intend to.


In the runnable example, we have taken the absolute path and joined it with the current working directory. This uses the join() method of the 
path module. There is also a split() method allowing you to split a path. In this case, we have split the filename from the pathname and 
assigned them to a tuple. The splitext() method allows you to split the module name from its file extension.
"""

# Runnable example:

import os

# This is how you would join two paths in your code
print(os.path.join('/home/runner/', 'os'))

path = "/home/runner/os/main.py"
# Splits the path into a pair (head, tail) where the tail is the end of the pathname
# The tail is after the / and the head is the pathname up to that point 
(dirname, filename) = os.path.split(path)
print(f'The directory path is {dirname}')
print(f'The filename is {filename}')
# Splits the filename into a pair (root, ext)
# The root is before the dot and the ext contains the dot with the suffix after it
(module, extension) = os.path.splitext(filename)
print(f'The module is {module}')
print(f'Its file suffix is {extension}')


# Additional Perspectives From People We Like

# There are many more methods in os.path which can be found in the official python documentation.

# https://docs.python.org/3/library/os.path.html