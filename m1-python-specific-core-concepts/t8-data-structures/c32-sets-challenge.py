"""
1.  Use the add() method to add the string "light bulbs" to the products_bought set
2.  use the update() method to add a list of three more products that have been bought ['wood', 'screws', 'saw'] to the products_bought set.
3.  Create a variable has_nails and assign it an expression that checks if "nails" is in the products_bought set.
4.  Create a variable has_paint and assign it an expression that checks if "paint" is in the products_bought set.
5.  Create a variable named unsold_items. Assign it an expression that finds the difference between product_list and products_bought using the difference operator. You will need to convert product_list to a set within the expression
6.  Print out the variable: has_nails
7.  Print out the variable: has_paint
8.  Print out the variable: unsold_items
"""

product_list = ['hammer', 'saw', 'nails', 'wood', 'screws', 'paint', 'brushes', 'light bulbs']
products_bought = {'nails', 'screws', 'hammer', 'wood', 'saw', 'hammer', 'saw', 'nails', 'nails', 'screws', 'hammer'}

# add your code here

products_bought.add('light bulbs')
products_bought.update(['wood', 'screws', 'saw'])

has_nails = 'nails' in products_bought

has_paint = 'paint' in products_bought

unsold_items =set(product_list)-products_bought

print(has_nails)
print(has_paint)
print(unsold_items)