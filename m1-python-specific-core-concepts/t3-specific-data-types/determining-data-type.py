"""Determining the Data Type

Python has the following data types built-in by default, in these categories:

1. Text Type:	str
2. Numeric Types:	int, float, complex
3. Sequence Types:	list, tuple, range
4. Mapping Type:	dict
5. Set Types:	set, frozenset
6. Boolean Type:	bool
7. Binary Types:	bytes, bytearray, memoryview
You can get the data type of any object by using the type() function:"""

print(type("Hello, World!"))
print(type(42))
print(type(3.145))
print(type(1j))
print(type(["egg", "bacon", "spam"]))
print(type(("egg", "bacon", "spam")))
print(type(range(6)))
print(type({"name" : "John", "age" : 80}))
print(type({"egg", "bacon", "spam"}))
print(type(True))
print(isinstance(3.14, int))


"""
To ascertain the type of any object you can use the built-in type() function. This function will give you the type. 
However, if you want to run a check on the type, you can use isinstance() which will return True or False. 
In the example below both my_var and 2 are integers so type() will return <class 'int'> and isinstance() will return True.
"""

print("my_var = 2")
my_var = 2
print(type(my_var))
print(type(2))
print(isinstance(my_var, int))