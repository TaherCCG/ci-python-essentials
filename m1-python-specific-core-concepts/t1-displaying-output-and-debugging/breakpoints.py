# Breakpoints are used to pause the execution of a program at a specific point in the code. This is useful for debugging purposes.

"""
Breakpoints using raise SystemExit
Often when editing your code, you would like to stop the program at a specific point to see what state it is in at that time. Python gives an option to raise SystemExit to force it to stop at a particular point. SystemExit , when raised, runs the exit() function in Python. This means the code is exited safely. This is analogous to shutting down your desktop PC from the menu rather than switching off the power at the wall.
In the runnable example, we set the variable age to 17 and then check if age is less than 18. If this is True then the raise SystemExit command will run. This exits the code gracefully. Using the SystemExit exception in your code means that you will be able to look back at the error log files of your programme and see that the code exited because you requested it to rather than for any error with your code.
"""
age1 = 20
if age1 <= 18:
    raise SystemExit('You must be older than 18!') 
else:
    print('You are older than 18!')  
    
age = 17
if age <= 18:
    raise SystemExit('You must be older than 18!')

age2 = 20
if age2 <= 18:
    raise SystemExit('You must be older than 18!') 
else:
    print('You are older than 18!')  
    
age3 = 10
if age3 <= 18:
    raise SystemExit('You must be older than 18!') 
else:
    print('You are older than 18!')  
    

"""
age 1 is 20, so the code will print 'You are older than 18!' and not raise an exception.
age is 17, so the code will raise an exception and print 'You must be older than 18!'
age 2 is 20, but it will not print 'You are older than 18!' because the code will raise an exception before it gets to that line.
age 3 is 10, again it will not print 'You must be older than 18!' because the code will raise an exception before it gets to that line.
"""
