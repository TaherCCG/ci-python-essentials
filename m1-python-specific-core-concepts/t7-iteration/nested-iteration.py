# Nested iteration

"""
Nested iteration is when you have a loop inside another loop. 
This is useful when you need to iterate over a sequence of items that are themselves sequences.
The inner loop will run to completion for each iteration of the outer loop.
"""

# Runnable Example 1
print("Runnable Example 1: Nested iteration")

i = 2
while i < 10:
    j = 2
    while j <= i/j:
        if not i % j:
            break
        j += 1
    if j > i/j:
        print(f'{i} is a prime number')
    i += 1

"""
In this example, we have a while loop inside another while loop
The outer loop will run from 2 to 9
The inner loop will run from 2 to the square root of i
If i is divisible by j then it is not a prime number
If i is not divisible by j then it is a prime number
The inner loop will run to completion for each iteration of the outer loop
"""