# Third Party Libraries

"""In addition to the built-in libraries, as Python is open source, anyone can create software and share it with the community.
A library is a collection of modules that have some common functionality. There is a Python Package Index (pypi.org) where these 
open source projects are shared.

library
In the runnable example, we are using a third-party library named numpy. It is a widely used library for scientific computing. 
We can give the package name an alias (np in this case), so we don’t have to type it out each time. Numpy extends the abilities 
of Python into scientific computing. Here we are creating a simple one-dimensional array. The repl.it already has numpy installed.
If you were trying this on your computer, you would have to install numpy locally as it is a third-party library rather than a 
built-in library installed with Python.

"""

# Runnable example:

import numpy as np 

a = np.array([1, 2, 3])

print(a)