def add_integers(list_integers):
	total = 0
	for x in list_integers:
		total += x
	return total
    
def multiply_intergers(list_integers):
    total = list_integers[0]
    for x in list_integers:
        # As it is a tuple you can use the in keyword to iterate 
        total = total * x
    return total