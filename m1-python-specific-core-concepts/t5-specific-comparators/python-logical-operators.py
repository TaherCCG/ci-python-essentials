# Python logical operators

""" 
Logical operators are used to combine conditional statements.

If you want to combine multiple comparisons, then you need logical operators. This is useful when you have to meet more than one comparison in a program. Logical operators apply to the Boolean values of True and False.

Python Logical Operators

Operator        |	Description	                                            | Example
============================================================================================

and	            |   Returns True if both statements are true	            |    x < 5 and x < 10
or	            |   Returns True if one of the statements is true	        |    x < 5 or x < 4
not	            |   Reverse the result, returns False if the result is true	|    not(x < 5 and x < 10)

"""

print(True and True)
print(True and False)
print(True or False)
print(not (4 < 5 and 4 < 10))

# Other examples
print("Other examples:")
print(2<3 and 3<4)              # True and True
print(2>3 or 3>4)               # False or False
print(not(2<3 and 3<4))         # not(True and True) = not(True) = False
print(not(2>3 or 3>4))          # not(False or False) = not(False) = True
print(not(2>3 and 3>4))         # not(False and False) = not(False) = True
print(not(2<3 or 3<4))          # not(True or True) = not(True) = False
print(2<3 and 3<4 and 4<5)      # True and True and True
print(2>3 or 3>4 or 4>5)        # False or False or False
print(not(2<3 and 3<4 and 4<5)) # not(True and True and True) = not(True) = False
print(not(2>3 or 3>4 or 4>5))   # not(False or False or False) = not(False) = True
print(not(2>3 and 3>4 and 4>5)) # not(False and False and False) = not(False) = True    
print(not(2<3 or 3<4 or 4<5))   # not(True or True or True) = not(True) = False
