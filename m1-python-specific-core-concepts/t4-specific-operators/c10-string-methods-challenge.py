"""Result
Your result should look like the following:

Grumpy, Dopey, Doc, Happy, Bashful, Sneezy, Sleepy
grumpy, dopey, doc, happy, bashful, sneezy, sleepy
grumpy dopey doc happy bashful sneezy sleepy
['grumpy', 'dopey', 'doc', 'happy', 'bashful', 'sneezy', 'sleepy']

"""


dwarves = "Grumpy, Dopey, Doc, Happy, Bashful, Sneezy, Sleepy"
print(dwarves)


# write your code here

lowercase_string = dwarves.lower()
print(lowercase_string)

commas_removed = lowercase_string.replace(",","")
print(commas_removed)

split_list = commas_removed.split(" ")
print (split_list)