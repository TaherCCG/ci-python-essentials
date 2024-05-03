# Nested if-else statements

""" Python Nested If-Else Statements
Nested if-else statements are if-else statements within if-else statements.
They are used to check multiple conditions based on the previous condition.

Syntax:
if condition1:
    if condition2:
        # code block
    else:
        # code block
else:
    # code block
"""


# Example 1: 
exit_program = True
manual_override = False
critical_systems_shutdown = False

if not exit_program and not critical_systems_shutdown:
    if manual_override:
        print("Shutting system down manually")
    else:
        print("This program will not exit just yet")
elif exit_program and critical_systems_shutdown is not True:
    print("Critical systems must be safely shut down before exiting the program")
else:
    print("This program will now be terminated...")

"""
In this example, we have a nested if-else statement that checks multiple conditions.
The outer if-else statement checks if the exit_program and critical_systems_shutdown variables are True or False.
If both variables are False, the inner if-else statement checks the manual_override variable.
If manual_override is True, the program will print "Shutting system down manually".
If manual_override is False, the program will print "This program will not exit just yet".
If exit_program is True and critical_systems_shutdown is not True, the program will print "Critical systems must be safely shut down before exiting the program".
If none of the conditions are met, the program will print "This program will now be terminated..."

In this case, exit_program is True, critical_systems_shutdown is False, and manual_override is False.
Therefore, the outer if-else statement will execute the elif block, and the output will be "Critical systems must be safely shut down before exiting the program"
"""


# Example 2: 
is_raining = True
is_snowing = False
temperature = 25

if is_raining:
    if is_snowing:
        print("It's raining and snowing")
    else:
        print("It's raining")
elif temperature < 32:
    print("It's freezing outside")
else:
    print("It's a beautiful day")

"""
In this example, I have a nested if-else statement that checks multiple conditions.
The outer if-else statement checks if the is_raining variable is True or False.
If is_raining is True, the inner if-else statement checks the is_snowing variable.
If is_snowing is True, the program will print "It's raining and snowing".
If is_snowing is False, the program will print "It's raining".
If is_raining is False, the program will check the temperature variable.
If the temperature is less than 32, the program will print "It's freezing outside".
If none of the conditions are met, the program will print "It's a beautiful day".

In this case, is_raining is True, is_snowing is False, and temperature is 25.
Therefore, the outer if-else statement will execute the else block, and the output will be "It's raining".
"""
