# String Methods
"""
String methods are built-in methods that can be used to manipulate strings.

There are many string methods, some more niche than others.

Method	     |       Description
==================================================
capitalize()	    Capitalizes the first character of the string
center()	        Centers string
count()	            Returns a count of times a specified value occurs in the string
encode()	        Returns an encoded version of the string (use decode() to decode)
endswith()	        Returns True if the string ends with a specified suffix
expandtabs()	    Sets the tab size in spaces of the string
find()	            Returns the lowest index position of where a specified character was found
index()	            Searches for a specified value and returns the position of where it was found or an error if not found
isalnum()	        Returns True if all characters are alphanumeric
isalpha()	        Returns True if all characters are alphabetic
isdigit()	        Returns True if all characters are digits
islower()	        Returns True if all characters are lower case
isspace()	        Returns True if all characters are whitespace
istitle()	        Returns True if the string is titlecased
isupper()	        Returns True if all characters in the string are upper case
join()	            concatenates string
ljust()	            Returns a left justified version of the string
lower()	            Converts a string into lower case
lstrip()	        Returns a left trim version of the string
partition()	        Returns a tuple where the string is parted into two strings and the separator
replace()	        Returns a string where a old value is replaced with a new value
rfind()	            Searches highest index in the string for a specified value
rindex()	        Same but with error if nothing found
rjust()	            Returns a right justified version of the string
rpartition()	    Returns a tuple where the string is parted into three parts
rsplit()	        Splits the string at the specified separator, and returns a list
rstrip()	        Returns a right trim version of the string
split()	            Splits the string at the specified separator, and returns a list
splitlines()	    Splits the string at line breaks and returns a list
startswith()	    Returns true if the string starts with the specified value
strip()	            Returns a trimmed version of the string
swapcase()	        Swaps cases, lower case becomes upper case and vice versa
title()	            Converts the first character of each word to upper case
translate()	        Returns a translated string
upper()	            Converts a string into uppercase
zfill()	            Fills the string with a specified number of 0 values at the beginning


"""

# Runnable Example

print ("String Methods")

print ("lower() method")
my_string = "HELLO WORLD"
my_string_lower_case = my_string.lower()

print(my_string_lower_case)

print ("upper() method")
my_string_2 = "hElLo WorLD"
my_string_2_upper_case = my_string_2.upper()

print (my_string_2_upper_case)
print ("isalpha() method")
print (my_string.isalpha())

print ("replace() method")
greetings = my_string.replace("WORLD", "Dave")
print(greetings)

print ("join() method")
motion = ("jump", "walk", "run")
new_string = "ing ".join(motion)
print(new_string)

print ("split() method")
print(my_string_2.split(" "))

print ("strip() method")
spaced_string = "     42       "
print(spaced_string.strip())