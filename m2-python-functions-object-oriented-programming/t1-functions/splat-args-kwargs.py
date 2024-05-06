# Splat! *args & **kwargs
# *args and **kwargs allow you to pass a variable number of arguments to a function.

# *args is used to send a non-keyworded variable-length argument list to the function. It allows you to pass a variable number of arguments to a function.
# **kwargs allows you to pass keyworded variable-length of arguments to a function. You should use **kwargs if you want to handle named arguments in a function.

"""
In a function, you can list the parameters separated with commas. An elementary function is one that takes parameters a, b and adds their 
argument values together. This function is then reusable as you can add any two numbers together. But what if you want to add three numbers 
together? One possible solution is to pass in a list as an argument containing all the numbers you wish to add. This does require you though 
to have created the list in advance. This is inconvenient. The purpose of *args is to allow you to pass in a varied number of positional 
arguments. The iterable object *args can be renamed to any other name as long as it is preceded by the unpacking operator *. Rather than a 
list, the *args operator is a tuple so is immutable and needs to be unpacked to use the values.


The **kwargs object behaves very similarly but rather than a tuple is a dictionary. Like with *args you can change the name as long 
as the ** unpacking operator precedes it. Where you would use **kwargs over *args is when you have a keyword or named arguments.
"""

# Python Function Arguments
# 1. Default Arguments
# 2. Keyword Arguments
# 3. Arbitrary Arguments, *args
# 4. Arbitrary Keyword Arguments, **kwargs

# *args

def addition(a, b):
    return a + b

print(addition(2,2))

def add_integers(list_integers):
	total = 0
	for x in list_integers:
		total += x
	return total

list_integers = [1, 2, 3, 4]
print(add_integers(list_integers))

def add_many_integers(*integers):
	# Rename *args to something suitable
	total = 0
	for x in integers:
		# As it is a tuple you can use the in keyword to iterate 
		total += x
	return total

print(add_many_integers(1,2,3,4,5,6,7,8,9))

def concatenate_words(**words):
	result = ""
	# As **kwargs is a dict you need to iterate over .values()
	for arg in words.values():
		result += arg
		result += " "
	return result

print(concatenate_words(a='This', b="is", c="a", d="useful", e="feature"))

"""
In the above example, we have a function called concatenate_words that takes in a variable number of keyword arguments.
We then iterate over the values of the dictionary and concatenate them together with a space in between them.
The result is then returned. The function is called with five keyword arguments, and the result is printed to the console.
"""
