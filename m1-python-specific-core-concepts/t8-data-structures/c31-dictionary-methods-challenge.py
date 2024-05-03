"""
1.  Use the update() method to add a new key-value pair to the challenger dictionary. The key is "occupation" and the value is "Hunter"
2.  Use the get() method to get the value stored at the "occupation" key in the challenger dictionary, and assign the value to a variable named occupation
3.  Add a print statement to print the value of the occupation variable to the terminal.
4.  Use the update() method to update the value stored at the "age" key to 17
5.  Use the pop() method to remove the key-value pair for "status" from the challenger dictionary.
"""

challenger = {
	"name": "Katniss Everdeen",
	"age": 16,
	"district": 12,
	"weapon": "Bow and Arrow", 
	"status": "Victor"
}

# add your code here
challenger.update({'occupation':'Hunter'})
occupation =challenger.get('occupation',0)
print(occupation)
challenger.update({'age':17})
challenger.pop('status')

print(challenger)