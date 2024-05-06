# Writing simple Functions in Python
print ("Writing simple Functions in Python")

# Function that takes 2 numbers, adds them together and returns the result.
print ("Function that takes 2 numbers, adds them together and returns the result.")
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum

result = add_two_numbers(10, 30)
print(result)

# Function that takes 3 numbers, multiples them together and returns the result.
print ("Function that takes 3 numbers, multiples them together and returns the result.")
def multiply_three_numbers(num1, num2, num3):
    product = num1 * num2 * num3
    return product

result = multiply_three_numbers(2, 3, 4)
print(result)

# Function that takes one number and returns its value squared (the number times itself)
print ("Function that takes one number and returns its value squared (the number times itself)")
def square_number(num):
    square = num * num
    return square

result = square_number(5)
print(result)


# Function that takes 2 numbers, and returns the value of the first number divided by the second number
print ("Function that takes 2 numbers, and returns the value of the first number divided by the second number")
def divide_two_numbers(num1, num2):
    divide_two = num1 / num2
    return divide_two

result = divide_two_numbers(10, 2)
print(result)

