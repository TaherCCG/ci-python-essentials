# Taking Parameters and Returning Results Challenge

"""
1.  Define a function named add_numbers that takes two parameters named: nums_tuple, min_value
2.  The function should return the sum of all the values in the nums_tuple that are greater or equal to the min_value
3.  Outside of the function
4.  Create a variable named: total and assign it the return value from calling the add_numbers function and passing in the two arguments: (21, 4, 7, 19, 1), 15
5.  print total
"""

def add_numbers(nums_tuple, min_value):
    total = 0
    for num in nums_tuple:
        if num >= min_value:
            total += num
    return total

total = add_numbers((21, 4, 7, 19, 1), 15)
print(total)


print("\n\n\n")
print ("Refactored code")

def add_numbers(nums_tuple, min_value):
    return sum(num for num in nums_tuple if num >= min_value)

total = add_numbers((21, 4, 7, 19, 1), 15)
print(total)