# Integers, Floats & Decimals

"""
Integers
Integers are whole numbers, positive or negative, without decimals, of unlimited length.
Integers are a built-in data type in Python.
"""

# Integers in Python:
print("Integers in Python:")
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

"""
Floats
Floats are real numbers, positive or negative, containing one or more decimals.
Float can also be scientific numbers with an "e" to indicate the power of 10.
"""

# Floats in Python:
print("Floats in Python:")
x = 1.10
y = 1.0
z = -35.59

# Floats can also be scientific numbers with an "e" to indicate the power of 10.

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

"""
Decimals
Decimals are numbers that are used in precision mathematical calculations.
The decimal module provides support for fast correctly-rounded decimal floating point arithmetic.
It offers several advantages over the float datatype.
"""

# Decimals in Python:
print("Decimals in Python:")
import decimal

x = decimal.Decimal(10)
y = decimal.Decimal(0.1)

print(type(x))
print(type(y))

# Note: To use the decimal module, you have to import it first using: import decimal


"""
Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods:
"""

# Convert from one type to another:
print("Convert from one type to another:")
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Note: You cannot convert complex numbers into another number type.
