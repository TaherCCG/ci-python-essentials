# Getting & Setting Dictionary Items

""" 
Getting Dictionary Items
To access a dictionary item, you can use the get() method or the square bracket syntax([]).
The get() method returns the value of the specified key. If the key does not exist, it returns None.
The square bracket syntax([]) also returns the value of the specified key. If the key does not exist, it raises a KeyError.

Setting Dictionary Items
To set a dictionary item, you can use the square bracket syntax([]) or the update() method.
The square bracket syntax([]) allows you to set the value of a key directly.
The update() method allows you to update the dictionary with the specified key-value pairs.
"""

# Runnable Example: Getting and Setting Dictionary Items
print("Getting and Setting Dictionary Items")
print()

keys = ['username', 'first_name', 'last_name', 'age']
default_value = ''
user = dict.fromkeys(keys, default_value)
print(user)
user['username'] = 'tombombadil'
user['first_name'] = 'Tom'
user['last_name'] = 'Bombadil'
user['age'] = 100
print(user)
print(user['age'])
print(user.get('home', "doesn't exist"))
user['home'] = 'Withywindle, Middle-Earth'
user['age'] = 99
print(user)
del user['home'] 
print(user)
print(list(user.keys()))
print(list(user.values()))
print(user)

