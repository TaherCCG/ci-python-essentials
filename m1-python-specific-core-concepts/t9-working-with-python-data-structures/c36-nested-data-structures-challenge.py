"""
1.  Declare a variable named student_data and assign it a value of a list.
2.  The list will contain two dictionaries, one for each student. Create the two dictionaries, one after another inside the list. Remembering the syntax needed to separate the two.
3.  Inside the first dictionary, define your key-value pairs:
4.  The first key is name, and its value is the string, John Smith
5.  The second key is email, and its value is the string john@gmail.com
6.  The third key is subjects, and its value is a list of string values for Math, Psychology, Physics, Chemistry and Biology
7.  Inside the second dictionary, define your key-value pairs:
8.  The first key is name, and its value is the string, Mary Jones
9.  The second key is email, and its value is the string mary@gmail.com
10. The third key is subjects, and its value is a list of string values for Fine Art, Music, Biology, Geography and Politics
11. Finally, on a new line after your data has been defined, add a print statement to print your student_data to the terminal.
"""

student_data = [
    {
        'name': 'John Smith', 
        'email':'john@gmail.com', 
        'subjects':['Math', 'Psychology', 'Physics', 'Chemistry', 'Biology']
        
    }, 
    {
        'name': 'Mary Jones', 
        'email':'mary@gmail.com', 
        'subjects':['Fine Art', 'Music', 'Biology', 'Geography', 'Politics']
    }
]

print(student_data)