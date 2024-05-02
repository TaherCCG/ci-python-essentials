# Equality vs. Identity

""" 
    - Equality: Compares the values of the objects.
    - Identity: Compares the memory locations of the objects.
    
    Python has two comparison operators for checking equality and identity.
    is: Returns True if both variables are the same object.
    is not: Returns True if both variables are not the same object.
"""

# example 1
num = 1
num_two = num
num == num_two
id(num)
id(num_two)


# example 2
num = 1
num_two = num
num is num_two

# example 3
num = 1
bool = True
num == bool
num is bool

# example 4
a=1
b=1.0
print(a==b)
print(a is b)
print(id(a))
print(id(b))
# a and b have the same numeric value but a different type
c=b
print(b==c)
print(b is c)
print(id(b))
print(id(c))
# b and c are equal in value and identity
