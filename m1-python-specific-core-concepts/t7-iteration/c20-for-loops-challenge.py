"""
1.  Create a variable named users and assign it a list value of ['anna', 'chris', 'brian']
2.  Using the range() and len() methods, create a for loop that loops over the users list.
3.  Inside the for loop, use the capitalize() method to update each entry so that each name starts with a capital letter.
4.  Outside the for loop, print the users list to check you have the correct output.
"""


users = ['anna', 'chris', 'brian']

for x in range(len(users)):
    users[x] = users[x].capitalize()

print(users)