# Controlling Iteration (Break, Continue & Pass)

""" 
Break: To stop the loop before it has looped through all the items.
Continue: To stop the current iteration and continue with the next.
Pass: To avoid getting an error when an empty block is not allowed.
"""

# Runnable Example 1
print("Runnable Example 1: break statement ")

for number in range(10):
    if number == 5:
        break    # break here

    print(f'Number is  {number}')

print('Left the loop')

# In this example, the loop will break when the number is equal to 5

# Runnable Example 2
print("Runnable Example 2: continue statement ")

for number in range(10):
    if number == 5:
        continue    # continue here

    print(f'Number is  {number}')

print('Left the loop')

# In this example, the loop will continue when the number is equal to 5

# Runnable Example 3
print("Runnable Example 3: pass statement")

for number in range(10):
    if number == 5:
        pass    # pass here

    print(f'Number is  {number}')

print('Left the loop')

# In this example, the loop will pass when the number is equal to 5
