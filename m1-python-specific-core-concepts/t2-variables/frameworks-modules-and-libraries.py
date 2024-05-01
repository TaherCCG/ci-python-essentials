""""
Function syntax example:

The multiplication() function is defined here, the paramaters
passed to it are named num1 and num2. And it returns the value
of the two numbers multiplied.
"""
def multiplication(num1, num2):
    return num1 * num2 
    # code inside a python function is indented by four spaces


""""
here the multiplication() function is called and passed the value of 
2 for num1 and the value of 3 for num2. So the multiplication function
will multiply 2 * 3 and return the value, which is stored in the
result1 variable. 
"""
result1 = multiplication(2, 3)
print(result1)

""""
here the multiplication() function is called and passed the value of 
4 for num1 and the value of 9 for num2. So the multiplication function
will multiply 4 * 9 and return the value, which is stored in the
result2 variable. 
"""
result2 = multiplication(4, 9)
print(result2)

""""
here the multiplication() function is called and passed the value of 
34 for num1 and the value of 99 for num2. So the multiplication function
will multiply 34 * 99 and return the value, which is stored in the
result3 variable. 
"""
result3 = multiplication(34, 99)
print(result3)

"""
Try changing the values passed to the multiplication function to
see the how the value returned from it changes.
"""

result4 = multiplication(5, 99)
print(result4)

result5 = multiplication(34, 5)
print(result5)


print("addition function results below:")

def addition(num1, num2):
    return num1 + num2 

result6 = addition(34, 5)
print(result6)

result7 = addition(34, 99)
print(result7)

result8 = addition(5, 5)
print(result8)