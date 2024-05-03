"""
1.  Using a single list index, get the value of "John" out of the names list and assign it to a variable named name
2.  Use a print statement to print the name variable to the terminal.
3.  Using list slicing, write the code to slice the names list starting at the index of 2, and ending at the index of 4 and assign it to a variable named two_names
4.  Use a print statement to print the two_names variable to the terminal.
5.  Using list slicing, write the code to slice the names list starting at the index of 1, ending at the index of 6 and a step value of 2, and assign it to a variable named other_names
6.  Use a print statement to print the other_names variable to the terminal.
"""

names = ["Mark", "Betty", "John", "Sally", "Bill", "Steven", "Mary", "Emily", "Adam"]

# write your code here

name = names[2]
print(name)

two_names = names[2:4]
print(two_names)

other_names= names[1:6:2]
print(other_names)