# Dictionaries

""" Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is unordered, changeable and does not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values.
You can recognise dictionaries by their curly braces { and } that enclose key-value pairs.
Dictionaries are similar to associative arrays in other programming languages.
You can create a dictionary by placing key-value pairs inside curly braces, separated by commas. For example:

my_dict = { 'name': 'Alice', 'age': 25, 'city': 'New York' }

Dictionaries are useful when you want to store data in a structured way, where each value is associated with a unique key.
You can access items in a dictionary using square brackets and the key, for example my_dict['name'].
You can also use the get() method to access items in a dictionary.
Dictionaries support various operations such as adding, updating, and deleting items.

"""

# Runnable Example: Dictionaries in Python
print("Dictionaries in Python")
print()

user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

print(user)
print(user['age'])
user['home'] = 'Withywindle, Middle-Earth'
user['age'] = 99
print(user)
del user['home'] 
print(user)
print(list(user))
print(sorted(user))
print(user)
print('username' in user)
