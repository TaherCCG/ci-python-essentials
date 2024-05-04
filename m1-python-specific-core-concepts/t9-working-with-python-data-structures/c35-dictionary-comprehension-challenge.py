"""
1.  Create a variable named cards_dict.
2.  Assign the value to cards_dict using dictionary comprehension. Loop through the cards list. Build your dictionary using the original list value as the dictionary key, the dictionary value should be the key converted into uppercase letters.
3.  Add a print statement to print the value of the cards_dict variable to the terminal.
"""


cards = ['king', 'queen', 'jack', 'ace']

# write your code here

# iterate through each key in cards list and add value as uppercase letter to cards_dict (dictionery)
cards_dict ={key: key.upper() for key in cards}
# print cards_dict
print(cards_dict)