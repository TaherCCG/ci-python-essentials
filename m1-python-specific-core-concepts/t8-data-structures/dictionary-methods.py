# Dictionary Methods 

"""The following are some of the methods that you can use with dictionaries:

Method	                |       Description
=======================================================================================================
clear()	                |       Removes all the elements from the dictionary
copy()	                |       Returns a copy of the dictionary
fromkeys()	            |       Returns a new dictionary with the specified keys and value
get(keyname, value)	    |       Returns the value of the specified keyname. Used in the previous unit. Returns default None if the keyname doesn't exist unless you override this default with a optional value.
items()	                |       Returns a list containing a tuple for each key:value pair
keys()	                |       Returns a list containing the dictionary's keys. Used in the previous unit.
pop()	                |       Removes the element with the specified key
popitem()	            |       Removes the last inserted key:value pair
setdefault()	        |       Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	            |       Updates the dictionary with the specified key:value pairs
values()	            |       Returns a list of all the values in the dictionary. Used in the previous unit.

"""

# Runnable Example: Dictionary Methods
print("Dictionary Methods")
print()

user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

print(user)
print(user.items())
print(user.get('age', 0))
user.update({'home': 'Withywindle, Middle-Earth'})
print(user)
print(user.popitem())
print(user)
user.clear()
print(user)

"""
Note that methods which alter the dictionary (clear() and update()) return None when printed. 
Methods that do not return any value return None as default in Python. 
Other methods like items(), get() and popitem() return items.

In the get() method for age, an optional value of 0 has been included so that will be returned 
rather than None if no age value is in the dictionary. The update() takes another dictionary and 
adds it to the existing one. If the key had already existed in the user dictionary, then its value 
would have been overwritten. The popitem() in this case, removed the 'home' key and its associated 
value as they were the last to be added. The clear() method removed all key:value pairs from the 
dictionary leaving an empty dictionary.
"""