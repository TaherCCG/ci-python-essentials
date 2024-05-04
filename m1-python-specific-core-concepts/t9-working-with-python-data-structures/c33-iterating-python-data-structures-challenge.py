"""
1.  Create a for loop that loops through each key and value in the data dictionary items.
2.  Inside the for loop, create an if statement that checks if the value is NOT equal to "student"
3.  Inside the if statement, use the capitalize() method to update the string values for all strings that are not "student" so that their first letter is capitalized.
4.  Outside the for loop, add a print statement to print the data to the console.
5.  Create a for loop using range() and len() that loops through the scores list
6.  Inside the for loop, increase each value in the scores list by 1.
7.  Add a print statement to print the value of scores to the console.
"""

data = {
	"first_name": "brian",
	"last_name": "johnson",
	"occupation": "student"
}

scores = [6, 9, 8, 7, 8, 9]

# write your code here

for key, value in data.items():
    if value != "student":
        data[key] =value.capitalize()
    
print(data)

for x in range(len(scores)):
    scores[x] +=1
    
print(scores)
