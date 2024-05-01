# Original code that needs to be modified:
# It throws an error because we are trying to concatenate a string with an integer.

"""
result = 40 + "2.2"
print(result)

result_two = "The answer to the ultimate question is " + 42
print(result_two)
"""

# Solution:

result = 40 + float("2.2")
print(result)

result_two = "The answer to the ultimate question is " + str(42)
print(result_two)

# Output:
# 42.2
# The answer to the ultimate question is 42