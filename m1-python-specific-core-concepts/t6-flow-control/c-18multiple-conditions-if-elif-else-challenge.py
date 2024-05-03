"""
Write an if else statement that checks whether the variable day is equal to "Monday", if it is print: "Meeting at 9:00" else print: "No meetings today"
Within the if else statement add a elif check the checks whether the day is equal to "Wednesday" if it is print: "Meeting at 2:00"
Underneath the elif check add another elif check the checks whether the day is equal to "Friday" if it is print: "Meeting at 4:00"
"""

day = 'Friday'

if day =="Monday":
    print("Meeting at 9:00")
elif day == "Wednesday":
    print("Meeting at 2:00")
elif day =="Friday":
    print("Meeting at 4:00")
else:
    print("No meetings today")

