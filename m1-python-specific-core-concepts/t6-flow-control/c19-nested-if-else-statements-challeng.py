"""
1.  Write an if-else statement, that checks the variable admin, if it is assigned True pass (using the pass keyword) if it assigned False print: "You need admin privileges to do this"
2.  If you have correctly structured your if-else and run your code it should print out the above string
3.  Remove the pass keyword
4.  And add another if-else statement, that checks the variable update_required, if it is assigned True print: "You are authorized to update" else print: "No update required"
5.  Change the value of the variable admin on line one to: True
6.  If you have correctly structured your nested if-else statement and set the variable admin to True your output should match the image above
"""



admin = True
update_required = True

if admin == True:
    if update_required == True:
        print("You are authorized to update")
    else:
        print("No update required")
else:
    print("You need admin privileges to do this")



