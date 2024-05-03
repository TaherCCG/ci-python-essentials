# Sets

"""Set is a collection of unique elements. It is unordered and unindexed.
Sets are written with curly brackets {}.
Sets are mutable, meaning you can change the items after the set has been created.
You cannot access items in a set by referring to an index, since sets are unordered the items have no index.
You can loop through the set items using a for loop.
You can add items to a set using the add() method.
You can remove items from a set using the remove() method.
You can use the len() method to determine the number of items in a set.
You can use the clear() method to empty a set.
You can use the del keyword to delete the set completely.
You can use the set() constructor to create a set.
"""

# Runnable Example: Sets
print("Sets")
print()

breakfast = {'bacon', 'egg', 'spam', 'spam', 'spam', 'spam', 'spam'}
print(breakfast)
print('egg' in breakfast)
breakfast.add('sausage')
print(breakfast)
breakfast.update(['Lobster Thermidor', 'truffle pate', 'crevettes', 'shallots','aubergines'])
print(breakfast)
breakfast.discard('aubergines')
print(breakfast)

print()
# Set Operators
print("Set Operators")
print()
hello = set("Hello")
world = set("World")
print(f"The unique letters in hello are: {hello}")
print(f"The letters in hello or world or both are: {hello|world}") # | is the symbol for union
print(f"The letters in both hello and world are: {hello&world}") # & is the symbol for intersection
print(f"The letters in hello but not world are: {hello-world}") # - is the symbol for difference
print(f"The letters in hello and world but not both are: {hello^world}") # ^ is the symbol for symmetric difference
