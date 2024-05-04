# Nested Data Structures

"""
In the previous unit, we saw how to iterate over simple data structures like strings, lists, dictionaries, and sets. In this unit, we will
look at how to iterate over nested data structures. Nested data structures are data structures that contain other data structures. For
example, a list of lists, a list of dictionaries, a dictionary of lists, a dictionary of dictionaries, etc.
"""

"""
Let's look at the runnable example to see how this works if we start with a list of lists where there are three lists of length four. 
If we wanted to write code to transpose this into a list of lists where there are four lists of length three then we would need quite a 
complicated nested for loop.
"""

matrix = [
    [11, 12, 13, 14],
    [15, 16, 17, 18],
    [19, 20, 21, 22],
]
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)


"""Run this code
This is quite a lot of code, but you can see there is an empty list outside the for loop but then another empty list nested within in the 
for loop. Each new list of 3 is created and then appended to the empty list.

See the first runnable example for a simplified version of this code.

Then read the paragraph under the runnable example to see a more real life example. The python tutor link will help you follow the logic 
step by step. There is a second runnable example to practise that."""

# Runnable code examples: 1. Transposing a matrix using nested for loops

print("Transposing a matrix using nested for loops")
print()

matrix = [
    [11, 12, 13, 14],
    [15, 16, 17, 18],
    [19, 20, 21, 22],
]

print([[row[i] for row in matrix] for i in range(4)])



"""
In this runnable example, we see the type of nesting dictionary structure you might find in a database. To access the nested dictionary, 
you string together the commands you would normally use. Therefore payroll['emp1']['name'] goes down one level to get the name of the first 
employee. The get() method can also be used; payroll['emp1'].get('Wage') as in this case to get the first employees wage. We can add and 
delete values as before using their keys. To print this data out in an easily readable fashion, it is best to use a nested loop. The first 
loop gets the key-value pairs and prints the key. The nested loop gets the key-value pairs from the nested dictionary and prints both.
"""

payroll = {'emp1': {'name': 'Precious', 'job': 'Mgr', 'Wage': 50000},
     'emp2': {'name': 'Kim', 'job': 'Dev', 'Wage': 60000},
     'emp3': {'name': 'Sam', 'job': 'Dev', 'Wage': 70000}}

print(payroll)

print(payroll['emp1']['name'])
print(payroll['emp1'].get('salary'))
print(payroll['emp1'].get('Wage'))
payroll['emp4'] = {'name': 'Max', 'job': 'Admin', 'Wage': 30000}
print(payroll)
del payroll['emp3']

for id, info in payroll.items():
    print(f'\nEmployee ID: {id}')
    for key in info:
        print(f'{key} : {info[key]}')
