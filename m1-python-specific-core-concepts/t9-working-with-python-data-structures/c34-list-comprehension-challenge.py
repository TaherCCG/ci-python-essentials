"""
1.  Using list comprehension, add each letter from the string "Marvin" to a list and assign it to a variable named letters.
2.  Write a print statement to print the value of the letters list to the terminal.
3.  Define a variable named numbers and assign it a value of this list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
4.  Using list comprehension, extract the even numbers from the numbers list and assign it to a variable named evens.
5.  Write a print statement to print the value of the evens list to the terminal.
"""

# Add eaxh letter of Marvin to list
letters= [i for i in "Marvin"]
# print letters list
print(letters)

#numbers list
numbers = [1,2,3,4,5,6,7,8,9,10]
# Add even number from numbers list and add to evens list
evens=[x for x in numbers if x % 2 == 0]
# print evens list
print(evens)
