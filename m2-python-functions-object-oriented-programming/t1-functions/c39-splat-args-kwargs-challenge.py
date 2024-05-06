# Splat! *args & **kwargs Challenge

"""
Define the make_string function:
1.  Create a function named make_string, that uses * correctly with a parameter: strings
2.  The function should return a string of all the values supplied joined, and separated by a space.
3.  The function should return the correct string, no matter how many arguments are passed into the function when it is called, and it will be tested using a different number of arguments

Call the make_string function:
1.  Outside the make_string function, declare a variable named my_string
2.  Assign the value returned from the make_string function to the my_string variable
3.  Call the make_string function with the following values: "Alderaan", "Coruscant", "Dagobah", "Endor", "Hoth".
4.  Print the value of the my_string variable to the terminal

Remember when you pass these values into the function, the *strings converts them into a tuple, So you will be working on a tuple inside the function.
 
Define the get_age function:
1.  Create a function named get_age, that uses ** with a parameter: data
2.  The function should return the value of the age key-value pair passed into the function or return the string: "no age provided" if there is no age key-value pair passed into the function.

Call the get_age function:
1.  Outside the get_age function, declare a variable named pats_age
2.  Assign the value returned from the get_age function to the pats_age variable.
3.  when calling the get_age function, pass it the following key values pairs name="pat", level=4, age=33, occupation="postman".
4.  Print the value of the pats_age variable to the terminal

Remember when you pass these key value pairs into the function, the **data converts them into a dictionary, 
So you will be working on a dictionary inside the function."""




def make_string(*strings):
    return " ".join(strings)

my_string = make_string( "Alderaan", "Coruscant", "Dagobah", "Endor", "Hoth")
print(my_string)

def get_age(**data):
    return data.get('age', 'no age provided')
    
pats_age =get_age(name="pat", level=4, age=33, occupation="postman")
print(pats_age)

