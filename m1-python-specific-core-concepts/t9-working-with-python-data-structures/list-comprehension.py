# List comprehension

""" List comprehension is a concise way to create lists. It is a way to create a new list by 
applying an expression to each item in an existing list. 

It is commonly used where you want to generate a list based on an operation or to create a new sub-list of an existing list.
"""

# Let's compare the list comprehension syntax with what you’ve seen before.

numbers = []
for x in range(10):
    numbers.append(x)
# This same code could be written as a list comprehension.

numbers = [x for x in range(10)]
# This is a more straightforward cleaner way to write the list. The list comprehension can also include additional logic. Here's a much more complex example.

combination = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combination.append((x,y))
# This code returns [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)] which is a list of tuples.This can be done in one line:

combination = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


# Runnable code examples: List Comprehension
print("List Comprehension")

# 1. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([i for i in range(10)])

# 2. [0, 2, 4, 6, 8, 10]
print([i for i in range(0,11,2)])

# 3. [0, 1, 4, 9, 16, 25, 36, 49]
print([x**2 for x in range(0,8)])

# 4. [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print([((i,(i+1))) for i in range(5)])

# 5. ['woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo']
print(['woohoo' for i in range(7)])

# 6. ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
hw = 'hello world'
print([i for i in hw])

# 7. [('A', 'D'), ('A', 'E'), ('A', 'F'), ('B', 'D'), ('B', 'E'), ('B', 'F'), ('C', 'D'), ('C', 'E'), ('C', 'F')]
ab = 'ABCDEF'
print([(ab[i],ab[j]) for i in range(0,3) for j in range(3,6)])

# The list comprehension is a powerful tool that can be used to create lists in a concise way. 
# It is a great way to create lists based on an operation or to create a new sub-list of an existing list.

