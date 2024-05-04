# Iterating Python Data Structures

"""In the for-loops unit, we saw how to iterate over strings and lists. The simplest case is to use the in keyword to iterate through 
the string or list. We also looked at using integers as indexes for the list. This could be done using range() and len()




"""


# Runnable code examples: Iterating over a Dictionary using items()

print("Iterating over a Dictionary using items()")
user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

for key, value in user.items():
    print(f"Key: {key}")
    print(f"Value: {value}")
    print("------------------")

# In the above example, we are iterating over the dictionary user. We are using the items() method to get the key-value pairs.


# Runnable code examples: Iterating over a Set

print("Iterating over a Set")

# Create a set
directions = set(['north', 'south', 'east', 'west'])

# Print its members
for direction in directions:
    print(direction)

# Add an item to the set:
directions.add('northwest')

print()
# Print the members again
# Notice the order cannot be relied upon!
for direction in directions:
    print(direction)
    
"""
In the above example, we are iterating over the set directions. We are using the for loop to iterate over the set. The order of the
elements in the set cannot be relied upon. The order of the elements in the set is not guaranteed to be the same as the order in which
they were added to the set.
"""

