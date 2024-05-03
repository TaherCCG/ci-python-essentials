"""
1.  Using the key "first_name" pull the value for this key from the data dictionary and assign it to a variable called name
2.  Use a print statement to print the value of name to the terminal.
3.  Using the key "species" pull the value for this key from the data dictionary and assign it to a variable called species
4.  Use a print statement to print the value of species to the terminal.
5.  Write the code to insert a new key of "age" with a value of 42 to the data dictionary. (Do not change the data dictionary where it was defined at the top of the file)
"""


data = {
    "first_name": "Arthur",
    "last_name": "Dent",
    "species": "Human"
}

# add your code here

name = data["first_name"]
print(name)
species =data["species"]
print(species)
data["age"]=42


# this will print the data to the terminal
print(data)
