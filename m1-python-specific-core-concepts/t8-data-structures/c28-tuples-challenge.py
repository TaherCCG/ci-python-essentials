"""
1.  Create a tuple variable named cars and pack it with the values of "Tesla", "BMW" and "Ferrari"
2.  Add a print statement to print your cars variable to the terminal.
3.  Create a variable named get_car and use tuple indexing to pull out the "BMW" value from the cars tuple, using the correct index number.
4.  Add a print statement to print the get_car variable to the terminal
5.  Unpack the cars tuple and assign its values to variables named car_one, car_two and car_three
6.  Write three print statements to print out your car_one, car_two and car_three variables to the terminal.
"""





cars =('Tesla','BMW', 'Ferrari')

print(cars)

get_car = cars[1]
print(get_car)

car_one, car_two, car_three = cars

print(car_one)
print(car_two)
print(car_three)
