# Catching Generic Errors With “as” Challenge

values = (10, 5)
def append_to_list(ls, val):
    try:
        ls.append(val)
    except AttributeError as e:
        print(e.args[0])
    return ls

result = append_to_list(values, 4)
print(result)







# Do Not Place Code Below This Line 
#this will print out the values variable after the append_to_list function is called
print(values)


