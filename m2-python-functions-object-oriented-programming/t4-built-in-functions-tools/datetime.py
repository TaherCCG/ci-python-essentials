# Datetime

"""
Dates and times can be tricky to work with, when coding. This is due to the differences in how a user may input a date. 
Also, you have to take into account whether the program has access to timezone information and what operating system is 
used by the computer on which you are running the program. There is no date data type in Python. The built-in datetime 
library allows you to manipulate dates and times.


In the runnable example, we have displayed the current date and time on the repl.it server where this code is running. 
The date contains a year, month, day, hour, minute, second and microsecond. The library contains methods to access that
data. We have obtained the year and printed it to the console. A common usage of the datetime library is to get a readable 
string from the datetime object. There is a method called strftime() that takes a parameter format to return the string as
you would like to display it to your user. In the first part of the runnable example we have shown the day of the week.

We can also access date information with python using datetime instance methods such as date() and time(). You can see these
in action in the second part of the runnable example below.

"""

# Runnable example:

from datetime import datetime

x = datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

the_date = datetime.now().date()
print(the_date)

the_time = datetime.now().time()
print(the_time)

